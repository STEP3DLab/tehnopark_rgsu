from entry_pass_generator.app.pdf import render_pdf
from entry_pass_generator.app.models import EntryRequest


def test_render_pdf_bytes():
    data = EntryRequest(
        full_name="Иванов И.И.",
        vehicle_plate="A123BC77",
        start_date="2024-01-01",
        end_date="2024-01-02",
        purpose="test",
    )
    pdf = render_pdf(data)
    assert isinstance(pdf, (bytes, bytearray))
    assert len(pdf) > 0
