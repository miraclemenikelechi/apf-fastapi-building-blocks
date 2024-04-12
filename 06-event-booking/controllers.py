from models import EventBooking


async def create_an_event(event: EventBooking)  -> dict[str, any]:
    data_from_user: dict[str, any] = {
        "attendee": event.attendee,
        "event_details": event.event_details,
    }

    return data_from_user
