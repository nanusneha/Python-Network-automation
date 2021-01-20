from netmiko import ConnectHandler

device_info = {'host': '100.1.1.1',
                'port': '22',
                 'username':'sneha'
                 , 'password':'cisco'
                 , 'secret':'cisco',
                  'device_type':'cisco_ios'}
connection = ConnectHandler(**device_info)
print('Entering the enable mode ')
connection.enable()

output = connection.send_config_from_file('ospf.txt')
print(output)

print('Closing the connection')
connection.disconnect()