#This is a program that looks for printers on your computer and allows the user to choose the default printer.
#Created by: Brandon Ferrotta
import subprocess, re, time, sys, os
from colorama import Fore, Back, Style, init, deinit
def main():
	init()
	os.system('mode con: cols=130 lines=30')
	command = 'wmic printer get name'

	printerNames = subprocess.run(command, stdout=subprocess.PIPE,stderr = subprocess.STDOUT, encoding='utf8')
	printerList = re.findall('(?:\n)(.+)', printerNames.stdout)
	printerList1 = [elem.rstrip() for elem in printerList]

	printerList1 = [e for e in printerList1 if e not in (
			'OneNote (Desktop)',
			'OneNote for Windows 10',
			'Adobe PDF',
			'Send To OneNote 2016',
			'Fax',
			'Microsoft Print to PDF',
			'Microsoft XPS Document Writer',
			'HP LaserJet Pro M12w',
			'HP Photosmart Plus 8209a-m',
			'HP LaserJet 1022 Class Driver',
			'doPDF 8',
			'Biscom Fax Printer',
			'Add to List Biscom Fax Printer'
		)]

	listNum = len(printerList1)
	printerList2 = reversed(printerList1)

	num = listNum
	print(Fore.YELLOW + '    ___        _                        _   _       ______     _       _              _____      _           _   _             ')
	print('   / _ \\      | |                      | | (_)      | ___ \\   (_)     | |            /  ___|    | |         | | (_)            ')
	print('  / /_\\ \\_   _| |_ ___  _ __ ___   __ _| |_ _  ___  | |_/ / __ _ _ __ | |_ ___ _ __  \\ `--.  ___| | ___  ___| |_ _  ___  _ __  ')
	print("  |  _  | | | | __/ _ \\| '_ ` _ \\ / _` | __| |/ __| |  __/ '__| | '_ \\| __/ _ \\ '__|  `--. \\/ _ \\ |/ _ \\/ __| __| |/ _ \\| '_ \\ ")
	print('  | | | | |_| | || (_) | | | | | | (_| | |_| | (__  | |  | |  | | | | | ||  __/ |    /\\__/ /  __/ |  __/ (__| |_| | (_) | | | |')
	print('  \\_| |_/\\__,_|\\__\\___/|_| |_| |_|\\__,_|\\__|_|\\___| \\_|  |_|  |_|_| |_|\\__\\___|_|    \\____/ \\___|_|\\___|\\___|\\__|_|\\___/|_| |_|')
	print(Fore.YELLOW + '  _____________________________________________________________________________________________________________________________\n' + Style.RESET_ALL)
	print('  Welcome, please select a number for the printer you want to set as your default printer!\n')
	print('  ------------------------------------------------------------------------------------------\n')
	for printer in printerList2:
		num -=1
		print(Fore.GREEN + f'  Press {num} for {printer}' + Style.RESET_ALL)

	print('\n  ------------------------------------------------------------------------------------------\n')
	print('  Created by Brandon Ferrotta\n\n')
	def selection1():
		while True:
			global selection
			selection = int(input('  Enter number here, then press enter: '))
			if selection >= listNum or selection < num:
				print('\n------------------------------------------------------------------------------------------\n')
				print(Fore.RED + '  You have entered a number not in range, please try again.\n' + Style.RESET_ALL)
			else:
				break

	while True:
		try:
			selection1()
			break
		except:
			print("\n  ---------------------------------------------------------------------------------------------\n")
			print(Fore.RED + "  Error! Please enter a number between 0-" + str(listNum) + '\n' + Style.RESET_ALL)


	print(f'\n\n  The printer you selected is \'{printerList1[selection]}\'. Have a great day!')
	command2 = 'RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "' + printerList1[selection] + '"'
	subprocess.run(command2)
	time.sleep(5)
	deinit()

main()
