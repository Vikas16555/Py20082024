# break- based on condition, exit the loop
for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        pass   # pass basically mean not out put o


    # |i| condition| o/p
    # | 0 | 0== 6 -> False | o/p -> No o/p
    # | 1 | 1== 6 -> False | o/p -> No o/p
    # | 2 | 2== 6 -> False | o/p -> No o/p
    # | 3 | 3== 6 -> False | o/p -> No o/p
    # | 4 | 4== 6 -> False | o/p -> No o/p
    # | 5 | 5== 6 -> False | o/p -> No o/p
    # | 6 | 5== 6 -> True | o/p -> 6
    # | 7 | 7== 6 -> False | o/p -> No o/p

