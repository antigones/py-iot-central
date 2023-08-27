from iot_central.iotc_objects import Command, Telemetry, CloudProperty, Property
from iot_central.responses import IOTCentralApiErrorResponse

from iot_central.iotcentral_api_service import IOTCentralAPIService



class IOTCentralError(BaseException):
    pass

class CompleteDevice:

    def __init__(self, name:str, display_name:str, commands:list[Command], telemetries:list[Telemetry], properties: list[Property], cloud_properties:list[CloudProperty]):
        self.name = name
        self.display_name = display_name
        self.commands = commands
        self.telemetries = telemetries
        self.properties = properties
        self.cloud_properties = cloud_properties
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name


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
    
    def get_devices(self) -> list[CompleteDevice]:
        complete_devices = list()
        devices = self.IOTCentralAPIService.get_devices()
        if isinstance(devices, IOTCentralApiErrorResponse):
            raise IOTCentralError()
        for device in devices.value:
            device_template = self.IOTCentralAPIService.get_template(device.template)
            if isinstance(device_template, IOTCentralApiErrorResponse):
                raise IOTCentralError()
            complete_device = CompleteDevice(
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
    
    def get_telemetry(self, device_name, property):
        return self.IOTCentralAPIService.get_telemetry(device=device_name, property=property)


    def _filter_objects_by_type(self, typeName: type, iot_objs_list: list) -> list[type]:
        return [x for x in iot_objs_list if isinstance(x, typeName)]


