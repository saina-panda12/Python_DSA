#153=1^3+5^3+3^3=153

n = 153
original = n               # keep the original value
nod = len(str(n))
total = 0
while n > 0:
    dig = n % 10
    total += dig ** nod
    n //= 10
print(total == original)   # True for 153
