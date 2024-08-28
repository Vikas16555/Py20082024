# escape sequence
print("Hello world")
print("Hello\nworld")      # I can also write hello \n world coz > newline world will go new line
print("Hello\tworld")      # I can also write hello \t world coz > tabline coz space given betwn
print("Hello\bworld")      # I can also write hello \b world coz > backspace deleted in btwn


# dir = 'c:\Vikas\n.txt' this will come in newline in single coat if we use double coat same thing hpn
# to fix this need to put r means raw to avoid the converstion to the escpe seq ex below
# R concept will be used in Automation API, web automation, file_path = r concept
# r also work with single ' coat also " .
#  to get the directy name then we use r raw string
# we can use single coat and double coat but in single coat need to put escpe seq. we prefer double "
name = 'vikas\'mahato'
name2 = "Vikas Mahato"
print(name)
print(name2)

dir = r"c:\Vikas\n.txt"
print(dir)