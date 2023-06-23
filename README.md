# py-iot-central

A small wrapper for IOTCentral API REST


Example usage:

    import os

    from dotenv import load_dotenv

    from iot_central.IOTCentral import IOTCentral

    load_dotenv()

    APP_SUBDOMAIN = os.getenv('APP_SUBDOMAIN')
    SAS_TOKEN = os.getenv('SAS_TOKEN')
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')

    iotc = IOTCentral(
    app_subdomain=APP_SUBDOMAIN,
    auth_type=AuthType.SAS_TOKEN.value, 
    token=SAS_TOKEN
    )

    devices: list[Device] = iotc.get_devices()
    print(devices)

    for device in devices:
        print(device)
        print(device.commands)
        print(device.telemetries)
        print(device.cloud_properties)
        print(device.properties)
    
    ...
    
    res = iotc.send_command(device_name, <command_name>)
    print(res)
    