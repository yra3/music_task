from src.auth.constants import ErrorCode
from src.exceptions import BadRequest, NotAuthenticated, PermissionDenied


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class UserNotFound(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class UserNotOwner(PermissionDenied):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED
