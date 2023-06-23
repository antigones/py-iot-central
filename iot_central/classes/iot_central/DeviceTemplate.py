from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from iot_central.classes.iot_central.CapabilityModel import CapabilityModel
from iot_central.classes.iot_central.CloudProperty import CloudProperty
from iot_central.classes.iot_central.Command import Command
from iot_central.classes.iot_central.Property import Property

@dataclass_json
@dataclass
class DeviceTemplate:
    etag: str
    displayName: str
    capabilityModel: CapabilityModel
    id: str = field(metadata=config(field_name="@id"))
    type: list[str] = field(metadata=config(field_name="@type"))
    context: list[str] = field(metadata=config(field_name="@context"))