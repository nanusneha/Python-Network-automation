import myparamiko

router1 = {'server_ip':'100.1.1.1', 'port':'22', 'user':'sneha', 'passwd':'cisco'}
client = myparamiko.connect(**router1)
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'ter len 0')
myparamiko.send_command(shell, 'enable')
myparamiko.send_command(shell, 'cisco')
myparamiko.send_command(shell, 'sh run')

output = myparamiko.show(shell)
#print(output)
output_list = output.splitlines()
output_list = output_list[9:-1]
#print(output_list)
output = '\n'.join(output_list)
#print(output)
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router1["server_ip"]}----{year}-{month}-{day}.txt'
print(file_name)

with open(file_name, 'w') as f:
    f.write(output)
    # all the above code will write the running config into router_backup.txt file. if i run this again tomorrow
    # it will overwrite. so we want to maintain /append running config fot 30 days.so we import datetime function before
    #writting it in a txt file.



myparamiko.close(client)