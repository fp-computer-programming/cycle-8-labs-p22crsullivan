# Author: CRS 12/03/21
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in lst:
    if number % 3 != 0:
        continue
    print(number)
