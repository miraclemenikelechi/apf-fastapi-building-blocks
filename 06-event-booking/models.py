from datetime import date

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, Field, PositiveInt, validator
from enum import Enum


class EventType(Enum):
    concert = "concert"
    workshop = "workshop"
    conference = "conference"


class Attendee(BaseModel):
    name: str = Field(
        default="John Doe",
        min_length=2,
        description="the name of the attendee",
    )

    email: EmailStr = Field(
        default="U0WzA@example.com",
        description="the email address of the attendee",
    )

    age: PositiveInt = Field(
        ge=18,
        description="the age of the attendee",
    )


class Event(BaseModel):
    title: str = Field(
        min_length=3,
        description="the title of the event",
    )

    description: str = Field(
        min_length=3,
        description="the description of the event",
    )

    location: str = Field(
        min_length=3,
        description="the location of the event",
    )

    scheduled_date: date = Field(
        description="the date of the event (DD-MM-YYYY)",
    )

    @validator("scheduled_date")
    def scheduled_date_must_be_future(cls, value: date) -> date:
        if value < date.today():
            raise HTTPException(
                status_code=400,
                detail="Scheduled date must be in the future",
            )

        return value

    type: EventType


class EventBooking(BaseModel):
    attendee: Attendee
    event_details: Event
