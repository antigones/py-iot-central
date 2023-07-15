from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

from iot_central.classes.iot_central.send_command_response_value import SendCommandResponseValue



@dataclass_json
@dataclass
class SendCommandResponse:
    value: list[SendCommandResponseValue]