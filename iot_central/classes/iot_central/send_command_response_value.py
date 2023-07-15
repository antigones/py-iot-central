from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json



@dataclass_json
@dataclass
class SendCommandResponseValue:
    responseCode: int
    response: str
    request: Optional[str] = None
    connectionTimeout: Optional[int] = None
    id: Optional[str] = None
    responseTimeout: Optional[int] = None