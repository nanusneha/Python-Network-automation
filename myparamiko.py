import paramiko
import time

def connect(server_ip , port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=port, username=user, password=passwd ,
                       look_for_keys=False,allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=2):
    print(f'Sending the command {command}')
    shell.send(command +'\n')
    time.sleep(timeout)

def show(shell , n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
   if ssh_client.get_transport().is_active() == True:
        print('closing the connection')
        ssh_client.close()
# all the above code is to create a function for all different tasks. and we can call these functions
# in different script.
     #(if we import myparamiko.py in another script, then it will execute the myparamiko script in another script.
     # so to avoid that , before it starts execting we will write if '__name__' == '__main__' and indent it{4 spaces})

#below are the codes to run the scripts using above defined functions.
if __name__ == '__main__' :
    router1 = {'server_ip':'100.1.1.1', 'port':'22', 'user':'sneha', 'passwd':'cisco'}
    client = connect(**router1)
    shell = get_shell(client)


    send_command(shell, 'enable')
    send_command(shell, 'cisco')
    send_command(shell, 'ter len 0')
    send_command(shell, 'sh run')

    output = show(shell)
    print(output)


