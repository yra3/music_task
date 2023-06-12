from uuid import UUID, uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.auth.exceptions import InvalidCredentials
from src.auth.schemas import AuthUser
from src.auth.security import check_password, hash_password
from src.database import User


def create_user(username: str, db: Session) -> AuthUser:
    token = uuid4()
    new_user = User(
        username=username,
        token=hash_password(str(token)),
    )
    db.add(new_user)
    db.commit()
    return AuthUser(user_id=new_user.id, token=token)


def get_user_by_id(user_id: int, db: Session) -> User:
    user = db.scalars(
        select(User).where(User.id == user_id).limit(1)
    ).first()
    return user


def authenticate_user(user: User, token: UUID) -> User:
    if not check_password(str(token), user.token.encode('utf-8')):
        raise InvalidCredentials()

    return user
