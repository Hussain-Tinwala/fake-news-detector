# 📰 Fake News & Scam Detection using Machine Learning and NLP

A machine learning-based web application to detect whether a news article is Fake or Real using Natural Language Processing (NLP) techniques and a Logistic Regression model.

This project demonstrates the power of AI to combat misinformation on digital platforms through clean data preprocessing, feature extraction, and predictive modeling.

---

## 🚩 Problem Statement

The rise of fake news and scams on social media platforms has led to widespread misinformation. This project aims to solve this challenge by using AI to classify news content as either Fake or Real.

## 🧑‍💻 Tech Stack

* **Python**
* **Streamlit** (for web app interface)
* **Scikit-learn** (for machine learning model)
* **NLTK** (for NLP preprocessing)
* **Pandas**, **NumPy** (for data manipulation)
* **Joblib** (for model persistence)
* **re** (for regex operations)
* **string** (for string operations)

## 🛠️ How It Works

1.  **Data Collection:**
    Used publicly available datasets from Kaggle consisting of labeled Fake and Real news articles.

2.  **Data Preprocessing:**
    Text cleaning (removal of noise, URLs, HTML tags, punctuation, numbers, and conversion to lowercase).

3.  **Feature Extraction:**
    TF-IDF Vectorization to convert text data into numerical features suitable for machine learning.

4.  **Model Training:**
    A Logistic Regression Classifier is trained on the processed text data.

5.  **Deployment:**
    An interactive web application created with Streamlit allows users to input text and get predictions.

## 🎯 Features

* Clean UI with Streamlit
* Confidence Score for predictions
* Simple input for headlines or article snippets
* Recent Predictions History tracking (if implemented in the app.py)

## 🚀 How to Run Locally

Follow these steps to get the Fake News Detector up and running on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Hussain-Tinwala/fake-news-detector.git
    cd fake-news-detector
    ```

2.  **Install Dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure your `requirements.txt` file contains all the libraries listed in the Tech Stack: `pandas`, `scikit-learn`, `nltk`, `streamlit`, `joblib`, `numpy`)

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```
    Open `http://localhost:8501` in your web browser.

## 📊 Sample Inputs for Testing

You can try the following examples in the web application:

**Real News Examples:**
* "NASA announces new moon mission for 2026"
* "India's GDP grows by 7.8% in Q1"

**Fake News Examples:**
* "Government giving free iPhones to all citizens next week"
* "Elon Musk confirms aliens built SpaceX rockets"

---