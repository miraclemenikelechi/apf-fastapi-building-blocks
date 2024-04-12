import re
from datetime import date

from pydantic import BaseModel, Field, PositiveFloat, validator
from fastapi import HTTPException


class PaymentRequest(BaseModel):
    amount: PositiveFloat = Field(
        ge=0,
        description="payment amount",
    )

    currency: str = Field(
        description="Currency code in ISO 4217 format (e.g., USD, EUR, GBP)",
        pattern=r"^[A-Z]{3}$",  # Regex pattern for currency validation
    )

    @validator("currency")
    def check_currency(cls, value: str) -> str:
        # Validate currency code against a list of supported currencies
        supported_currencies = ["NGN", "USD", "EUR", "GBP", "JPY", "CAD"]
        if value not in supported_currencies:
            raise HTTPException(
                status_code=400,
                detail="Unsupported currency",
            )
        return value

    card_number: str = Field(
        min_length=16,
        max_length=16,
        description="card number",
    )

    @validator("card_number")
    def validate_card_number(cls, value: str) -> str:
        # Define a dictionary mapping card prefixes to validation patterns
        card_patterns: dict[str, str] = {
            "4": r"^4[0-9]{12}(?:[0-9]{3})?$",  # Visa
            "5[1-5]": r"^5[1-5][0-9]{14}$",  # Mastercard
            "3[47]": r"^3[47][0-9]{13}$",  # American Express
            "6(?:011|5[0-9]{2})": r"^6(?:011|5[0-9]{2})[0-9]{12}$",  # Discover
        }

        # Iterate through the patterns and perform validation
        for prefix, pattern in card_patterns.items():
            if value.startswith(prefix) and re.match(pattern, value):
                return value  # Valid card number under this pattern

        raise HTTPException(
            status_code=400,
            detail="Invalid card number",
        )  # Raise an exception for invalid numbers

    expiration_date: str = Field(
        min_length=5,
        max_length=5,
        description="Expiration date in MM/YY format",
        pattern=r"^(0[1-9]|1[0-2])\/?([0-9]{2})$",
        examples=["12/24"],
    )

    @validator("expiration_date")
    def check_if_card_is_expired(cls, value: str) -> str:
        # Parse the expiration date string to extract MM and YY parts
        mm, yy = value.split("/")
        expiration_date = date(
            int(f"20{yy}"), int(mm), 1
        )  # Assuming expiration date is first day of the month

        # Compare expiration date with current date
        if expiration_date < date.today():
            raise HTTPException(
                status_code=400,
                detail="Card has expired",
            )

        return value  # Return the validated expiration date

    cvv: str = Field(
        min_length=3,
        max_length=4,
        description="CVV code",
        examples=["123"],
    )

    @validator("cvv")
    def validate_cvv(cls, value: str) -> str:
        if not value.isdigit() or len(value) not in (3, 4):
            raise HTTPException(
                status_code=400,
                detail="Invalid CVV code",
            )
        return value  # Return the validated CVV code
