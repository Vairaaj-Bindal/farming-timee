import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset (replace 'crop_data.csv' with your actual dataset file)
data = pd.read_csv('Crop_recommendation.csv')

# Separate features (soil and environmental parameters) and target (crop categories)
X = data[['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall']]
y = data['label']

# train and test   
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree !!
model = DecisionTreeClassifier(random_state=42)

# Train i
model.fit(X_train, y_train)

# M predictions 
y_pred = model.predict(X_test)

# Calcuate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

N = float(input("Enter Nitrogen level: "))
P = float(input("Enter Phosphorous level: "))
K = float(input("Enter Potassium level: "))
temperature = float(input("Enter Temperature: "))
ph = float(input("Enter pH value: "))
humidity = float(input("Enter Humidity level: "))
rainfall = float(input("Enter Rainfall: "))

# Create a new DataFrame with the ser input
new_data = pd.DataFrame({
    'N': [N],
    'P': [P],
    'K': [K],
    'temperature': [temperature],
    'ph': [ph],
    'humidity': [humidity],
    'Rainfall': [rainfall]
})

# Predict the crop category based on the input
predicted_crop = model.predict(new_data)
print(f"Predicted Crop Category: {predicted_crop[0]}")
