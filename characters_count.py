string = input("Enter a string: ")

digits, letters, special = 0, 0, 0

for character in string:
    if character.isdigit():
        digits += 1
    elif character.isalpha():
        letters += 1
    else:
        special += 1

print(f'Digits: {digits}')
print(f'Letters: {letters}')
print(f'Special Characters: {special}')