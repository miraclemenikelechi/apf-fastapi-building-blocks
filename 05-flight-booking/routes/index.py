from fastapi import APIRouter
from models.index import Booking


router = APIRouter(prefix="/booking", tags=["booking"])


@router.post("/book")
async def to_book_a_flight(booking: Booking):
    return booking
