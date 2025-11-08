# Take a character and check if it’s a vowel or consonant

char = input("Enter String : ").lower()
list1 = ["a", "e", "i", "o", "u"]

if char in list1:
    print(f"{char} is a Vowel")
else:
    print("consonant")
