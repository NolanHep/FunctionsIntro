def nolsters():
    x = input('Input Name:')
    print(x)
nolsters()

def birthday():
    x = input('What is your birthday?')
    print(x)
birthday()

try:
    x = int(input('Type a number!'))
    print('Success')
except ValueError as value_error:
    print('Wrong')

