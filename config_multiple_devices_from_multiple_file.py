from netmiko import ConnectHandler
with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()
for ip in devices:
    device_info = {'host': ip , 'port': '22', 'username':'sneha', 'password':'cisco',
                     'device_type': 'cisco_ios', 'secret':'cisco'}
    device_list.append(device_info)
print(device_list)

for device in device_list:
    connection = ConnectHandler(**device)

    print('Entering into enable mode')
    connection.enable()

    File = input(f'Enter the configuration file for {device["host"]}:')

    output = connection.send_config_from_file(File)
    print(output)

    print(f'Closing the connection {device_info["host"]}')
    connection.disconnect()

    print('#' * 30)







print('Connection closing')
