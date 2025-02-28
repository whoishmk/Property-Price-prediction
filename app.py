import streamlit as st
import requests

# Retrieve the API key from Streamlit secrets.
# In your secrets.toml file, add:
# [api]
# OPENROUTER_API_KEY = "your_actual_api_key_here"
API_KEY = st.secrets["api"]["OPENROUTER_API_KEY"]

API_URL = 'https://openrouter.ai/api/v1/chat/completions'

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

st.title("Property Price Prediction")

# Input widgets for user data
area = st.text_input("Enter the area:")
city = st.text_input("Enter the city:")
bhk = st.text_input("Enter the BHK:")
gated = st.text_input("Enter Gated:")
flat = st.text_input("Enter Flat:")

if st.button("Submit"):
    # Define the request payload (data)
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {
                "role": "user", 
                "content": f"Average property price in {area} {city} for a {bhk} {gated} {flat} and what will be the price in future , just write the numbers and years"
            }
        ]
    }
    
    # Send the POST request to the API
    response = requests.post(API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        api_response = response.json()
        first_content = api_response['choices'][0]['message']['content']  # Extract first content
        st.success("API Response:")
        st.write(first_content)
    else:
        st.error(f"Failed to fetch data from API. Status Code: {response.status_code}")
