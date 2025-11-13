from fastapi import FastAPI
from banco import cursos


app = FastAPI()


if __name__ == "__main__":
    app.run()
    # import uvicorn

    # uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)