# from netmiko import Netmiko
#
# connection = Netmiko(host = '100.1.1.1', port = '22', username = 'sneha', password = 'cisco', device_type='cisco_ios')
#
# output = connection.send_command('sh ip int brief')
# print(output)

from netmiko import ConnectHandler

device_info = {'host' :'100.1.1.1', 'port':'22', 'username':'sneha', 'password':'cisco',
              'device_type':'cisco_ios'}
connection = ConnectHandler(**device_info)

output = connection.send_command('sh ver')
print(output)

print('Closing connection')
connection.disconnect()


# in netmiko we do not need time.sleep() cmd and ter length 0 to print entire output.
