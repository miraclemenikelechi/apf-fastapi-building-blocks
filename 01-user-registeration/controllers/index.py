import bcrypt
from models.index import User
# from utils.hash_passkey import hash_password_with_salt


async def create_new_user(create_username: str, create_email: str, create_password: str) -> User:
    """
    Create a new user with the given username, email, and password.

    Args:
        create_username (str): The username of the new user.
        create_email (str): The email of the new user.
        create_password (str): The password of the new user.

    Returns:
        User
    """
    # hashed_password: bytes = await hash_password_with_salt(passkey=create_password, rounds=12)

    new_user: User = User(
        username=create_username,
        email=create_email,
        
        password=bcrypt.hashpw(
            create_password.encode(),
            bcrypt.gensalt(rounds=12)
        )
    )

    return new_user


# async def hash_password_with_salt(passkey: str, rounds: int = 10) -> bytes:
#     """
#     A function that hashes a password with a provided salt using bcrypt.

#     Parameters:
#     passkey (str): The password to be hashed.
#     rounds (int): The number of rounds for the hashing algorithm.

#     Returns:
#     bytes: The hashed password.
#     """
#     salt: bytes = bcrypt.gensalt(rounds)
#     hashed_password: bytes = bcrypt.hashpw(passkey.encode(), salt)

#     return hashed_password
