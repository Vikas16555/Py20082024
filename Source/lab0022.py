# Take a user inputs a,b and calculate the sum, mul, div, sub
# calculator program

num1 = int(input("Enter the num 1"))
nmu2 = int(input("Enter the num2"))

print(type(num1))
print(type(nmu2))

print("sum is", num1 + nmu2)
print("sub is", num1-nmu2)
print("mul is", num1*nmu2)
print("Div is", num1/nmu2) # division is always decimal 'python is very smart lang will give float whenever
# we divide high no chance is float will come in decimals 1.56

# num1> 99 + num2 > 99 should be 198 'but' it's showing 9999 why because this is a string when we sum 2 str they join
# together
# we can't sub 2 str we can't div 2 str we can't mul 2 str.
# In this case we need to convert these into integer str to int
