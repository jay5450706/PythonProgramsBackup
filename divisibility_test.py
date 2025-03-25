n = 30
if n % 2 == 0:
    print("Number is divisible by 2")
elif n % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is neither divisible by 2 nor 3")
print("Done!")

age = 20
nationality = 'kenyan'
if age > 18:
    if age < 30:
        if nationality == 'indian':
            print("You are eligible for exam")
else:
    print("You are not eligible for exam") #if your age > 18, 'You are not eligible for exam' will not printed.
    