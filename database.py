# This is demo that shows how an acutal database works.

# name: David uche
# website: https://daviduche03.github.io

# Email: daviduche176@gmail.com



#initialize an empty database ie: a dictionary
from colorama import init, Fore, Back
from termcolor import colored
from pyfiglet import Figlet
init(autoreset=True)
database = {}

f = Figlet(font='standard')
print(colored(f.renderText('    welcome'), 'green'))


while True:
	print (Fore.YELLOW + """
       (c) CREATE
       (G) GET INPUT BY ID
       (A) GET ALL INPUT
       (D) DELETE ALL INPUT
       (DI) DELETE BY ID
       (U) UPDATE
       (I) GET ALL ID'S
       (E) END PROGRAM'
       

 """)
	action = input(Fore.CYAN + 'what do you want to do: ')
	if action.upper() == 'C':
		id = input(Fore.GREEN + 'Enter your unique id (eg; 123 or 556): ')
		name = input('Enter your name: ')
		password = input('Enter your password: ')
		database[id] = name, password
	elif action.upper() == 'G':
		id = input('Enter your id: ')
		if not id in database:
			print (Fore.RED + 'invaid id')
		else:
			print (f'Your data is {database[id]}')
	elif action.upper() == 'A':
		print (Fore.BLUE + f"{database}")
		if database == {}:
			print (Fore.GREEN + 'Database is empty')
	elif action.upper() == 'D':
		if database == {}:
			print ('Database is already cleared')
		else:
			database.clear()
			print ('Bye, database deleted have a nice day')
	elif action.upper() == 'DI':
		id = input('id: ')
		if not id in database:
			print (Fore.GREEN + "ID not in DATABASE")
		else:
			del database[id]
			print ('item deleted')
	elif action.upper() == 'U':
		id = input('id: ')
		if not id in database:
			print (Fore.BLUE + "ID doesn't match")
		else:
			name = input('New name: ')
			password = input('New password: ')
			database[id] = name, password
	elif action.upper() == 'I':
		db = {"password": 'dave'}
		word = input(Fore.GREEN + 'Enter password: ')
		if not word in db['password']:
			print (Fore.RED + 'Wrong password')
		else:
			print (database.keys())
	
	elif action.upper() == 'E':
		break
