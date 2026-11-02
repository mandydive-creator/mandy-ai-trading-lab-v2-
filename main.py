from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

BASE = 3576420
RISK_PCT = 0.02
HOLDINGS = {
    "2330": 40,
    "3711": 100,
    "2337": 5700,
    "0050": 1000,
    "00981A": 15000,
    "AAPL": 10,
    "NVDA": 10,
    "BTC-USD": 1
}
RISK_AMOUNT = BASE * RISK_PCT
CURRENT_MKT = 3503876

CORE = ["2330","3711","2337","0050","00981A","AAPL","NVDA","BTC-USD"]

@app.get("/")
def root():
    return {
        "lab": "Mandy AI Trading Lab V2 AUTO",
        "base": BASE,
        "risk_pct": RISK_PCT,
        "risk_amount": RISK_AMOUNT,
        "holdings": HOLDINGS,
        "note": f"current {CURRENT_MKT}*2%={CURRENT_MKT*0.02}",
        "core": CORE,
        "time": datetime.now().isoformat()
    }

@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.now().isoformat()}
