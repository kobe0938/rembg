# main.py
from fastapi import FastAPI, File, UploadFile
from rembg import remove
from PIL import Image
import io
from starlette.responses import StreamingResponse

app = FastAPI()


@app.post("/remove")
async def remove_background(file: UploadFile = File(...)):
    contents = await file.read()
    input_image = Image.open(io.BytesIO(contents)).convert("RGBA")
    output_image = remove(input_image)
    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")
