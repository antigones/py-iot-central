from iot_central.IOTCentralAPIService import IOTCentralAPIService
from iot_central.classes.iot_central.CloudProperty import CloudProperty
from iot_central.classes.iot_central.Command import Command
from iot_central.classes.iot_central.Telemetry import Telemetry

class Device:

    def __init__(self, name:str, display_name:str, commands:list[Command], telemetries:list[Telemetry], properties, cloud_properties:list[CloudProperty]):
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