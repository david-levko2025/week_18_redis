import uvicorn
from fastapi import FastAPI

from routes import route as order_route

app = FastAPI(debug=True)

app.include_router(order_route)


if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost",port=8000,reload=True)