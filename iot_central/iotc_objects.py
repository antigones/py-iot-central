from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json


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

@dataclass_json
@dataclass
class CloudProperty:
    id: Optional[str] = field(metadata=config(field_name="@id"))
    type: str = field(metadata=config(field_name="@type"))
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    schema: Optional[str] = None

@dataclass_json
@dataclass
class Property:
    id: Optional[str] = field(metadata=config(field_name="@id"))
    type: str=field(metadata=config(field_name="@type"))
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    schema: Optional[str] = None
    color: Optional[str] = None

@dataclass_json
@dataclass
class Telemetry:
    id: Optional[str] = field(metadata=config(field_name="@id"))
    type: list[str]=field(metadata=config(field_name="@type"))
    name:str

    comment: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None

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


@dataclass_json
@dataclass
class DeviceTemplate:
    etag: str
    displayName: str
    capabilityModel: CapabilityModel
    id: str = field(metadata=config(field_name="@id"))
    type: list[str] = field(metadata=config(field_name="@type"))
    context: list[str] = field(metadata=config(field_name="@context"))

@dataclass_json
@dataclass
class IOTCentralApiErrorDetail:
    code: str
    message: str
    requestId: str
    time: str