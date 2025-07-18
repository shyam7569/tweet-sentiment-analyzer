import streamlit as st
import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
# pathlib and time are no longer strictly needed without file path input or time.sleep for API
# from pathlib import Path
# import time

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Tweet Sentiment Analyzer",
    layout="wide", # Use wide layout for better visualization space
    initial_sidebar_state="expanded"
)

# --- Initialize matplotlib with cyberpunk aesthetic ---
# These settings will apply to all matplotlib plots generated in the app
plt.style.use('dark_background')
# Define a custom color palette with neon colors for better cyberpunk feel
sns.set_palette(['#22c55e', '#3b82f6', '#ef4444', '#a855f7', '#f97316'])
plt.rcParams.update({
    'text.color': 'white',
    'axes.labelcolor': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'axes.edgecolor': '#3b82f6', # Neon blue for axis lines
    'figure.facecolor': '#1e1e5f', # Dark purple for figure background
    'axes.facecolor': '#0a0a23' # Very dark blue for plot area background
})

# --- Optimized tweet cleaning function (vectorized for performance) ---
@st.cache_data # Cache this function to avoid re-running on every interaction
def clean_tweet(text_series: pd.Series) -> pd.Series:
    """
    Cleans a pandas Series of tweet texts by removing URLs, mentions,
    hashtags, and non-alphabetic characters, then converts to lowercase.

    Args:
        text_series (pd.Series): A Series containing tweet texts.

    Returns:
        pd.Series: A Series of cleaned tweet texts.
    """
    text = text_series.astype(str)
    # Remove URLs (http, https, www)
    text = text.str.replace(r"http\S+|www\S+|https\S+", '', regex=True, flags=re.MULTILINE)
    # Remove mentions (@username) and standalone hashtags (#, which are often left after URL removal)
    text = text.str.replace(r'\@\w+|\\#', '', regex=True)
    # Remove non-alphabetic characters (keep spaces)
    text = text.str.replace(r"[^a-zA-Z\s]", '', regex=True)
    # Convert to lowercase and strip leading/trailing whitespace
    return text.str.lower().str.strip()

# --- Optimized sentiment analysis function ---
@st.cache_data # Cache this function to avoid re-running on every interaction
def apply_sentiment_analysis(df: pd.DataFrame, text_column: str = 'cleaned_content') -> pd.DataFrame:
    """
    Applies VADER sentiment analysis to a specified text column in a DataFrame
    and adds sentiment scores (pos, neu, neg, compound) and a sentiment label.

    Args:
        df (pd.DataFrame): The input DataFrame.
        text_column (str): The name of the column containing text for analysis.

    Returns:
        pd.DataFrame: The DataFrame with added sentiment columns.
    """
    analyzer = SentimentIntensityAnalyzer()
    # Apply sentiment analysis to each text and store scores in a list
    scores = [analyzer.polarity_scores(text) for text in df[text_column]]
    # Convert list of score dictionaries to a DataFrame
    df_scores = pd.DataFrame(scores)
    # Rename columns to avoid conflicts and indicate they are sentiment scores
    df_scores.columns = [f"sent_{col}" for col in df_scores.columns]
    # Concatenate the new sentiment score DataFrame with the original DataFrame
    df = pd.concat([df, df_scores], axis=1)
    # Determine sentiment label based on compound score
    df['sentiment_label'] = df['sent_compound'].apply(
        lambda x: 'positive' if x > 0.05 else 'negative' if x < -0.05 else 'neutral'
    )
    return df

# --- Load and process dataset function ---
@st.cache_data # Cache this function to avoid re-running on every file upload
def load_and_process_data(uploaded_file) -> pd.DataFrame:
    """
    Loads a CSV file from a Streamlit UploadedFile object, cleans the content,
    and performs sentiment analysis.

    Args:
        uploaded_file: A Streamlit UploadedFile object.

    Returns:
        pd.DataFrame: The processed DataFrame, or None if an error occurs.
    """
    try:
        df = pd.read_csv(uploaded_file)
        # Ensure 'content' column exists
        if 'content' not in df.columns:
            st.error("❌ Error: The uploaded CSV must contain a 'content' column with tweet text.")
            return None

        # Apply cleaning and sentiment analysis
        df['cleaned_content'] = clean_tweet(df['content'])
        df = apply_sentiment_analysis(df)
        # Rename 'lang' to 'language' for consistency, if 'lang' exists
        if 'lang' in df.columns:
            df = df.rename(columns={'lang': 'language'})
        else:
            df['language'] = 'unknown' # Default if no language column

        return df
    except Exception as e:
        st.error(f"❌ Error processing dataset: {e}")
        return None

