from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import config, dataclass_json

from iot_central.classes.iot_central.iotcentral_api_error_detail import IOTCentralApiErrorDetail


@dataclass_json
@dataclass
class IOTCentralApiErrorResponse:
    error: IOTCentralApiErrorDetail
