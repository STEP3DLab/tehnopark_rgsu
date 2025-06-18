from entry_pass_generator.app.models import validate_request, EntryRequest
import pytest
from datetime import date

def test_validate_request_success():
    data = {
        "full_name": "Иванов И.И.",
        "vehicle_plate": "A123BC77",
        "start_date": "2024-01-01",
        "end_date": "2024-01-02",
        "purpose": "test"
    }
    req = validate_request(data)
    assert isinstance(req, EntryRequest)
    assert req.full_name == "Иванов И.И."


def test_validate_request_fail():
    with pytest.raises(ValueError):
        validate_request({"full_name": "", "start_date": "not-a-date"})
