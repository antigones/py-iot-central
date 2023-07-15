import datetime
import requests

from iot_central.classes.auth_type import AuthType

from iot_central.classes.iot_central.device import Device
from iot_central.classes.iot_central.device_template import DeviceTemplate
from iot_central.classes.iot_central.iot_central_error import IOTCentralError
from iot_central.classes.iot_central.iotcentral_api_error_response import IOTCentralApiErrorResponse
from iot_central.classes.iot_central.list_devices_response import ListDevicesResponse
from iot_central.classes.iot_central.send_command_response import SendCommandResponse



class IOTCentralAPIService:

    def __init__(self, app_subdomain:str, auth_type:AuthType, token:str, api_version="2022-07-31"):
        self.app_subdomain = app_subdomain
        self.auth_type = auth_type
        self.token = token
        self.api_version = api_version
        self.headers = self.build_headers(auth_type=self.auth_type)

    def build_headers(self, auth_type: AuthType) -> dict:
        match auth_type:
            case AuthType.SAS_TOKEN:
                return {
                    "Authorization":f"{self.token}"
                }
            case AuthType.BEARER:
                return {
                    "Bearer":f"{self.token}"
                }

    def get_devices(self) -> list[Device] | IOTCentralApiErrorResponse:

        url = f"https://{self.app_subdomain}/api/devices?api-version={self.api_version}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            res = ListDevicesResponse.from_json(response.text)
        else:
            res = IOTCentralApiErrorResponse.from_json(response.text)
        return res

    def get_template(self, device_template_id) -> DeviceTemplate | IOTCentralApiErrorResponse:

        url = f"https://{self.app_subdomain}/api/deviceTemplates/{device_template_id}?api-version={self.api_version}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            res = DeviceTemplate.from_json(response.text)
        else:
            res = IOTCentralApiErrorResponse.from_json(response.text)
        return res


    def update_property(self, device, payload: str) -> requests.Response:

        url = f"https://{self.app_subdomain}/api/devices/{device}/properties?api-version={self.api_version}"
        response = requests.patch(url, headers=self.headers, json=payload)
        return response


    def send_command(self, device, command, payload={}) -> SendCommandResponse | IOTCentralApiErrorResponse :

        url = f"https://{self.app_subdomain}/api/devices/{device}/commands/{command}?api-version={self.api_version}"
        response = requests.post(url, headers=self.headers, json=payload, verify=False)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            res = SendCommandResponse.from_json(response.text)
        else:
            res = IOTCentralApiErrorResponse.from_json(response.text)
        return res