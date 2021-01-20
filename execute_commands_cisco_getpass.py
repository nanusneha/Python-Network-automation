import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass('Enter the password:')
router = {'hostname': '80.0.0.2', 'port':'22', 'username': 'sneha', 'password': password}
ssh_client.connect(**router, look_for_keys=False , allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal length 0 \n')
shell.send('show ip int brief\n')
time.sleep(1)
output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

print(ssh_client.get_transport().is_active())
# the password 'cisco' is hard coded so its not secure. to avoid that we import getpass
#password = getpass.getpass('str') and in the dict i will use password.
#it doesnt work here so click on the network automation dic, copy-->absolute path
# go to windows terminal cd paste it.
#dir ( to check all the directory)
#to run the script copy the name of the file then > python <name of the script paste it>
#we can see all the output on the terminal.


