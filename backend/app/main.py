from fastapi import FastAPI

app = FastAPI(title="PawCare AI API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "PawCare AI Backend"}
