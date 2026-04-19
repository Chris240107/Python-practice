import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabets = letters + digits + special_chars

pwd_length = 12

pwd = ''

for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabets))

print(pwd)

while True:
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabets))
    if any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2:
        break

print(pwd)

