class Stack():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top_index = -1
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        try:
            if self.is_empty():
                raise IndexError("Pop from empty stack")
            self.__top_index -= 1
            return self.__stack.pop()
        except IndexError as msg:
            print(msg)

    def push(self, value):
        try:
            if self.is_full():
                raise IndexError("Push to full stack")
            self.__top_index += 1
            self.__stack.append(value)
        except IndexError as msg:
            print(msg)

    def top(self):
        try:
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self.__stack[self.__top_index]
        except IndexError as msg:
            print(msg)


if __name__ == '__main__':
    stack1 = Stack(capacity=5)
    stack1.push(1)

    assert stack1.is_full() == False
    stack1.push(2)

    print(stack1.is_full())  # False
    print(stack1.top())  # 2
