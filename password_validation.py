import re

password = input('Enter the password: ')
password_length =  len(password)

is_valid = False

while True:
    if password_length < 7 or password_length > 20: break
    elif not re.search('[A-Z]', password): break
    elif not re.search('[a-z]', password): break
    elif not re.search('[0-9]', password): break
    elif not re.search('[$#@!]', password): break
    elif re.search('\s', password): break
    else:
        is_valid = True
        break

if is_valid:
    print("Password is valid.")
else:
    print("Password is invalid.")
