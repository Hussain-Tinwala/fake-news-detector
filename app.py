import streamlit as st
import numpy as np
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Title and page config
st.set_page_config(page_title="Fake News Detector", layout="wide")
st.title("📰 Fake News & Scam Detector")
st.markdown("Detect if a news article is **Fake** or **Real** using Machine Learning and NLP")

# Load and prepare data
news_df = pd.read_csv('train.csv')
news_df = news_df.fillna(' ')
news_df['content'] = news_df['author'] + ' ' + news_df['title']

# Preprocess data
ps = PorterStemmer()
def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [ps.stem(word) for word in stemmed_content if word not in stopwords.words('english')]
    return ' '.join(stemmed_content)

news_df['content'] = news_df['content'].apply(stemming)

# TF-IDF
X = news_df['content'].values
y = news_df['label'].values
vector = TfidfVectorizer()
vector.fit(X)
X = vector.transform(X)

# Train/test split and model training
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=2)
model = LogisticRegression()
model.fit(X_train, Y_train)

# Accuracy for display
accuracy = accuracy_score(Y_test, model.predict(X_test)) * 100

# Sidebar
with st.sidebar:
    st.header("📊 Project Info")
    st.write("This app uses a Logistic Regression model trained on a news dataset to predict whether a news article is real or fake.")
    st.write("Model Accuracy: **{:.2f}%**".format(accuracy))
    st.markdown("---")
    st.write("**Tech Stack:** Python, Scikit-learn, NLP, Streamlit")

# Prediction function
def prediction(input_text):
    processed = stemming(input_text)
    transformed = vector.transform([processed])
    pred = model.predict(transformed)
    prob = model.predict_proba(transformed)[0]
    return pred[0], prob

# User input
input_text = st.text_area("🔍 Enter a news headline or short article below:")

# Detect button
if st.button("🧠 Detect"):
    if input_text.strip() != "":
        label, probability = prediction(input_text)
        if label == 1:
            st.error("🚨 **Fake News Detected!**")
        else:
            st.success("✅ **Real News Detected!**")

        st.markdown("#### 📈 Confidence Score")
        st.progress(int(probability[label] * 100))
        st.write("Confidence: **{:.2f}%**".format(probability[label] * 100))
    else:
        st.warning("Please enter some text.")

# Optional: Add a prediction history (session-based)
if 'history' not in st.session_state:
    st.session_state.history = []

if input_text:
    st.session_state.history.append((input_text, "Fake" if label == 1 else "Real"))

if st.session_state.history:
    st.markdown("### 📝 Recent Predictions")
    for i, (text, result) in enumerate(reversed(st.session_state.history[-5:])):
        st.write(f"{i+1}. **{result}** → {text[:60]}...")

