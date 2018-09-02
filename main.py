from bank_account import Bank

num = 8000
while(True):
	choice = int(input("1.creation \n 2.withdrawl \n 3.deposit \n 4.transaction  \n"))
	if choice == 1:
		name = input("enter the name")
		bal = eval(input("enter the amount"))
		
		num = num + 1
		user = Bank(bal,name,num)
	elif choice	== 2:
		acc = eval(input("enter the account number"))
		amt = eval(input("enter the amount"))		 
		user.withdraw(amt,acc)

	elif choice	== 3:
		acc = eval(input("enter the account number"))
		amt = eval(input("enter the amount"))		 
		user.deposit(amt,acc)

	elif choice	== 4:
		acc = eval(input("enter the account number"))
		user.trans(acc)

	else:
		break
		