from netmiko import ConnectHandler

device_info = {'host':'100.1.1.1', 'port': '22', 'username':'sneha', 'password':'cisco', 'device_type':'cisco_ios',
               'secret': 'cisco'}

connection = ConnectHandler(**device_info)
prompt = connection.find_prompt()  #to check in which router mode we are in.(user mode,previlage or config mode
print(prompt)
connection.enable()  #to enter into the previlage mode
prompt = connection.find_prompt()
print(prompt)

output = connection.send_command('sh run')
print(output)
#print(connection.check_config_mode()) # it gives False coz we are in previlage mode. if its in config mode then-->true
if  not connection.check_config_mode():
    connection.config_mode()     #now it enters into global config mode.
connection.send_command('username pavan password pavan')

print('Closing connection')
connection.disconnect()
