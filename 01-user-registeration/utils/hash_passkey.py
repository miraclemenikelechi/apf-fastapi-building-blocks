import bcrypt


async def hash_password_with_salt(passkey: str, rounds: int = 10) -> bytes:
    """
    A function that hashes a password with a provided salt using bcrypt.

    Parameters:
    passkey (str): The password to be hashed.
    rounds (int): The number of rounds for the hashing algorithm.

    Returns:
    bytes: The hashed password.
    """
    salt: bytes = bcrypt.gensalt(rounds)
    hashed_password: bytes = bcrypt.hashpw(passkey.encode(), salt)

    return hashed_password
