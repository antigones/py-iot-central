from enum import Enum

class AuthType(Enum):
    BEARER = 'Bearer'
    SAS_TOKEN = 'SharedAccessSignature'