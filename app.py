from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running on Render!"}

@app.get("/ping")
def ping():
    return {"status": "pong"}

# Optional: Custom error handling
@app.get("/error")
def error_test():
    return JSONResponse(status_code=400, content={"error": "Test error"})

# Data model for POST
class Item(BaseModel):
    name: str
    value: int

# POST test
@app.post("/submit")
def submit_data(item: Item):
    return {"received_name": item.name, "received_value": item.value}
