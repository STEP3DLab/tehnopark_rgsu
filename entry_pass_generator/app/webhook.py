from pathlib import Path
import io

from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import FileResponse, StreamingResponse, HTMLResponse

from .models import validate_request, EntryRequest
from .pdf import render_pdf
from .mail import send_to_security

app = FastAPI()

TEMPLATE_DIR = Path(__file__).parent / "templates"
INDEX_HTML = TEMPLATE_DIR / "index.html"
START_HTML = TEMPLATE_DIR / "start.html"

@app.post("/webhook")
def webhook(data: dict):
    try:
        entry_request: EntryRequest = validate_request(data)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    pdf_bytes = render_pdf(entry_request)
    send_to_security(pdf_bytes, entry_request)
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def index():
    """Serve simple HTML form for data input."""
    return FileResponse(INDEX_HTML)


@app.get("/start", response_class=HTMLResponse)
def start_page():
    """Landing page with start button and simple 3D animation."""
    return FileResponse(START_HTML)


@app.post("/generate")
def generate(
    full_name: str = Form(...),
    vehicle_plate: str | None = Form(None),
    start_date: str = Form(...),
    end_date: str = Form(...),
    purpose: str = Form(...),
):
    data_dict = {
        "full_name": full_name,
        "vehicle_plate": vehicle_plate,
        "start_date": start_date,
        "end_date": end_date,
        "purpose": purpose,
    }
    try:
        entry_request: EntryRequest = validate_request(data_dict)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    pdf_bytes = render_pdf(entry_request)
    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=entry_pass.pdf"},
    )
