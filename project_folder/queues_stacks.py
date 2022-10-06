import random

arr = [random.randint(-100, 100) for i in range(15)]


def edit(stack):
    print(stack)
    answer = str(input('Do you want to add? Or remove a value from the stack answer (1 or 2): '))
    if answer == '1':
        value = int(input('Enter int value here: '))
        stack.append(value)

    elif answer == '2':
        stack.pop(-1)

    recur = str(input('Do you still want to edit this stack? (Y/N): '))
    if recur == 'Y':
        edit(stack)
    return stack


edit(arr)