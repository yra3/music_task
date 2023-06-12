from fastapi import APIRouter, UploadFile, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from src.audio import service
from src.audio.dependencies import valid_owned_audio
from src.auth.dependencies import valid_auth_data
from src.config import settings
from src.database import User, Audio
from src.dependencies import get_db
from src.utils import logger

router = APIRouter()


@router.post("/record")
def create_upload_file(
    audio: UploadFile,
    user: User = Depends(valid_auth_data),
    db: Session = Depends(get_db),
):
    audio = service.save_audio(audio, user, db)
    audio_url = f'http://{settings.SITE_DOMAIN}:{settings.SITE_PORT}/record?id={audio.id}&user={user.id}'
    return {"audio_url": audio_url}


@router.get("/record")
def download_file(
    audio: Audio = Depends(valid_owned_audio),
) -> FileResponse:
    new_filename = audio.name + '.mp3'
    return FileResponse(path=audio.filepath, filename=new_filename, media_type='audio/mpeg')
