class Queue():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        try:
            if self.is_empty():
                raise IndexError("Dequeue from empty queue")
            return self.__queue.pop(0)
        except IndexError as msg:
            print(msg)

    def enqueue(self, value):
        try:
            if self.is_full():
                raise IndexError("Enqueue to full stack")
            self.__queue.append(value)
        except IndexError as msg:
            print(msg)

    def front(self):
        try:
            if self.is_empty():
                raise IndexError("Queue is empty")
            return self.__queue[0]
        except IndexError as msg:
            print(msg)


if __name__ == '__main__':
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)

    print(queue1.is_full())  # False
    print(queue1.front())  # 1
