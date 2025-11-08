num = [12, 13, 14, 15, 1, 34, 2, 7, 8]

# res = sorted(num)
#
# result=res[-1]
#
# print(result)
#with sorting we can find the largest element

largest = num[0]

for n in num:
    if n > largest:
        largest=n
        print(largest)
