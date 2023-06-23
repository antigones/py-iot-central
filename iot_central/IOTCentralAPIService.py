import datetime
import requests
from iot_central.classes.iot_central.Device import Device
from iot_central.classes.iot_central.DeviceTemplate import DeviceTemplate
from iot_central.classes.iot_central.ListDevicesResponse import ListDevicesResponse



class IOTCentralAPIService:

    def __init__(self, app_subdomain, auth_type, token, api_version="2022-07-31"):
        self.app_subdomain = app_subdomain
        self.auth_type = auth_type
        self.token = token
        self.api_version = api_version
        self.headers = self.build_headers()

    def build_headers(self):
        return {
            "Authorization":f"{self.auth_type} {self.token}"
        }
    
    def get_devices(self)->list[Device]:
        url = f"https://{self.app_subdomain}/api/devices?api-version={self.api_version}"
        response = requests.get(url, headers=self.headers)
        devices_res = ListDevicesResponse.from_json(response.text)
        return devices_res
    
    def get_template(self, device_template_id) -> DeviceTemplate:
        url = f"https://{self.app_subdomain}/api/deviceTemplates/{device_template_id}?api-version={self.api_version}"
        response = requests.get(url, headers=self.headers)
        device_template = DeviceTemplate.from_json(response.text)
        return device_template

    def send_command(self, device, command):
        payload = {
            "request": datetime.datetime.utcnow().isoformat()
        }

        url = f"https://{self.app_subdomain}/api/devices/{device}/commands/{command}?api-version={self.api_version}"
        response = requests.post(url, headers=self.headers, json=payload, verify=False)
        return response