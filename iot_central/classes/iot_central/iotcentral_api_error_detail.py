from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class IOTCentralApiErrorDetail:
    code: str
    message: str
    requestId: str
    time: str
