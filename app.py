import streamlit as st
import pickle

# load model
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('spam_vectorizer.pkl', 'rb'))

st.title("Email Spam Detector")

input_mail = st.text_area("Enter Email Text")

if st.button("Predict"):
    data = vectorizer.transform([input_mail])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Ham Mail ✅")
    else:
        st.error("Spam Mail 🚫")