import subprocess, sys

options = ['Shutdown', 'Restart']
print('''
 _____ _           _      _                      ___  ___                                    __   _____ 
/  ___| |         | |    | |                     |  \/  |                                   /  | |  _  |
\ `--.| |__  _   _| |_ __| | _____      ___ __   | .  . | __ _ _ __   __ _  __ _  ___ _ __  `| | | |/' |
 `--. | '_ \| | | | __/ _` |/ _ \ \ /\ / | '_ \  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ | '__|  | | |  /| |
/\__/ | | | | |_| | || (_| | (_) \ V  V /| | | | | |  | | (_| | | | | (_| | (_| |  __| |    _| |_\ |_/ /
\____/|_| |_|\__,_|\__\__,_|\___/ \_/\_/ |_| |_| \_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|    \___(_\___/ 
                                                                            __/ |                       
                                                                           |___/                        
''')

choice = int(input("\nWarning: Save your important works before proceeding further\n\n1. {}\n2. {}\n\nEnter your choice: ".format(*options)))
if choice in [1, 2]:
	time = input("\nEnter time (in ms) after which you want to {}: ".format(options[choice-1]))
	try:
		t = int(time)
		if t < 0:
			raise ValueError
	except ValueError:
		print("\nSystem error occured\nCannot perform operation\nProgram exiting.....")
		sys.exit(0)
	if choice == 1:
		subprocess.call(["shutdown", "-f", "-s", "-t", time])
	else:
		subprocess.call(["shutdown", "-f", "-r", "-t", time])
else:
	print("Wrong Input/nProgram exiting.....")
