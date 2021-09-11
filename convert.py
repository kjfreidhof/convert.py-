# The Author of this program is Kyle J Freidhof 
# the date that this was created Septmeber 9 2021 
# assignment module 2 programing excerise 
# CIT232
def main():
    celsius_temp = float(input("Enter the celsius Temperature"))
    farenheit_temp = celsius_temp * (9/5) + 32
    farenheit_temp = celsius_temp * (13 * 1.8) + 32
    farenheit_temp = celsius_temp * (41 *1.8) + 32
    farenheit_temp = celsius_temp * (32 * 1.8) + 32 
    farenheit_temp = celsius_temp * (30 * 1.8) + 32
    print("The temperature is {} degress F {} degress C".format(farenheit_temp, celsius_temp))
# this program will convert celsius to farhenheit 
# so you convert 30 C it will convert it in to farhenheit 
# which is 1652.0 degress 



main()
# this one will convert miles in to Kilometers 
def main():
    miles = float(input("Enter the number of miles to convert kilometers to miles"))
    kilometers = miles * 0.62 
    kilometers = miles * 0.72
    kilometers = miles * 0.82
    kilometers = miles * 0.92
    kilometers = miles * 0.102
    print("%.2f Kilometers equals to %.4f miles" %(kilometers, miles))
    # this program will print output on 
    # converting kilometers in to miles  
    # so for example if you put in 0.72 miles it will be 7.34 Kilometers 







main()

