from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock API is running successfully!"}

@app.get("/data")
def get_stock_data():
    # ScanX / Intraday Stock Data Response Format
    return [
        {
            "symbol": "TATASTEEL",
            "name": "Tata Steel Ltd",
            "price": 168.20,
            "changePercent": 3.4,
            "volumeSurge": 2.8,
            "ema20": 164.0,
            "supertrend": "BULLISH",
            "rsi": 68.5,
            "alphaScore": 95,
            "breakoutType": "Intraday Alpha"
        },
        {
            "symbol": "RELIANCE",
            "name": "Reliance Industries Ltd",
            "price": 2980.50,
            "changePercent": 2.1,
            "volumeSurge": 2.4,
            "ema20": 2920.0,
            "supertrend": "BULLISH",
            "rsi": 66.2,
            "alphaScore": 91,
            "breakoutType": "20 EMA Breakout"
        }
    ]
