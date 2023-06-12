from src.audio.constants import ErrorCode
from src.exceptions import BadRequest, NotFound


class WrongFileType(BadRequest):
    DETAIL = ErrorCode.WRONG_FILE_TYPE


class AudioNotFound(NotFound):
    DETAIL = ErrorCode.AUDIO_NOT_FOUND

