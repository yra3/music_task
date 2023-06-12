import bcrypt


def hash_password(password: str) -> str:
    pw = password.encode('utf8')  # bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt).decode('utf8')


def check_password(password: str, password_in_db: bytes) -> bool:
    password_bytes = password.encode('utf8')  # bytes(password, "utf-8")
    return bcrypt.checkpw(password_bytes, password_in_db)
