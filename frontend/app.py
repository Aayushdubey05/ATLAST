import streamlit as st
import requests

# Define the backend API endpoint
API_ENDPOINT = "http://localhost:5000/api/recommend"

st.title("Stock Recommendation")

# Display button to fetch stock recommendation
if st.button("Get Stock Recommendation"):
    try:
        # Send GET request to backend API
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            # Extract and display recommended product
            recommendation = response.json().get("recommendation", "No recommendation found.")
            st.write("Recommended Product for Stock Increase:")
            st.json(recommendation)
        else:
            st.write("Failed to fetch recommendation. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        st.write("Error:", e)
