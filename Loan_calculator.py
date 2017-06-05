
print ("Loan calculator")

borrowed = int(raw_input("Amount borrowed: "))
rate = int(raw_input("Interest borrowed: "))
years = int(raw_input("years: "))

print (borrowed)
print(rate)
interest = borrowed * rate * years
payment = borrowed + interest
print ("1")


print ("Amount borrowed: " + str(borrowed))
print ("1")

print('Total interest paid: ' + str(interest))

print ("PymtNo     Amount Paid    Remaining Balance")
print ('----		-----	--------')

i = 0
amountpaid = 0
while payment != 0:  
	print (str(i) + "	" + "$ "+ str(amountpaid)+ "$" + str(payment))
	payment = payment - amountpaid
	amountpaid = payment / (years * 12)
