from fastapi import FastAPI, HTTPException

from .models import validate_request, EntryRequest
from .pdf import render_pdf
from .mail import send_to_security

app = FastAPI()

@app.post("/webhook")
def webhook(data: dict):
    try:
        entry_request: EntryRequest = validate_request(data)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    pdf_bytes = render_pdf(entry_request)
    send_to_security(pdf_bytes, entry_request)
    return {"status": "ok"}
