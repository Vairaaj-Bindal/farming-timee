import streamlit as st
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Load the dataset (replace 'Crop_recommendation.csv' with your actual dataset file)
data = pd.read_csv('/Users/tript/farm/Crop_recommendation.csv')

# Separate features (soil and environmental parameters) and target (crop categories)
X = data[['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall']]
y = data['label']

# Train and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Decision Tree
model = tree.DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Streamlit app
st.title("Crop Prediction App") 

# User input for new data
N = st.slider("Enter Nitrogen level", float(X['N'].min()), float(X['N'].max()), float(X['N'].mean()))
P = st.slider("Enter Phosphorous level", float(X['P'].min()), float(X['P'].max()), float(X['P'].mean()))
K = st.slider("Enter Potassium level", float(X['K'].min()), float(X['K'].max()), float(X['K'].mean()))
temperature = st.slider("Enter Temperature", float(X['temperature'].min()), float(X['temperature'].max()), float(X['temperature'].mean()))
ph = st.slider("Enter pH value", float(X['ph'].min()), float(X['ph'].max()), float(X['ph'].mean()))
humidity = st.slider("Enter Humidity level", float(X['humidity'].min()), float(X['humidity'].max()), float(X['humidity'].mean()))
rainfall = st.slider("Enter Rainfall", float(X['rainfall'].min()), float(X['rainfall'].max()), float(X['rainfall'].mean()))

# Create a new DataFrame with the user input
new_data = pd.DataFrame({
    'N': [N],
    'P': [P],
    'K': [K],
    'temperature': [temperature],
    'ph': [ph],
    'humidity': [humidity],
    'rainfall': [rainfall]
})

# Predict the crop category based on the input
predicted_crop = model.predict(new_data)
st.write(f"Predicted Crop Category: {predicted_crop[0]}")

