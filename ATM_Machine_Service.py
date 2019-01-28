#! /usr/bin/env python
# -*- coding: UTF-8 -*-
print("""=======================================================================
                           ONR BANK
                            WELCOME
Please Insert Your Card and Press 1 or Press 9 to Continue Without Card
=======================================================================""")
def withcard():
	balance = 2000
	while True:
		print("""Services:
			1. Balance Screening
			2. Withdraw Cash
			3. Deposit Cash
			4. Transfer Cash
			5. Cancel""")
		choice = input("Service: ")
		if choice == "1":
			print("Please Wait...")
			print("Your Balance is {}£".format(balance))
			choicebalance = input("For New Service 1, Cancel 2: ")
			if choicebalance == "1":
				continue
			elif choicebalance == "2":
				print("Have a Good Day...")
				break
			else:
				print("Invalid Option, Please Try Again...")
				continue
		elif choice == "2":
			print("Please Wait...")
			cashwanted = int(input("Please Enter Amount or Press 0 to Cancel: "))
			if cashwanted > balance:
				print("Sorry. There is No Enough Money in Your Account...")
				continue
			elif cashwanted == "0":
				print("Have a Good Day...")
				break
			else:
				print("Your Cash is Being Counted. Please Wait...")
				balance -= cashwanted
				print("Balance is {}£. Please Do Not Forget Your Card...".format(balance))
				break
		elif choice == "3":
			print("Please Wait...")
			cashin = int(input("Please Enter Amount or Press 0 to Cancel: "))
			if cashin == "0":
				print("Have a Good Day...")
				break
			elif cashin < 10:
				print("You Can Not Deposit Less Than 10£...")
				continue
			else:
				print("Your Cash is Being Counted. Please Wait...")
				balance += cashin
				print("Your Balance is {}£, Thank You for Your Payment...".format(balance))
				continue
		elif choice == "4":
			print("Please Wait...")
			cashtransfer = int(input("Please Enter Amount or Press 0 to Cancel: "))
			if cashtransfer > balance:
				print("There is No Enough Money in Your Account...")
				continue
			elif cashtransfer == "0":
				print("Have a Good Day...")
				break
			else:
				transferconfirmation = input("Do You Confirm The Amount {}£(to Confirm Press 'y' nor Press 'n': ".format(cashtransfer))
				if transferconfirmation == "y":
					print("Transfer in Progress. Please Wait...")
					balance -= cashtransfer
					print("Your Balance is {}£, Transfer is Approved...".format(balance))
					continue
				elif transferconfirmation == "n":
					print("Process is Aborting, Please Wait...")
					break
				else:
					print("Invalid Option. Please Try Again...")
					continue
		elif choice == "5":
			print("Have a Good Day, Please Do Not Forget Your Card...")
			break
		else:
			print("Invalid Option. Please Try Again...")
			continue
def withoutcard():
	balance = 2000
	difacount = 2000
	while True:
		print("""Services :
		1. Deposit Cash
		2. Transfer Cash
		3. Cancel""")
		choice = input("Service: ")
		if choice == "1":
			print("Please Wait...")
			cashin = int(input("Please Enter Amount or Press 0 to Cancel:  "))
			if cashin == 0:
				print("Have a Good Day...")
				break
			else:
				balance += cashin
				print("Cash is Depositing...")
				print("It is Done. Thank You...")
				continue
		elif choice == "2":
			print("Please Wait...")
			cashtransfer = int(input("Please Enter Amount or Press 0 to Cancel: "))
			if cashtransfer == 0:
				print("Have a Good Day...")
				break
			else:
				print("Please Wait...")
				difacount +=cashtransfer
				continue
		elif choice == "3":
			print("Have a Good Day...")
			break
		else:
			print("Invalid Option. Please Try Again...")
			continue
def process():
	choice = input("Card or Without Card: ")
	while True:
		pin = "1234"
		if choice == "1":
			print("Please Wait...")
			userpin = input("Please Enter Pin: ")
			if userpin == "1234":
				print("Welcome...")
				withcard()
			else:
				print("Invalid Option. Please Try Again...")
				continue
		elif choice == "9":
			print("Please Wait...")
			withoutcard()
		else:
			print("Invalid Option. Please Try Again...")
			break
process()

