from netmiko import ConnectHandler

device_info = {'host':'100.1.1.1', 'port':'22', 'username': 'sneha', 'password':'cisco',
                'secret': 'cisco', 'device_type': 'cisco_ios'}

connection = ConnectHandler(**device_info)
print('Entering the enable mode:')
connection.enable()
#list of commands which i want to execute.
commands = ['int loopback 1', 'ip add 1.1.1.1 255.255.255.255', 'exit', 'username u1 password cisco']
#instead of list we can also write like this
#cmd = int lo 1; ip add 1.1.1.1 255.255.255.0 ;exit
#output = connection.send_config_set(cmd.split(';'))
                   # or
# cmd = ''' int lo 1
# ip add 1.1.1.1 255.255.255.0
# exit '''
# output = connection.send_config_set(cmd.split('\n'))
output = connection.send_config_set(commands)
print(connection.find_prompt())
print(output)

connection.send_command('do wr')


print('Closing connection')
connection.disconnect()



