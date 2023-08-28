from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json

from iot_central.iotc_objects import Device, IOTCentralApiErrorDetail

@dataclass_json
@dataclass
class UpdatePropertyResponse:
    metadata: dict = field(metadata=config(field_name="$metadata"))

@dataclass_json
@dataclass
class SendCommandResponseValue:
    responseCode: int
    response: Optional[str] = None
    request: Optional[str] = None
    connectionTimeout: Optional[int] = None
    id: Optional[str] = None
    responseTimeout: Optional[int] = None
    
@dataclass_json
@dataclass
class SendCommandResponse:
    value: list[SendCommandResponseValue]

@dataclass_json
@dataclass
class ListDevicesResponse:
    value: list[Device]


@dataclass_json
@dataclass
class IOTCentralApiErrorResponse:
    error: IOTCentralApiErrorDetail


@dataclass_json
@dataclass
class GetTelemetryResponse:
    timestamp: str
    value: object