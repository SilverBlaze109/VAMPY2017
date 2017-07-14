import os

os.system("clear")

f = open("Receit.txt","w")

customer = input("What is your name? ")

Money = 0

P_Counter = 0

O_Counter = 0

CR_Counter = 0

W_Counter = 0

C_Counter = 0

J_Counter = 0

M_Counter = 0

CK_Counter = 0

CA_Counter = 0

while True:
	os.system("command espeak Enter your order")
	order = str(input("Enter your order. "))
	if order == "Pancake":
		Money = 12.99 + Money
		P_Counter = P_Counter + 1
	if order == "Omlet":
		Money = 5.99 + Money
		O_Counter = O_Counter + 1
	if order == "Cinnamin Roll":
		Money = 3.99 + Money
		CR_Counter = CR_Counter + 1
	if order == "Water":
		Money = 1.00 + Money
		W_Counter = W_Counter + 1
	if order == "Coffee":
		Money = .10 + Money
		C_Counter = C_Counter + 1
	if order == "Juice":
		Money = 1.00 + Money
		J_Counter = J_Counter + 1
	if order == "Muffin":
		Money = 1.50 + Money
		M_Counter = M_Counter + 1
	if order == "Cake":
		Money = 3.99 + Money
		CA_Counter = CA_Counter + 1
	if order == "Cookie":
		Money = 2.00 + Money
		CK_Counter = CK_Counter + 1
	if order == "Done":
		break

f.write(customer + "\n====================\n" + str(P_Counter) + " * Pancake \n" + str(O_Counter) + " * Omelt \n" + str(CR_Counter) + " * Cinnamin Roll \n" + str(W_Counter) + " * Water \n" + str(C_Counter) + " * Coffee \n" + str(J_Counter) + " * Juice \n" + str(M_Counter) + " * Muffin \n" + str(CA_Counter) + " * Cake \n" + str(CK_Counter) + " * Cookie \n" + str(Money))
