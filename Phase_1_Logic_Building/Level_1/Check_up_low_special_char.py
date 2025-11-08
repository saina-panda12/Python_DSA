char= input("Enter String : ")

if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
elif char.isdigit():
    print("Digit")
else:
    print("special character")
