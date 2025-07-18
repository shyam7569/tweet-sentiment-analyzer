# 🌊 Tweet Sentiment Analyzer: A Cyberpunk Journey into Social Media Insights

## 🚀 Project Overview
Welcome to the **Tweet Sentiment Analyzer**, a cutting-edge web application crafted to dive deep into the emotional pulse of tweets about the 2022 Pakistan floods. Built with **Streamlit**, this project leverages the power of **VADER Sentiment Analysis**, **Pandas**, **Matplotlib**, and **Seaborn** to transform raw tweet data into meaningful insights. With a sleek cyberpunk aesthetic, the app delivers interactive visualizations and a seamless user experience, making it a powerful tool for understanding public sentiment during crises. This project was born from an iterative development process, overcoming challenges like local execution hurdles and Twitter API limitations, to deliver a robust, cloud-hosted solution.

## 🌟 Features
- **📂 File Upload**: Upload a CSV file (like `FloodsInPakistan-tweets.csv`) with a `content` column for tweet text analysis.
- **🧹 Text Cleaning**: Strips away URLs, mentions, hashtags, and non-alphabetic characters, ensuring clean text for analysis.
- **😊 Sentiment Analysis**: Uses VADER to compute positive, neutral, negative, and compound sentiment scores, labeling tweets as positive, neutral, or negative.
- **📊 Visualizations**: Renders vibrant bar and pie charts showcasing language and sentiment distributions, styled in a neon-drenched cyberpunk theme.
- **🖥️ Interactive Interface**: Streamlit’s wide layout and sidebar provide an intuitive experience, with cached functions for blazing-fast performance.
- **☁️ Cloud Deployment**: Hosted on Streamlit Community Cloud for global accessibility.

## 🛠️ Requirements
The project depends on the following Python libraries, listed in `requirements.txt`:
- `streamlit`: For the web interface.
- `pandas`: For data manipulation.
- `vaderSentiment`: For sentiment analysis.
- `matplotlib`: For plotting visualizations.
- `seaborn`: For enhanced, stylish visualizations.

## 📥 Installation
Follow these steps to set up the project locally:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/tweet-sentiment-analyzer.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd tweet-sentiment-analyzer
   ```
3. **Create a Virtual Environment** (recommended for dependency isolation):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🖱️ Running Locally
To launch the app on your machine:
1. Ensure all dependencies are installed.
2. Run the Streamlit application:
   ```bash
   streamlit run sentiment_app_no_live.py
   ```
3. Open the local URL (e.g., `http://localhost:8501`) in your browser.
4. Upload a CSV file (e.g., `FloodsInPakistan-tweets.csv`) to explore the data and visualizations.

## ☁️ Deploying to Streamlit Community Cloud
Make your app accessible worldwide with Streamlit Community Cloud:
1. **Push to GitHub**:
   - Initialize a Git repository and push your files:
     ```bash
     git init
     git add .
     git commit -m "Initial commit with Tweet Sentiment Analyzer"
     git remote add origin https://github.com/your-username/tweet-sentiment-analyzer.git
     git push -u origin main
     ```
2. **Sign Up/Log In**:
   - Create an account or log in at [Streamlit Community Cloud](https://streamlit.io/cloud).
3. **Create a New App**:
   - Click "New app" and connect your GitHub repository.
   - Set the main script path to `sentiment_app_no_live.py`.
   - Ensure `requirements.txt` is in the repository root for dependency installation.
4. **Deploy the App**:
   - Click "Deploy" to build and host the app.
   - Once deployed, you’ll receive a public URL (e.g., `https://your-app-name.streamlit.app`).
5. **Test the Deployment**:
   - Visit the public URL, upload `FloodsInPakistan-tweets.csv`, and verify that the app processes data and displays visualizations correctly.

## 🎮 Usage
- **Upload Data**: Use the sidebar to upload a CSV file containing tweet data. The file must include a `content` column with tweet text.
- **View Results**: Explore a sample of processed data, including original and cleaned text, language, sentiment scores, and labels.
- **Visualize Insights**: Enjoy four interactive charts:
  - **Top 10 Languages (Bar)**: Displays the most common languages in the dataset.
  - **Language Distribution (Pie)**: Shows the proportion of each language.
  - **Sentiment Distribution (Bar)**: Highlights the count of positive, neutral, and negative tweets.
  - **Sentiment Distribution (Pie)**: Visualizes sentiment proportions.
- **Error Handling**: The app provides clear error messages if the CSV lacks a `content` column or is empty.

## 🧬 Development Journey
The Tweet Sentiment Analyzer was crafted through a dynamic, iterative process, overcoming technical hurdles to deliver a polished product. Here’s a glimpse into the journey:

### Initial Vision
The goal was to create a web interface for a Python script analyzing tweet sentiments, focusing on the 2022 Pakistan floods. The app needed to process a CSV file, clean text, perform sentiment analysis, and present visualizations in an accessible format.

### Challenges Overcome
- **Local Execution Woes**: Early attempts to run Streamlit locally faced dependency conflicts and environment issues. These were resolved by using a virtual environment and ensuring Python 3.8+ compatibility.
- **Twitter API Roadblocks**: Plans to fetch live tweets via the Twitter API were thwarted by rate limits (e.g., 100 tweets per request, 15-minute windows). The solution was to pivot to static CSV input, using the provided `FloodsInPakistan-tweets.csv`.
- **Performance Optimization**: Initial versions were slow due to repetitive data processing. Implementing Streamlit’s `@st.cache_data` decorator for key functions (`clean_tweet`, `apply_sentiment_analysis`, `load_and_process_data`) significantly boosted performance.

### Iterative Enhancements
- **Framework Choice**: Explored Flask and Django but chose Streamlit for its rapid development and visualization capabilities.
- **Cyberpunk Aesthetic**: Applied a dark background with neon colors (e.g., `#22c55e`, `#3b82f6`) to Matplotlib/Seaborn plots, creating a futuristic vibe.
- **UI Refinement**: Adopted Streamlit’s wide layout, sidebar file uploader, and side-by-side chart displays for a modern, user-friendly interface.
- **Final Script**: The `sentiment_app_no_live.py` script integrates all features, with robust error handling and optimized performance.

## 📊 Sample Dataset
The included `FloodsInPakistan-tweets.csv` contains real tweets about the 2022 Pakistan floods, with columns like `content` (tweet text), `lang` (language), and more. The `content` column is essential for text processing, while `lang` is used for language distribution analysis.

## 🌍 Impact and Use Cases
This application is a powerful tool for researchers, NGOs, and policymakers analyzing public sentiment during crises. By visualizing language and sentiment distributions, it reveals how communities respond to disasters, aiding in targeted relief efforts. The cyberpunk aesthetic makes data exploration engaging, while Streamlit Community Cloud ensures accessibility.

## 🔮 Future Enhancements
- **Live Data Streaming**: Integrate Twitter API with elevated access to fetch real-time tweets (if rate limits are resolved).
- **Additional Visualizations**: Add word clouds or time-series analysis to uncover trends.
- **Multilingual Support**: Enhance cleaning and analysis for non-English tweets.
- **Export Options**: Allow users to download processed data or charts.

## 📜 License
This project is licensed under the [MIT License](LICENSE), encouraging open collaboration and innovation.

## 🙏 Acknowledgments
- **VADER Sentiment**: For robust sentiment analysis.
- **Streamlit Community**: For an intuitive platform and cloud hosting.
- **Matplotlib/Seaborn**: For bringing data to life with style.
- **You**: For exploring this project and joining the journey to uncover social media insights!