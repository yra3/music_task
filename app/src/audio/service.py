from uuid import UUID, uuid4

from fastapi import UploadFile
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.audio.constants import MP3_FOLDER, MP3_SUFFIX
from src.audio.exceptions import WrongFileType
from src.database import Audio, User
from src.utils import logger


def save_wav_as_mp3(wav_audio, path) -> None:
    try:
        AudioSegment.from_wav(wav_audio).export(path, format="mp3")
    except CouldntDecodeError:
        raise WrongFileType()


def get_audio_by_id(id: UUID, db: Session) -> Audio:
    audio = db.scalars(
        select(Audio).where(Audio.id == id).limit(1)
    ).first()
    return audio


def save_audio(audio: UploadFile, user: User, db: Session) -> Audio:
    audio_id = uuid4()
    filename = str(audio_id) + MP3_SUFFIX
    new_path = MP3_FOLDER / filename
    save_wav_as_mp3(audio.file, new_path)
    new_audio = Audio(
        id=audio_id,
        name=audio.filename,
        filepath=str(new_path),
        user=user
    )
    db.add(new_audio)
    db.commit()
    return new_audio
