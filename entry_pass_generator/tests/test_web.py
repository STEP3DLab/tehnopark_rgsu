from fastapi.testclient import TestClient
from entry_pass_generator.app.webhook import app

client = TestClient(app)

def test_generate_pdf_endpoint():
    response = client.post(
        "/generate",
        data={
            "full_name": "Иванов И.И.",
            "vehicle_plate": "A123BC77",
            "start_date": "2024-01-01",
            "end_date": "2024-01-02",
            "purpose": "test",
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/pdf")
    assert len(response.content) > 0
