import config
import streamlit as st
import plotly as pl
import requests as r
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import django as dj
import pandas as web
import datetime as dt
import mplfinance as mpf
import plotly.graph_objects as go
import js2py
from django.db import models
import os
import time

# Function to get stock quotes
@st.cache(ttl=10)  # Cache the data for 10 seconds
def get_stock_quotes(tickers):
    stock_data = yf.download(tickers, period="1d", interval="1m")
    latest_quotes = stock_data['Close'].iloc[-1]
    previous_quotes = stock_data['Close'].iloc[-2]
    return latest_quotes, previous_quotes

# Add a sidebar for user input
tickers = st.sidebar.text_input("Enter stock tickers (comma-separated)")

if tickers:
    tickers = tickers.split(',')
    tickers = [ticker.strip().upper() for ticker in tickers]
    
    # Display scrolling banner with updated styling
    st.markdown("""
    <style>
    .scrolling-banner {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        animation: scroll-left 20s linear infinite;
        font-family: 'Arial', sans-serif;
        font-size: 20px;
    }
    @keyframes scroll-left {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    .up {
        color: green;
    }
    .down {
        color: red;
    }
    </style>
    """, unsafe_allow_html=True)
    
    latest_quotes, previous_quotes = get_stock_quotes(tickers)
    
    banner = ""
    for ticker in tickers:
        if ticker in latest_quotes.index:
            latest_price = latest_quotes[ticker]
            previous_price = previous_quotes[ticker]
            if latest_price > previous_price:
                indicator = "▲"
                style_class = "up"
            else:
                indicator = "▼"
                style_class = "down"
            banner += f"<span class='{style_class}' style='margin-right: 50px;'>{ticker}: ${latest_price:.2f} {indicator}</span>"
    
    st.markdown(f"<div class='scrolling-banner'>{banner}</div>", unsafe_allow_html=True)
    
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("Violet and Light Green Modern Gradient Financial Consultant Finance Animated Logo.png")

with col3:
    st.write(' ')
    
#st.markdown("<h1 style='text-align: center;'>The VIX is a key trading indicator that reflects the market's expectations for volatility in the next 30 days, based on S&P 500 index options. A higher VIX signals increased market uncertainty and potential turbulence, while a lower VIX suggests a more stable and calm market environment. Monitoring VIX levels and trends can be crucial for shaping effective trading strategies.</h1>", unsafe_allow_html=True)

# Add divider line
st.markdown("---")

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>", unsafe_allow_html=True)

# List available page files
page_files = os.listdir("Pages")
page_files = [file for file in page_files if file.endswith(".py")]

# Add a menu item to select pages
selected_pages = st.multiselect("Select Trade Cipher Features", page_files)

# Execute the selected pages
for selected_page in selected_pages:
    exec(open(f"Pages/{selected_page}").read())

st.markdown("""
<a target="_blank" href="https://shareasale.com/r.cfm?b=1517949&amp;u=3574798&amp;m=57542&amp;urllink=&amp;afftrack="><img src="https://static.shareasale.com/image/57542/generic-728x90-green_00.jpg" border="0" alt="Buy Gold and Silver" /></a>
""", unsafe_allow_html=True)

# Add divider line
st.markdown("---")

st.sidebar.header("Trade Cipher Tools")

import streamlit as st
import plotly.graph_objects as go

# Define a header for the app
st.header("Stock/Crypto Watchlist")

# Create an empty list to store the watchlist
watchlist = []

# Define a function to add symbols to the watchlist
def add_to_watchlist(symbol):
    watchlist.append(symbol.upper())
    return "{symbol.upper()} added to watchlist."

# Use a form to collect input from users
with st.form("Add Symbol"):
    st.write("Enter a stock or crypto symbol to add to your watchlist:")
    new_symbol = st.text_input("Symbol")
    add_button = st.form_submit_button("Add")

# Add new symbols to the watchlist
if new_symbol and add_button:
    result = add_to_watchlist(new_symbol)
    st.success(result)

# Display the current watchlist
if watchlist:
    st.header("My Watchlist")

    # Use icons to represent different symbols
    for symbol in watchlist:
        if "BTC" in symbol:
            st.image("btc.png", width=30)
        elif "ETH" in symbol:
            st.image("eth.png", width=30)
        else:
            st.write(symbol)

    # Use data visualization to provide insights about the watchlist
    fig = go.Figure()
    for symbol in watchlist:
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name=symbol.upper()))

    fig.update_layout(title="Price Trend")
    st.plotly_chart(fig)
else:
    st.warning("Your watchlist is empty.")



# Add custom CSS to style the app
st.markdown(
    """
    <style>
    body {
        font-family: Arial, Helvetica, sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.text("Watch Bloomberg Video 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=DxmDPrfinXY')

# Add divider line
st.markdown("---")

st.sidebar.text("Watch CNBC Live 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=9NyxcX3rhQs')

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)

import streamlit as st

st.title('Welcome to Trade Cipher!')

from PIL import Image

image = Image.open('S&P500.png')

st.image(image , use_column_width = True)

st.markdown("""Our trading app makes it simple to help traders and investors make the right choices when trading various trading instruments!"""
    """ You can view historical market data, View investment indicators, and place trades using your preferred trading platform and much more!
    """)

import streamlit as st

# Placeholder for the product showcase
product_showcase = st.empty()

# Load the ShareASale widget script
st.markdown("""
    <script type="text/javascript" src="https://showcase.shareasale.com/shareASale_liveWidget_loader.js?dt=06072023043517"></script>
    <script type="text/javascript">shrsl_ShareASale_liveWid_Init(50615, 3574798, 'shrsl_ShareASale_liveWid_wideSkyScraper_populate');</script>
    """, unsafe_allow_html=True)

# Display the product showcase
product_showcase.markdown('<div class="shrsl_ShareASale_productShowCaseTarget_50615"></div>', unsafe_allow_html=True)

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=1207190.332&subid=0&type=4"><IMG border="0"   alt="Newegg" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=1207190.332&subid=0&type=4&gridnum=1"></a>
""", unsafe_allow_html=True)
