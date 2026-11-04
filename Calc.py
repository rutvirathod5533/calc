def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "this division can't be done, please change your divider"
    return a / b

def power(a, b):
    return a ** b

def rem(a, b):
    if b == 0:
        return "remainder by zero can't be done"
    return a % b

while True:
    choice = input('addition / subtraction / multiplication / division / power / remainder / exit: ').lower()

    if choice == 'exit':
        print('Goodbye!')
        break

    if choice not in ('addition', 'subtraction', 'multiplication', 'division', 'power', 'remainder'):
        print('Invalid choice, try again.')
        continue

    try:
        x = float(input('enter your first number: '))
        y = float(input('enter your second number: '))
    except ValueError:
        print('Please enter valid numbers.')
        continue

    if choice == 'addition':
        result = add(x, y)
    elif choice == 'subtraction':
        result = sub(x, y)
    elif choice == 'multiplication':
        result = mul(x, y)
    elif choice == 'division':
        result = div(x, y)
    elif choice == 'power':
        result = power(x, y)
    else:
        result = rem(x, y)

    if isinstance(result, str):
        print(result)
    else:
        print(f'Result: {result:g}')