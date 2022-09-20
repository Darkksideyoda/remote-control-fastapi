from fastapi import FastAPI, UploadFile, File
import shutil
import os
import time
from RemoteControl_DL import find_remote


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "remote-control-detection"}


@app.post("/upload-remote-image")
async def upload_remote_image(file: UploadFile = File(...)):
    with open(f"{file.filename}", "wb") as buffer:
        print(os.stat(file.filename).st_size)
        shutil.copyfileobj(file.file, buffer)
    detected_result = find_remote(file.filename, 40)
    return {"result": f"{detected_result}"}

