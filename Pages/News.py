import requests
import streamlit as st

import streamlit as st
import requests

st.header("Business News")

# set the API endpoint and parameters
url = "https://newsapi.org/v2/top-headlines?country=us&category=business"
params = {"country": "us", "apiKey": "e05f54f819fb43b4b67385072ad1db10"}

# make the API request and retrieve the data
response = requests.get(url, params=params)
data = response.json()

# display the data in the Streamlit app with formatting

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Business News</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("Here are the top headlines in business:")
for article in data["articles"]:
    st.write("## " + article["title"])
    st.write(article["description"])
    st.write(f"Source: {article['source']['name']}  Published: {article['publishedAt']}")
    st.write("---")


# Set the font family and size using HTML tags
html = f"<div style='font-family: Arial; font-size: 12pt </div>"
# Write the HTML to the Streamlit app
st.write(html, unsafe_allow_html=True)