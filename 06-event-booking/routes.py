from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import EventBooking
from controllers import create_an_event

events = APIRouter(prefix="/events", tags=["event"])


@events.post("/", response_model=EventBooking)
async def book_an_event(event: EventBooking):

    data = await create_an_event(event)

    json_compatible_data: dict[str, any] = {
        "message": "event created",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(
        status_code=201,
        content=json_compatible_data,
    )
