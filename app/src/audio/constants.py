from src.config import settings

MP3_FOLDER = settings.BASE_DIR / 'mp3'
MP3_SUFFIX = '.mp3'


class ErrorCode:
    AUDIO_NOT_FOUND = "Audio not found. Wrong audio_id"
    WRONG_FILE_TYPE = "Uploaded file has wrong type."
