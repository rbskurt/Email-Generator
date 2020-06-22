from random import randint


fname = input(str('What is your first name?'))
lname = input(str('What is your last name?'))
number = str(randint(0,999))
domain = input(str('gmail or yahoomail?'))

email = fname + lname + number + '@' + domain + '.com'
print(email)
