import streamlit as st
import requests
import os
import numpy as np

# Replace with your OpenRouter API key

API_URL = 'https://openrouter.ai/api/v1/chat/completions'
os.environ['API_KEY'] = st.secrets['API_KEY']

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {os.environ['API_KEY']}',
    'Content-Type': 'application/json'
}

st.title("Property Price Prediction")
#image
from PIL import Image
image = Image.open('vyza_solutions_pvt_ltd_cover.jpg')
st.image(image, caption='Hasib Md. Khan | Vyza Solutions Pvt. Ltd.')

# Input widgets for user data
area = st.text_input("Enter the area:")
city = st.text_input("Enter the city:")
bhk = st.text_input("Enter the number of Bedrooms:")
age = st.text_input("Enter the age of the property: (in years)" )
gated = st.radio("Select Gated or not: ", ('Yes', 'No'))


if (gated == 'Yes'):
    st.success("Gated")
else:
    st.success("Not gated")
                
property = st.radio("Select Type of Property: ", ('Apartment', 'House' , 'Villa','Building'))


if (property == 'Apartment'):
    st.success("Apartment")
elif (property == 'House'):
    st.success("House")
elif (property == 'Building'):
    st.success("Building")
else:
    st.success("Villa")

 
if st.button("Submit"):
    # Define the reyquest payload (data)
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {
                "role": "user", 
                "content": f"Average property price in {area} {city} for a {bhk} {gated} which was built in {age} {property} in 2025 and what will be the price in future , just write the numbers and years"
            }
        ]
    }
    
    # Send the POST request to the API
    response = requests.post(API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        api_response = response.json()
        first_content = api_response['choices'][0]['message']['content']  # Extract first content
        st.success("Predicted Prices:")
        st.write(first_content)
    else:
        st.error(f"Failed to fetch data from API. Status Code: {response.status_code}")


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Create a synthetic dataset with four categories.
data = [
    # Affordable Residential
    ("This locality offers affordable housing options, cost-effective apartments, and budget-friendly rentals.", "Affordable Residential"),
    ("Middle-income families find value in the budget-friendly and affordable residential neighborhood.", "Affordable Residential"),
    ("An economical area with low-cost housing and great value for money.", "Affordable Residential"),
    ("Affordable residential community with plenty of budget apartments.", "Affordable Residential"),
    ("A cost-effective, value-driven locality perfect for middle-income residents.", "Affordable Residential"),
    
    # Upscale Residential
    ("The area is known for its upscale residential community, luxury apartments, and high-end villas.", "Upscale Residential"),
    ("Premium living with exclusive neighborhoods and expensive housing.", "Upscale Residential"),
    ("An upscale locality with sophisticated architecture and premium amenities.", "Upscale Residential"),
    ("High-end residential area with luxury homes and exclusive communities.", "Upscale Residential"),
    ("Exclusive, upscale residential neighborhood with elegant houses and a posh lifestyle.", "Upscale Residential"),
    
    # IT Hub
    ("This locality is a bustling IT hub with major tech parks and corporate offices.", "IT Hub"),
    ("An area dominated by IT companies, start-up ecosystems, and modern office complexes.", "IT Hub"),
    ("Tech-savvy and dynamic, with numerous IT parks and high-tech infrastructure.", "IT Hub"),
    ("A vibrant IT hub with corporate buildings, tech startups, and modern amenities.", "IT Hub"),
    ("The region is known for its tech parks, innovative IT firms, and a dynamic work environment.", "IT Hub"),
    
    # Heritage
    ("A traditional locality steeped in history with cultural landmarks and heritage buildings.", "Heritage"),
    ("This area is known for its rich heritage, historical monuments, and traditional architecture.", "Heritage"),
    ("An old and established neighborhood with a strong cultural heritage and classic charm.", "Heritage"),
    ("Heritage area featuring historic sites, ancient temples, and traditional markets.", "Heritage"),
    ("A culturally rich locality with heritage architecture and historical significance.", "Heritage"),
    
    # Commercial
    ("This locality is a vibrant commercial center, hosting numerous retail outlets and business offices.", "Commercial"),
    ("A bustling business district with modern shopping malls, office complexes, and eateries.", "Commercial"),
    ("This area is known for its commercial dynamism with high foot traffic and a variety of retail spaces.", "Commercial"),
    ("The commercial hub of the city, with a mix of shopping centers, banks, and corporate offices.", "Commercial"),
    ("A thriving commercial area featuring local markets, upscale retail stores, and entertainment options.", "Commercial"),
    
    # Mixed-Use
    ("A mixed-use locality that offers a balance of residential housing, commercial spaces, and recreational areas.", "Mixed-Use"),
    ("This area is designed as a mixed-use community, blending apartments, offices, and leisure facilities.", "Mixed-Use"),
    ("A vibrant mixed-use neighborhood with integrated living spaces, retail, and public amenities.", "Mixed-Use"),
    ("A modern locality with a mix of residential buildings, business centers, and community parks.", "Mixed-Use"),
    ("An urban mixed-use development featuring housing, shopping, and entertainment options.", "Mixed-Use")
]

# Create a DataFrame from the dataset.
df = pd.DataFrame(data, columns=["Description", "Category"])

# Preprocess the text by converting it to lowercase.
df["Cleaned_Description"] = df["Description"].str.lower()

# Split the dataset into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(
    df["Cleaned_Description"], df["Category"], test_size=0.2, random_state=42
)

# Build a machine learning pipeline:
# 1. TF-IDF Vectorizer to transform text into numerical features.
# 2. Logistic Regression classifier for categorization.
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(solver="liblinear"))
])

# Train the model.
pipeline.fit(X_train, y_train)

# Evaluate the model.
y_pred = pipeline.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Example: Predict the category of a new description.
new_sentence = first_content
predicted_category = pipeline.predict([new_sentence.lower()])
print("New sentence classified as:", predicted_category[0])
