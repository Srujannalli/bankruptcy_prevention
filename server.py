import streamlit as st
import joblib
import pandas as pd
import sklearn
# Load the trained model
model = joblib.load('saved_model.pkl')

st.title('Bankruptcy Prediction App')

# Input form for user to enter feature values
st.header('Enter Feature Values:')
feature1 = st.number_input('industrial_risk')
feature2 = st.number_input('management_risk')
feature3 = st.number_input('financial_flexibility')
feature4 = st.number_input('credibility')
feature5 = st.number_input('competitiveness')
# Add more input fields for other features as needed

# Create a dictionary from user input
user_input = {
    'industrial_risk': [feature1],
    'management_risk': [feature2],
    'financial_flexibility': [feature3],
    'credibility': [feature4],
    'competitiveness': [feature5],
    # Include other features
}

user_data = pd.DataFrame(user_input)

# Make predictions
if st.button('Predict'):
    prediction = model.predict(user_data)
    if prediction == 'bankruptcy':
        st.error('Bankruptcy: Yes')
    else:
        st.success('Bankruptcy: No')

st.text('Note: Click "Predict" to see the prediction result.')


