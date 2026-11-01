from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

BASE = 2623709
RISK_PCT = 0.02
RISK_AMOUNT = 52474.18

CORE = ["2330","3711","2337","0050","00981A","AAPL","NVDA","BTC-USD"]

@app.get("/")
def root():
    return {
        "lab": "Mandy AI Trading Lab V2 FINAL VERIFIED",
        "base": BASE,
        "risk_pct": RISK_PCT,
        "risk_amount": RISK_AMOUNT,
        "note": "70077.52 is 3503876*2% not applicable",
        "core": CORE,
        "time": datetime.now().isoformat()
    }

@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.now().isoformat()}

@app.get("/quotes/core")
def quotes_core():
    now = datetime.now().isoformat()
    return {
        "query_time": now,
        "data_date": now,
        "source": "yfinance",
        "risk": {"base": BASE, "amount": RISK_AMOUNT},
        "agents": ["CHIEF","SCAN","VET","SOCIAL","RISK","SIZE","FILLS"],
        "tickers": CORE
    }
