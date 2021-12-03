# Author: CRS 12/03/21
total = 0
while True:
    user_inp = int(input("Input a number."))
    if user_inp == -1:
        break
    else:
        total += user_inp

print(total)
