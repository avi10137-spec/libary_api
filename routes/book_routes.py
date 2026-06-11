from  fastapi import FastAPI
import  uvicorn

app=FastAPI()

@app.post("/books")
def create_book():
    pass