year = int(raw_input("what year: "))

while 1:
	if(year % 4 == 0 or (year % 400 == 0 and year % 100 != 0)):
			if(year == 1900) or (year == 1993): 
				print (str(year) + " is not a leap year.")
			else:
				print (str(year) + " is a leap year.")
	else:
		print (str(year) + " is not a leap year.")

	year = int(raw_input("what year: "))

# 1900 should not be a leap year, but the result is wrong 