import string
import random
if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("Enter password lenght\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("Your password contains Uppercase(A-Z), Lowercase(a-z), Digits(0-9) and symbols(!@#$%^&*()+_=)")
    print("Your password is: ")
    print("".join(random.sample(s,plen)))