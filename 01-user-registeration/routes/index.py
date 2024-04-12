from controllers.index import create_new_user
from fastapi import APIRouter
from models.index import User

router = APIRouter()


@router.post("/register")
async def register_user(user: User):
    """
    Asynchronous function to register a new user.

    Parameters:
    - user: User (input): User object containing username, password, and email.

    Returns:
    - created_user: User (output): Newly created user object.
    """
    get_username = user.username
    get_password = user.password
    get_email = user.email

    created_user: User = await create_new_user(
        create_username=get_username,
        create_email=get_email,
        create_password=get_password
    )

    return created_user
