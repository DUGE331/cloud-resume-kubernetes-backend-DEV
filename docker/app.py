from fastapi import FastAPI
from fastapi.responses import JSONResponse
from core import increment_visitor  # <-- fixed

app = FastAPI()

@app.get("/dev-visitor")
def get_visitor():
    count = increment_visitor()
    return JSONResponse(content={"visitor_count": count}, headers={"Access-Control-Allow-Origin": "*"})