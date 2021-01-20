import paramiko
import time

ssh_Client = paramiko.SSHClient()
print(type(ssh_Client))
ssh_Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_Client.connect(hostname = '80.0.0.2' , port = '22', username = 'sneha', password = 'cisco',
#                   look_for_keys=False, allow_agent=False)

router = {'hostname': '100.1.1.1', 'port': '22', 'username':'sneha', 'password':'cisco'}
ssh_Client.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh_Client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int brief | ex unass\n')
time.sleep(1)
output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

print(ssh_Client.get_transport().is_active())

ssh_Client.close()