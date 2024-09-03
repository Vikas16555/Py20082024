# write a program to find the max between
# logic building formula
# 1 user inputs > two integers
# 2 out put > int 1 which ever is greater max number it will return
# 3 input method
# we need to ask from the interwar which data typ you are expecting will it int or float
# why float suppose if user wants to compare 31.4 or 45.36
# when we are in doubt we should ask
# num1 = float(input("Enter the num1\n"))
# num2 = float(input("Enter the num2\n"))


num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))

if num1 > num2:
    print("Max is", num1)
else:
    print("max is", num2)
