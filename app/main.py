from fastapi import FastAPI
from routers import letters

app = FastAPI()
app.include_router(letters.router)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", reload=True)