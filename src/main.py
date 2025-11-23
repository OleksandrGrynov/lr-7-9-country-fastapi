from fastapi import FastAPI
from src.external_api.router import router as external_router

app = FastAPI(title="Country API Integration Lab")

app.include_router(external_router)

@app.get("/")
def root():
    return {"message": "Country API lab is running"}
