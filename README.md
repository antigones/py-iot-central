# py-iot-central

A small wrapper for IOTCentral REST API


Example usage:

    import os

    from dotenv import load_dotenv

    from iot_central.iotc_objects import AuthType
    from iot_central.iotcentral import CompleteDevice, IOTCentral, IOTCentralError

    load_dotenv()

    APP_SUBDOMAIN = os.getenv('APP_SUBDOMAIN')
    SAS_TOKEN = os.getenv('SAS_TOKEN')
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')

    iotc = IOTCentral(
        app_subdomain=APP_SUBDOMAIN,
        auth_type=AuthType.SAS_TOKEN, 
        token=SAS_TOKEN
    )

    # listing devices and properties/commands/telemetries/cloud properties
    devices: list[CompleteDevice] = iotc.get_devices()
    print(devices)

    for device in devices:
        print(device)
        print(device.commands)
        print(device.telemetries)
        print(device.cloud_properties)
        print(device.properties)
    
    ...
    
    # getting telemetry (property: 'temperature')
    res = iotc.get_telemetry(<device_id>,'temperature')
    print(res)
    
    # sending a command
    res = iotc.send_command(<device_id>, <command_name>)
    print(res)

    # updating a property
    humidity_obj = {'HumidityPercentage':random.randint(20,60)}
    payload = json.dumps(humidity_obj)
    res = iotc.update_property(<device_id>, humidity_obj)
    print(res)
    