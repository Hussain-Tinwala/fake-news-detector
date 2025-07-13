📰 Fake News & Scam Detection using Machine Learning and NLP
A machine learning-based web application to detect whether a news article is Fake or Real using Natural Language Processing (NLP) techniques and a Logistic Regression model.

This project demonstrates the power of AI to combat misinformation on digital platforms through clean data preprocessing, feature extraction, and predictive modeling.

🚩 Problem Statement
The rise of fake news and scams on social media platforms has led to widespread misinformation. This project aims to solve this challenge by using AI to classify news content as either Fake or Real.

🧑‍💻 Tech Stack
Python

Streamlit (for web app interface)

Scikit-learn (for machine learning model)

NLTK (for NLP preprocessing)

Pandas, NumPy (for data manipulation)

🛠️ How It Works

1️⃣ Data Collection
Used publicly available datasets from Kaggle consisting of labeled Fake and Real news articles.

2️⃣ Data Preprocessing
Text Cleaning (removal of noise, URLs, HTML tags)

3️⃣ Model Training
Logistic Regression Classifier

4️⃣ Deployment
Interactive web app created with Streamlit

🎯 Features
Clean UI with Streamlit

Confidence Score for predictions

Simple input for headlines or article snippets

Recent Predictions History tracking

🚀 How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/Hussain-Tinwala/fake-news-detector.git
cd fake-news-detector

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
streamlit run app.py

Open http://localhost:8501 in your browser.

📊 Sample Inputs for Testing
Real News Examples
"NASA announces new moon mission for 2026"

"India's GDP grows by 7.8% in Q1"

Fake News Examples
"Government giving free iPhones to all citizens next week"

"Elon Musk confirms aliens built SpaceX rockets"
