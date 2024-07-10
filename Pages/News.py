import requests
import streamlit as st
from urllib.parse import quote

# Function to fetch Business News data
def get_business_news_data():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business"
    params = {"country": "us", "apiKey": "e05f54f819fb43b4b67385072ad1db10"}
    response = requests.get(url, params=params)
    return response.json()["articles"]

# Function to fetch Wall Street Journal Articles data
def get_wall_street_journal_data():
    url = "https://newsapi.org/v2/everything?domains=wsj.com"
    params = {"apiKey": "e05f54f819fb43b4b67385072ad1db10"}
    response = requests.get(url, params=params)
    return response.json()["articles"]

# Function to generate social media sharing links
def generate_sharing_links(url, title):
    encoded_url = quote(url)
    encoded_title = quote(title)
    facebook = f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}"
    twitter = f"https://twitter.com/intent/tweet?url={encoded_url}&text={encoded_title}"
    linkedin = f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}"
    instagram = f"https://www.instagram.com/?url={encoded_url}"
    return facebook, twitter, linkedin, instagram

# Create a dropdown to select the tab
selected_tab = st.selectbox("Select a tab:", ["Current Business News", "Wall Street Journal Articles"])

if selected_tab == "Current Business News":  # Fetch and display data for Business News tab
    st.header("Current Business News")

    # Fetch Business News data
    business_news_data = get_business_news_data()

    # Display the data in the Streamlit app with formatting
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>Business News</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("Here are the top headlines in business:")
    for article in business_news_data:
        st.write("## " + article["title"])
        if article.get("urlToImage"):
            st.image(article["urlToImage"], width=400)
        st.write(article["description"])
        st.write(f"Source: {article['source']['name']}  Published: {article['publishedAt']}")
        st.write(f"[Read more]({article['url']})")  # Display the source URL
        facebook, twitter, linkedin, instagram = generate_sharing_links(article['url'], article['title'])
        st.write(f"[Share on Facebook]({facebook}) | [Share on X]({twitter}) | [Share on LinkedIn]({linkedin}) | [Share on Instagram]({instagram})")
        st.write("---")

if selected_tab == "Wall Street Journal Articles":  # Fetch and display data for Wall Street Journal tab
    st.header("Wall Street Journal Articles")

    # Fetch Wall Street Journal Articles data
    wall_street_journal_data = get_wall_street_journal_data()

    # Display the data in the Streamlit app with formatting
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>WSJ Articles</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("Here are the top articles from WSJ:")
    for article in wall_street_journal_data:
        st.write("## " + article["title"])
        if article.get("urlToImage"):
            st.image(article["urlToImage"], width=400)
        st.write(article["description"])
        st.write(f"Source: {article['source']['name']}  Published: {article['publishedAt']}")
        st.write(f"[Read more]({article['url']})")  # Display the source URL
        facebook, twitter, linkedin, instagram = generate_sharing_links(article['url'], article['title'])
        st.write(f"[Share on Facebook]({facebook}) | [Share on X]({twitter}) | [Share on LinkedIn]({linkedin}) | [Share on Instagram]({instagram})")
        st.write("---")
