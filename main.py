import uvicorn
from fastapi import FastAPI
import password_generator

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/generate_pass")
def generate_password_endpoint():
    return {"password": password_generator.generate_password()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
