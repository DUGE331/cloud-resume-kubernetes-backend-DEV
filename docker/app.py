from fastapi import FastAPI
from fastapi.responses import JSONResponse
from core import increment_visitor  # <-- fixed

app = FastAPI()

# Existing visitor route
@app.get("/dev-visitor")
def get_visitor():
    count = increment_visitor()
    return JSONResponse(content={"visitor_count": count}, headers={"Access-Control-Allow-Origin": "*"})

# Friendly root route
@app.get("/")
def root():
    return {"message": "Visitor Counter API is running. Use /dev-visitor to get the count."}