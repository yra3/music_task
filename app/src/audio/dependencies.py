from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from src.audio import service
from src.auth.dependencies import valid_user_id
from src.auth.exceptions import UserNotOwner
from src.database import Audio, User
from src.dependencies import get_db
from src.exceptions import NotFound
from src.utils import logger


def valid_audio_id(id: UUID, db: Session = Depends(get_db)) -> Audio:
    audio = service.get_audio_by_id(id, db)
    if not audio:
        raise NotFound()

    return audio


def valid_owned_audio(
    audio: Audio = Depends(valid_audio_id),
    user: User = Depends(valid_user_id),
) -> Audio:
    if audio.user_id != user.id:
        raise UserNotOwner()

    return audio

