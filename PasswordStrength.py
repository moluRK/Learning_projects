# PAssword strength checker
import numbers
import string
print("creat a password with at least 1 upper case , 1 llowercase and 1 symbols along with numbers.")
password=input("creat a password: ")
lower=string.ascii_lowercase
upper=string.ascii_uppercase
panchuation =string.punctuation
if any(char in lower for char in password) and any(char in upper for char in password) and any(char in panchuation for char in password):
    print("Good password.")
else:
    print("please choose a strong password!")