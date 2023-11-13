import string
import random

print("Your Password must contains this letters or symbols or digits")
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

length= int(input("Enter the length:\n"))

password = ""

for i in range(length):
    password += random.choice(chars)
    
print("Your Password is:\n", password)