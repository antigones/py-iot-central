from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from iot_central.classes.iot_central.capability_model import CapabilityModel
from iot_central.classes.iot_central.cloud_property import CloudProperty
from iot_central.classes.iot_central.command import Command
from iot_central.classes.iot_central.property import Property

@dataclass_json
@dataclass
class DeviceTemplate:
    etag: str
    displayName: str
    capabilityModel: CapabilityModel
    id: str = field(metadata=config(field_name="@id"))
    type: list[str] = field(metadata=config(field_name="@type"))
    context: list[str] = field(metadata=config(field_name="@context"))