name = input ('Enter your name:  ')
num1 = int(input('Enter your first number:   '))
sign = input('Enter your operator:   ')
num2 = int(input('Enter your second number:    ' ))

if sign =='+':
    print(num1 + num2)
elif sign == '-':
    print (num1 - num2)
elif sign == '*':
    print(num1/num2)
else:
    print(f'{name}, you no get sense at all!!!!!!!!!!!      ')
    