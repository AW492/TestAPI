from fastapi import FastAPI
from fastapi.responses import JSONResponse

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
