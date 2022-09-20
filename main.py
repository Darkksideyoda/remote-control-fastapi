from fastapi import FastAPI, UploadFile, File
import shutil
import os
import time

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "remote-control-detection"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/calculate/{x}")
async def pow_calculate(x: int):
    return {"message": f"Pow Of the Given Number {x * x}"}


@app.post("/upload-remote-image")
async def upload_remote_image(file: UploadFile = File(...)):
    with open(f"{file.filename}", "wb") as buffer:
        print(os.stat(file.filename).st_size)
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}
