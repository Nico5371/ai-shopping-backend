from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, AI Shopping!"}

@app.get("/api/ai-recommendations")
def get_recommendations():
    return {"products": ["Product 1", "Product 2", "Product 3"]}
  
