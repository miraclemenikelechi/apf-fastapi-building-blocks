import re

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, Field, validator


class User(BaseModel):
    username: str
    password: str = Field(
        description="the length of the password should not be less than 8 characters. it should contain a capital letter, small letterm symbols, and numbers.",
        min_length=8,
        max_length=64
    )
    email: EmailStr

    @validator("password")
    def validate_password(cls, value: str) -> str:
        """
        Validates the password value against a regex pattern to ensure it meets the expected criteria.

        Args:
            cls (class): The class object.
            value (str): The password value to be validated.

        Raises:
            HTTPException: If the password value does not meet the expected criteria.

        Returns:
            str: The validated password value.
        """
        regex_pattern: str = r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"

        if not re.match(regex_pattern, value):
            raise HTTPException(
                status_code=400,
                detail="password does not meet the expected criteria"
            )

        return value
    
    @validator("username")
    def validate_username(cls, value: str) -> str:
        """
        Validates the username value against a regex pattern to ensure it meets the expected criteria.

        Args:
            cls (class): The class object.
            value (str): The username value to be validated.

        Raises:
            HTTPException: If the username value does not meet the expected criteria.

        Returns:
            str: The validated username value.
        """
        regex_pattern: str = r"^[a-zA-Z0-9._-]{3,15}(?:$|_[0-9a-zA-Z]{0,15})"

        if not re.match(regex_pattern, value):
            raise HTTPException(
                status_code=400,
                detail="username does not meet the expected criteria"
            )

        return value
