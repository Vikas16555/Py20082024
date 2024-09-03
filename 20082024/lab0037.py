# condition and loops
# condition age>18>you are allowed to vote. True? True
# condition age< less than 18 are you allowed to vote? > false
# write a program to take a user age and let him know if he can go the club.

# logic building
# 1. user input- data type- int
# out put- string- telling the user if he can go or not

# 2 rough logic
# a user age is 21 print can go
# a user age is less than 21 print can't go

# 3 write the logic
# : is something we can't miss
# we can also use formating so the code will appear in one line
# if age >=21:
# print(f"can go club-> {age}")
# else:
# print(f"can't go with this age-> {age})
# after formating 22
#              can go club-> 22

age = input("Enter your age\n")
age = int(age)

if age >= 21:
    print("can go club")
else:
    print("can't go with age")
# with this ans
# 18
#  can't go with age
