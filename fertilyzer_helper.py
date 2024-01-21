import pandas as pd
from sklearn import model_selection
from sklearn import tree
from sklearn import metrics
import streamlit as st

# Load data
data = pd.read_csv('/Users/tript/farm/Fp.csv')

# Features and target
x = data[['Temparature', 'Humidity ', 'Moisture', 'Nitrogen', 'Potassium', 'Phosphorous']]
y = data['Fertilizer Name']

# Train-test split
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.4, random_state=42)

# Decision Tree model
model = tree.DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

# Streamlit UI
st.title("Crop Prediction App")

# User input through sliders
temperature = st.slider("Enter Temperature level:", float(x['Temparature'].min()), float(x['Temparature'].max()), float(x['Temparature'].mean()))
humidity = st.slider("Enter Humidity level:", float(x['Humidity '].min()), float(x['Humidity '].max()), float(x['Humidity '].mean()))
moisture = st.slider("Enter Moisture level:", float(x['Moisture'].min()), float(x['Moisture'].max()), float(x['Moisture'].mean()))
nitrogen = st.slider("Enter Nitrogen level:", float(x['Nitrogen'].min()), float(x['Nitrogen'].max()), float(x['Nitrogen'].mean()))
potassium = st.slider("Enter Potassium level:", float(x['Potassium'].min()), float(x['Potassium'].max()), float(x['Potassium'].mean()))
phosphorous = st.slider("Enter Phosphorous level:", float(x['Phosphorous'].min()), float(x['Phosphorous'].max()), float(x['Phosphorous'].mean()))

# Create a DataFrame for the new data
new_data = pd.DataFrame({
    'Temparature': [temperature],
    'Humidity ': [humidity],
    'Moisture': [moisture],
    'Nitrogen': [nitrogen],
    'Potassium': [potassium],
    'Phosphorous': [phosphorous]
})

# Make a prediction
predicted_crop = model.predict(new_data)

# Display the predicted crop category
st.write(f"Predicted Crop Category: {predicted_crop[0]}")
