from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="FastAPI App"
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
