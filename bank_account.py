
class Bank:
	users = {}
	
	def __init__(self,bal,name,num):
		
		self.acc = num 
		self.name = name		
		self.bal = bal
		self.min = 500
		self.users[self.acc] = [["                    ",f"{self.bal}" + " "* (20- len(f"{self.bal}"))]]
		print(f"account number : {self.acc}")

	def withdraw(self,amt,acc):
		if acc not in self.users.keys():
			print("account not present")
		else:
			temp = self.bal - amt
			if(temp < self.min):
				print(f"maintain minimum balance{self.min} current bal {self.bal}")
			else:
				self.bal -= amt
				self.users[self.acc].append(["-"+f"{amt}"+ " " * (20- len(f"{self.bal}")),f"{self.bal}" + " "* (20- len(f"{self.bal}"))])
		

	def deposit(self,amt,acc):
		if acc not in self.users.keys():
			print("account not present")
		else:
			self.bal += amt
			self.users[self.acc].append([f"{amt}"+ " " * (21- len(f"{self.bal}")),f"{self.bal}" + " "* (20- len(f"{self.bal}"))])
			

	def trans(self,acc):
		print('Transactions          ','     Balance             ')
		self.users[self.acc].reverse()
		for i in range(self.users[self.acc].__len__()):
			print(self.users[self.acc].pop())
		


	






