from dataclasses import dataclass
from dataclasses_json import dataclass_json

from iot_central.classes.iot_central.Device import Device



@dataclass_json
@dataclass
class ListDevicesResponse:
    value: list[Device]