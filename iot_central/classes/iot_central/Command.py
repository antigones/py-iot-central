from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class Command:
    id: Optional[str] = field(metadata=config(field_name="@id"))
    type: str=field(metadata=config(field_name="@type"))
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    commandType: Optional[str] = None
    comment: Optional[str] = None