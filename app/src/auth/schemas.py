from uuid import UUID

from pydantic import BaseModel


class AuthUser(BaseModel):
    user_id: int
    token: UUID
