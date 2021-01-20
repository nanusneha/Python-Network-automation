import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#password = getpass.getpass('Enter the password:')
router = {'hostname':'100.1.1.1', 'port':'22', 'username':'admin', 'password':'admin'}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('enable\n')
shell.send('cisco\n')
shell.send('ter len 0\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')
# print(output)
with open('Handson_challenge.txt', 'w') as f:
    f.write(output)

