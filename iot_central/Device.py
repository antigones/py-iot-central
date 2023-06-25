

from iot_central.classes.iot_central.property import Property
from iot_central.classes.iot_central.cloud_property import CloudProperty
from iot_central.classes.iot_central.telemetry import Telemetry
from iot_central.classes.iot_central.command import Command


class Device:

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