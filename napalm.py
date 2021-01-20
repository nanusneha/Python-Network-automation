from napalm import get_network_driver

driver = get_network_driver('ios')

option_arg = {'secret':'cisco'}
ios = driver('10.1.1.10', 'sneha','cisco', option_arg=option_arg)
ios.open()

print(dir(ios))

ios.close()
