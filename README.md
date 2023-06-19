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
        auth_type="SharedAccessSignature",
        # auth_type="Bearer",
        token=SAS_TOKEN)

    # get template for device
    devices_response = iotc.list_devices()

    devices = devices_response.value
    print('devices')
    print(devices)

    # get commands from device template
    template_for_device = iotc.get_template(<template_dtmi>)
    print('template')
    print(template_for_device)
    template_commands = template_for_device.get_commands()
    print('commands')
    command_list = list(template_commands)
    
    ...
    
    res = iotc.send_command(device_name, <command_name>)
    print(res)
    