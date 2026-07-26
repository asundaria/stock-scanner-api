from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock API is running! Go to /data to see stocks."}

@app.get("/data")
def get_stock_data():
    url = "https://scanx.trade/stock-screener/intraday-alpha-scannner-384541?utm_source=youtube&utm_medium=ScanX&utm_id=Himanshu"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    # यह कोड वेबसाइट से टेबल का डेटा निकालने की कोशिश करेगा
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # अभी के लिए हम एक टेस्टिंग डेटा भेज रहे हैं ताकि सर्वर चेक हो सके
    return {
        "status": "success",
        "message": "Data will appear here shortly once we finalize the table structure!"
    }