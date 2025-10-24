from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from styler import KNNImageStyler
from PIL import Image
import io
import os

app = FastAPI(title="KNN Image Styler")

# Setup folders
os.makedirs("outputs", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount static templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/style", response_class=HTMLResponse)
async def style_image(
    request: Request,
    file: UploadFile = File(...),
    cluster_min: int = Form(2),
    cluster_max: int = Form(8)
):
    # Ensure cluster count doesn’t exceed 20
    if cluster_max > 20:
        cluster_max = 20

    # Ensure logical range
    if cluster_min > cluster_max:
        cluster_min = max(2, cluster_max - 1)

    # Read uploaded image
    img_bytes = await file.read()
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    # Initialize styler
    styler = KNNImageStyler(cluster_range=(cluster_min, cluster_max))

    # Generate styled images
    styles = styler.generate_styles(image)
    
    # Save results
    output_files = []
    for k, styled in styles.items():
        path = f"outputs/styled_{k}.jpg"
        styled.save(path)
        output_files.append(path)
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "styled_images": output_files,
            "cluster_min": cluster_min,
            "cluster_max": cluster_max,
        }
    )


# Serve outputs
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")

