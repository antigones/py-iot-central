from dataclasses import dataclass, field
from typing import Optional, Union
from dataclasses_json import config, dataclass_json

from iot_central.classes.CapabilityModelContent import CapabilityModelContent
from iot_central.classes.Command import Command
from iot_central.classes.Telemetry import Telemetry


@dataclass_json
@dataclass
class CapabilityModel:
    type: str = field(metadata=config(field_name="@type"))
    id: str = field(metadata=config(field_name="@id"))

    contents:list[CapabilityModelContent] # this should be an union Command | Telemetry
    displayName:str
    description:Optional[str] = None
