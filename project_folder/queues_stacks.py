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


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def insert(self, new_value):
        if self.next is None:
            self.next = Node(new_value)
            self.next.prev = self
            return

        self.next.insert(new_value)

    def show(self):
        print(self.value)
        if self.next is not None:
            self.next.show()


    def stack(self):
        pass

    def queue(self):
        pass


# edit(arr)

firstNode = Node(10)
firstNode.insert(6)
firstNode.insert(9)
firstNode.insert(5)
firstNode.insert(19)
firstNode.show()