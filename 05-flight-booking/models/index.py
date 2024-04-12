from datetime import date
from enum import Enum

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, Field, validator
from pydantic_extra_types.phone_numbers import PhoneNumber


class Gender(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class Title(str, Enum):
    mr = "Mr"
    mrs = "Mrs"
    miss = "Miss"


class ContactDetails(BaseModel):
    title: Title = None
    first_name: str = Field(min_length=3, max_length=12)
    last_name: str = Field(min_length=3, max_length=12)
    age: int = Field(gt=1, lt=150)
    email_address: EmailStr
    phone_number: PhoneNumber = Field(
        default=None,
        description="the phone number should be in the format +2349123456789",
        example="+2349123456789"
    )
    gender: Gender = None


class FlightDetails(BaseModel):
    coming_from: str = Field(
        default=None,
        description="the name of the city you are coming from",
        min_length=3,
        max_length=12,
    )
    going_to: str = Field(
        default=None,
        description="the name of the city you are going to",
        min_length=3,
        max_length=12,
    )
    flight_date: date = Field(
        default=None,
        description="the date of the flight (DD-MM-YYYY)",
        example="2012-12-12"
    )
    seat_preference: str

    @validator("flight_date")
    def validate_flight_date(cls, value):
        if (isinstance(value, str)):
            try:
                day, month, year = map(int, value.split("-"))
                return date(year, month, day)

            except ValueError:
                raise HTTPException(
                    status_code=400, detail="Incorrect data format, should be YYYY-MM-DD"
                )

        if value < date.today():
            raise HTTPException(
                status_code=400, detail="flight date cannot be in the past"
            )

        return value


class Booking(BaseModel):
    contact_details: ContactDetails
    flight_details: FlightDetails