# --- Visualize distributions function (modified for Streamlit) ---
def visualize_distribution(data: pd.DataFrame, column: str, title: str, top_n: int = 10, is_pie: bool = False) -> plt.Figure:
    """
    Generates a matplotlib figure for distribution visualization (bar or pie chart).

    Args:
        data (pd.DataFrame): The input DataFrame.
        column (str): The column to visualize.
        title (str): The title of the plot.
        top_n (int): Number of top categories to display for bar chart.
        is_pie (bool): If True, generates a pie chart; otherwise, a bar chart.

    Returns:
        plt.Figure: The generated matplotlib figure.
    """
    # Create a new figure and axes for each plot
    fig, ax = plt.subplots(figsize=(10 if not is_pie else 8, 6 if not is_pie else 8))
    counts = data[column].value_counts().head(top_n)

    if is_pie:
        # Ensure counts are not empty to avoid error in pie plot
        if not counts.empty:
            counts.plot.pie(autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12}, ax=ax)
            ax.set_ylabel('') # Hide default y-label for pie chart
        else:
            ax.text(0.5, 0.5, "No data to display", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=14, color='gray')
            ax.set_xticks([])
            ax.set_yticks([])
    else:
        if not counts.empty:
            sns.barplot(x=counts.index, y=counts.values, edgecolor='white', ax=ax)
            ax.set_xlabel(column.capitalize(), fontsize=12)
            ax.set_ylabel('Number of Tweets', fontsize=12)
            plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for readability
        else:
            ax.text(0.5, 0.5, "No data to display", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=14, color='gray')
            ax.set_xticks([])
            ax.set_yticks([])

    ax.set_title(title, fontsize=16, pad=20, weight='bold')
    plt.tight_layout()
    return fig

# --- Streamlit Application Main Logic ---
def main():
    st.title("🌊 Tweet Sentiment Analysis and Visualization")
    st.markdown("""
    This application allows you to upload a CSV file containing tweets for sentiment analysis
    and visualize the distribution of languages and sentiments.
    """)

    st.sidebar.header("Data Input")
    uploaded_file = st.sidebar.file_uploader("Upload your tweet CSV file", type=["csv"])

    df = None
    if uploaded_file is not None:
        st.info("📊 Processing uploaded dataset... This may take a moment.")
        df = load_and_process_data(uploaded_file)

        if df is not None and not df.empty:
            st.success("✅ Dataset processed successfully!")

            # Display sample of processed data
            st.subheader("📄 Sample of Processed Data")
            output_cols = ['content', 'cleaned_content', 'language', 'sent_pos', 'sent_neu', 'sent_neg', 'sent_compound', 'sentiment_label']
            # Ensure all output_cols exist in df before selecting
            existing_output_cols = [col for col in output_cols if col in df.columns]
            st.dataframe(df[existing_output_cols].head(5))

            st.markdown("---")
            st.header("📈 Data Visualizations")

            # Create columns for side-by-side plots
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Top 10 Languages in Tweets")
                # Pass the figure object to st.pyplot
                fig_lang_bar = visualize_distribution(df, 'language', 'Top 10 Languages in Tweets', is_pie=False)
                st.pyplot(fig_lang_bar)

            with col2:
                st.subheader("Language Distribution")
                fig_lang_pie = visualize_distribution(df, 'language', 'Language Distribution', is_pie=True)
                st.pyplot(fig_lang_pie)

            col3, col4 = st.columns(2)
            with col3:
                st.subheader("Sentiment Distribution (Bar Chart)")
                fig_sentiment_bar = visualize_distribution(df, 'sentiment_label', 'Sentiment Distribution in Tweets', is_pie=False)
                st.pyplot(fig_sentiment_bar)

            with col4:
                st.subheader("Sentiment Distribution (Pie Chart)")
                fig_sentiment_pie = visualize_distribution(df, 'sentiment_label', 'Sentiment Distribution', is_pie=True)
                st.pyplot(fig_sentiment_pie)
        elif df is not None and df.empty:
            st.warning("The uploaded file was processed, but it appears to be empty or contains no valid data.")
        # Error messages for file processing are handled within load_and_process_data

# This block is only executed when the script is run directly
if __name__ == '__main__':
    main()
#python -m streamlit run sentiment_app_no_live.py