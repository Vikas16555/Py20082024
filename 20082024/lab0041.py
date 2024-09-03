# grade calculator
# write a program that calculates and displays the letter grade for a given numerical score
# based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59


# logic building formula need to ask user input
# 1 -> user inputs -> score -> int
# 2 -> out put-> str -> A or B .....

score = int(input("Enter your score\n"))

# score >=90 and score <=100 -> "A"
# score >=80 and score <=89 -> "B"
# score >=70 and score <=79 -> "c"
# score >=60 and score <=69 -> "D"
# score >=0 and score <=59 -> "C"
# if someone types 101 and still it's showing fail in this scenario we can add one more elif score >greater
# < smaller

if score >= 90 and score <= 100:  # simplified chaining format -> 90 <= score <= 100
    print("your grade is", "A")
elif score >= 80 and score <= 89:
    print("your grade is", "B")
elif score >= 70 and score <= 79:
    print("your grade is", "c")
elif score >= 60 and score <= 69:
    print("your grade is", "D")
elif score >=106:
    print("your are superman !!")
else:
    print("your grade is", "F")
