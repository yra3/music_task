from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from src.auth import service
from src.auth.exceptions import UserNotFound
from src.database import User
from src.dependencies import get_db
from src.utils import logger


def valid_user_id(user: int, db: Session = Depends(get_db)) -> User:
    user = service.get_user_by_id(user, db)
    if not user:
        raise UserNotFound()

    return user


def valid_auth_data(
    token: UUID,
    user: User = Depends(valid_user_id),
) -> User:
    user = service.authenticate_user(user, token)
    return user
