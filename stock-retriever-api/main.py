from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import redis
import uvicorn

redis_client = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/stock/")
async def root(symbol: str):
    print("receive symbol", symbol)
    price = redis_client.get(symbol)
    return price

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")