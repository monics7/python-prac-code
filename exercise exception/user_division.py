print('We can divide any two numbers')
print('enter q to quit')

while True:
    first_number = input("Enter first number")
    if first_number == 'q':
        break
    second_number = input("Enter second number")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
