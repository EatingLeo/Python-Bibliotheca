# !/usr/bin/env python
# -*- coding: utf-8 -*- 
T = raw_input("Enter the temperature you want to convert: ")
print ("you entered " + T)
con = raw_input("Convert between Fahrenheit or Celsius. Enter F or C： ")
print ("you entered " + con)


if con == "C":
	Tc = T
	Tf= int(Tc) * 1.8 + 32
	print (Tc + " C = " + str(Tf) + " F")
else:
	Tf = T
	Tc = 5/float(9) * (int(Tf)-32)
	print (Tf + " F = " + str(Tc) + " C")
