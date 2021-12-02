# Author: CRS 12/02/21
def sum_to(n):
    total = 0
    x = 0
    while x <= int(n):
        total += x
        x += 1
        print(total)


total = input("Input an integer.")
print(sum_to(total))
