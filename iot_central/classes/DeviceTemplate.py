from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from iot_central.classes.CapabilityModel import CapabilityModel

@dataclass_json
@dataclass
class DeviceTemplate:
    etag: str
    displayName: str
    capabilityModel: CapabilityModel
    id: str = field(metadata=config(field_name="@id"))
    type: list[str] = field(metadata=config(field_name="@type"))
    context: list[str] = field(metadata=config(field_name="@context"))

    def get_commands(self):
        commands = filter(lambda content: content.type == 'Command', self.capabilityModel.contents)
        return commands