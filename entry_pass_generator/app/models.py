from datetime import date
from pydantic import BaseModel, ValidationError

class EntryRequest(BaseModel):
    """Schema of incoming entry request."""

    full_name: str
    vehicle_plate: str | None = None
    start_date: date
    end_date: date
    purpose: str


def validate_request(data: dict) -> EntryRequest:
    """Validate raw dict and return EntryRequest."""
    try:
        return EntryRequest(**data)
    except ValidationError as e:
        raise ValueError(e.errors())
