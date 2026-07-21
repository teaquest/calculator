def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        print("Can't divide by zero")
    else:
        return number1 / number2

history = []


while True:
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    print('6. History')
    try: #add a if menu_num not in ][1,2,3,4,5]
        menu_num = int(input('Choose an option: '))
    except ValueError:
        print("Invalid selection. Enter a number 1 - 6.")
        continue


    if menu_num == 5:
        break
    
    if menu_num == 6:
        #add check if the history is blank
        print(history)
        continue

    try:
        num1 = float(input('Enter first number: '))
    except ValueError:
        print("Invalid number. Please enter a numeric value.")
        continue
    try:
        num2 = float(input('Enter second number: '))
    except ValueError:
        print("Invalid number. Please enter a numeric value.")
        continue 
    
    if menu_num == 1:
        result = add(num1, num2)
        equation = str(num1) + " + " + str(num2) + " = " + str(result)
        
    elif menu_num == 2:
        result = subtract(num1, num2)
        equation = str(num1) + " - " + str(num2) + " = " + str(result)
    
    elif menu_num == 3:
        result = multiply(num1, num2)
        equation = str(num1) + " * " + str(num2) + " = " + str(result)

    elif menu_num == 4:
        result = divide(num1, num2)
        equation = str(num1) + " / " + str(num2) + " = " + str(result)
    
        

    else:
        print("Invalid selection. Enter a number 1 - 6.")
        continue
    
    print('Result: ', result)
    history.append(equation)
    print()