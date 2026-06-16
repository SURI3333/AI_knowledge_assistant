from passlib.hash import bcrypt

# ✅ simple in-memory user store (replace with DB later)
fake_users = {}


def register_user(email: str, password: str):
    """
    Registers a new user
    """

    if email in fake_users:
        raise Exception("User already exists")

    # ✅ truncate password for bcrypt
    safe_password = password[:72]

    hashed_password = bcrypt.hash(safe_password)

    fake_users[email] = hashed_password

    return {"msg": "User registered successfully"}


def login_user(email: str, password: str):
    """
    Authenticates user
    """

    if email not in fake_users:
        raise Exception("User not found")

    safe_password = password[:72]

    if not bcrypt.verify(safe_password, fake_users[email]):
        raise Exception("Invalid password")

    return {"msg": "Login successful"}