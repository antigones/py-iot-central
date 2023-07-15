from iot_central.classes.iot_central.iot_central_error import IOTCentralError
from iot_central.classes.iot_central.iotcentral_api_error_response import IOTCentralApiErrorResponse
from iot_central.device import Device

from iot_central.classes.iot_central.cloud_property import CloudProperty
from iot_central.classes.iot_central.command import Command
from iot_central.classes.iot_central.property import Property
from iot_central.classes.iot_central.telemetry import Telemetry
from iot_central.iotcentral_api_service import IOTCentralAPIService

class IOTCentral:

    def __init__(self, app_subdomain, auth_type, token, api_version="2022-07-31"):
        self.app_subdomain = app_subdomain
        self.auth_type = auth_type
        self.token = token
        self.api_version = api_version
        self.IOTCentralAPIService = IOTCentralAPIService(
            app_subdomain=self.app_subdomain, 
            auth_type=self.auth_type,
            token=self.token,
            api_version=self.api_version)
    
    def get_devices(self) -> list[Device]:
        complete_devices = list()
        devices = self.IOTCentralAPIService.get_devices()
        if isinstance(devices, IOTCentralApiErrorResponse):
            raise IOTCentralError()
        for device in devices.value:
            device_template = self.IOTCentralAPIService.get_template(device.template)
            if isinstance(device_template, IOTCentralApiErrorResponse):
                raise IOTCentralError()
            complete_device = Device(
                name=device.id, 
                display_name=device.displayName,
                commands=self._filter_objects_by_type(Command, device_template.capabilityModel.contents),
                telemetries=self._filter_objects_by_type(Telemetry, device_template.capabilityModel.contents),
                cloud_properties=self._filter_objects_by_type(CloudProperty, device_template.capabilityModel.contents),
                properties=self._filter_objects_by_type(Property, device_template.capabilityModel.contents))
            complete_devices.append(complete_device)
        return complete_devices

    

    def send_command(self, device, command):
        return self.IOTCentralAPIService.send_command(device=device, command=command)
    

    def update_property(self, device_name, payload:str):
        return self.IOTCentralAPIService.update_property(device=device_name, payload=payload)


    def _filter_objects_by_type(self, typeName: type, iot_objs_list: list) -> list[type]:
        return [x for x in iot_objs_list if isinstance(x, typeName)]
