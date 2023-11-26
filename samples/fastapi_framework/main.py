import uvicorn
from fastapi import FastAPI
from config import START_PORT

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is FastAPI Project!"}


if __name__ == "__main__":
    uvicorn.run(app,  host='0.0.0.0', port=START_PORT)
