import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Google Stock Price App

This app show the stock **closing price** and **volume** of Google!

""")
    

# https://torwardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# define the ticker symbol
tickerSymbol = "GOOGL"

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period="1d", start="2010-12-31", end="2023-12-31")

#  Open   High   Low Close   Volume   Dividends   Stock Splits


st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)