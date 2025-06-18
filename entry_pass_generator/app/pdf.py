from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from .models import EntryRequest

TEMPLATE_DIR = Path(__file__).parent / "templates"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def render_pdf(data: EntryRequest) -> bytes:
    """Render PDF bytes from EntryRequest."""
    template = env.get_template("sz_template.html")
    html_content = template.render(**data.model_dump())
    pdf = HTML(string=html_content).write_pdf()
    return pdf
