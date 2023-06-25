from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json

from iot_central.classes.iot_central.cloud_property import CloudProperty
from iot_central.classes.iot_central.command import Command
from iot_central.classes.iot_central.property import Property
from iot_central.classes.iot_central.telemetry import Telemetry


@dataclass_json
@dataclass
class CapabilityModel:
    type: str = field(metadata=config(field_name="@type"))
    id: str = field(metadata=config(field_name="@id"))
    contents: list[Command | Telemetry | Property | CloudProperty] # this should be an union Command | Telemetry
    displayName: str
    description: Optional[str] = None

    def __post_init__(self):
        # this is a trick because dataclass_json is unable to deserialize list of union types
        tmp = list()
        item = None
        for content in self.contents:
            if isinstance(content['@type'], str):
                if content['@type'] == 'Command':
                    item = Command.from_dict(content)
                if content['@type'] == 'Property':
                    item = Property.from_dict(content)
            if isinstance(content['@type'],list):
                if 'Telemetry' in content['@type']:
                    item = Telemetry.from_dict(content)
                if 'Cloud' in content['@type']:
                    item = CloudProperty.from_dict(content)
                if 'Property' in content['@type']:
                    item = Property.from_dict(content)
            tmp.append(item)
        self.contents = tmp
