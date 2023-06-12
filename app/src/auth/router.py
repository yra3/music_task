from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.auth import service
from src.dependencies import get_db
from src.auth.schemas import AuthUser

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=AuthUser)
def register_user(
    username: str,
    db: Session = Depends(get_db),
) -> AuthUser:
    user = service.create_user(username, db)
    return user
