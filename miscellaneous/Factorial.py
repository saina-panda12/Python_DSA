num = int(input("Enter a number: "))
fact=1
if num <0:
    print("No factorial for -ve numbers")
elif num == 0:
    print("Fact of 0 is 1")
else:
    for i in range(1, num+1):
        fact=fact*i
    print(f'The factorial of {num} is {fact}')
