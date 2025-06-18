import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

from .models import EntryRequest

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "0"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SECURITY_EMAIL = os.getenv("SECURITY_EMAIL")


def send_to_security(pdf: bytes, data: EntryRequest) -> None:
    """Send generated PDF to security via email."""
    msg = EmailMessage()
    msg["Subject"] = "Служебная записка на въезд"
    msg["From"] = SMTP_USER
    msg["To"] = SECURITY_EMAIL
    msg.set_content(
        f"Служебная записка для {data.full_name} во вложении.")
    msg.add_attachment(pdf, maintype="application", subtype="pdf",
                       filename="entry_pass.pdf")

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
