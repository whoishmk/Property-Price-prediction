import streamlit as st
import requests
import os

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
        st.success("API Response:")
        st.write(first_content)
    else:
        st.error(f"Failed to fetch data from API. Status Code: {response.status_code}")
