from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Device:
    id: str
    etag: str
    displayName: str
    simulated: bool
    provisioned: bool
    template: str
    enabled: bool
