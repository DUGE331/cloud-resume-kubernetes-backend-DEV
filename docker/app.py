from fastapi import FastAPI
from fastapi.responses import JSONResponse
from core import increment_visitor  # your visitor increment function

app = FastAPI()

# Friendly root route
@app.get("/")
def root():
    return {"message": "Visitor Counter API is running. Use /dev-visitor to get the count."}

# Visitor counter route
@app.get("/dev-visitor")
def get_visitor():
    count = increment_visitor()  # increments the counter
    return JSONResponse(content={"visitor_count": count}, headers={"Access-Control-Allow-Origin": "*"})