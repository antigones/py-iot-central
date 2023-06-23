import datetime
from iot_central.Device import Device
from iot_central.IOTCentralAPIService import IOTCentralAPIService
from iot_central.classes.iot_central.CloudProperty import CloudProperty
from iot_central.classes.iot_central.Command import Command
from iot_central.classes.iot_central.Property import Property
from iot_central.classes.iot_central.Telemetry import Telemetry

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
        for device in devices.value:
            device_template = self.IOTCentralAPIService.get_template(device.template)
            complete_device = Device(
                name=device.id, 
                display_name=device.displayName,
                commands=self.filter_objects_by_type(Command, device_template.capabilityModel.contents),
                telemetries=self.filter_objects_by_type(Telemetry, device_template.capabilityModel.contents),
                cloud_properties=self.filter_objects_by_type(CloudProperty, device_template.capabilityModel.contents),
                properties=self.filter_objects_by_type(Property, device_template.capabilityModel.contents))
            complete_devices.append(complete_device)
        return complete_devices

    def send_command(self, device, command):
        self.IOTCentralAPIService.send_command(device=device, command=command)


    def filter_objects_by_type(self, typeName: type, l: list) -> list[type]:
        return [x for x in l if isinstance(x, typeName)]