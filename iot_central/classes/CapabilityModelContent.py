from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class CapabilityModelContent:
    id: str = field(metadata=config(field_name="@id"))
    type: list[str] | str=field(metadata=config(field_name="@type"))
    name:str
    description:Optional[str] = None
    displayName:Optional[str] = None
    schema:Optional[str] = None
    commandType:Optional[str] = None
    writeable:Optional[bool] = None
    decimalPlaces:Optional[int] = None
    displayUnit:Optional[str] = None
    maxValue:Optional[int] = None
    minValue:Optional[int] = None