def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10       # get last digit
        rev = rev * 10 + digit  # append digit to reversed number
        n = n // 10          # remove last digit
    return rev

# Example
num = 12345
print(reverse_number(num))  # Output: 54321
