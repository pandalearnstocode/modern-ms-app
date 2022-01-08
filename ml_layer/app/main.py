from fastapi import FastAPI, File, Body
from starlette.responses import Response, JSONResponse
import io
from app.segmentation import get_segmentator, get_segments
from app.ml_jobs import sample_job

model = get_segmentator()

app = FastAPI(
    title="DeepLabV3 image segmentation",
    description="""Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.1.0",
)


@app.post("/segmentation")
def get_segmentation_map(file: bytes = File(...)):
    """Get segmentation maps from image file"""
    segmented_image = get_segments(model, file)
    bytes_io = io.BytesIO()
    segmented_image.save(bytes_io, format="PNG")
    return Response(bytes_io.getvalue(), media_type="image/png")

@app.post("/ex1")
def run_task(data=Body(...)):
    delta = int(data["amount"])
    x = data["x"]
    y = data["y"]
    task = sample_job.delay(delta, x, y)
    return JSONResponse({"Result": task.get()})