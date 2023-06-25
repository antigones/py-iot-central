from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class Telemetry:
    id: Optional[str] = field(metadata=config(field_name="@id"))
    type: list[str]=field(metadata=config(field_name="@type"))
    name:str

    comment: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    
