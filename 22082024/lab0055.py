# match statement
# switch in Java
# match the out put and execute

#sytnax

# match variable:
#   case pattern1:
        # code block
#  case pattern2:
        # code block

# write a program to ask the user which browser he wants to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Excute the firefox code")
    case "chrome":
        print("Excute the Chrome code")
    case "edge":
        print("Excute the Edge code")
    case "safari":
        print("Excute the safari code")
    case _:
        print("Browser Not found!")

        # if i am typing capital chrome it's saying browser not found how to fix this
        # browser_name = browser_name.lower()



