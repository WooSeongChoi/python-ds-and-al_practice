class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Linked_Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not self.head

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
        else:
            print('Queue is empty!')
    
    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def print(self):
        node = self.head
        while node:
            print(node.value, end = ' ')
            node = node.pointer
        print()

if __name__ == '__main__':
    queue = Linked_Queue()
    print(f'is empty? : {queue.isEmpty()}')
    for i in range(3):
        queue.enqueue(i)
    queue.print()

    for i in range(3, 10):
        queue.enqueue(i)
    queue.print()

    print(f'peek : {queue.peek()}')
    print(f'dequeue : {queue.dequeue()}')
    print(f'peek : {queue.peek()}')
    queue.print()
    queue.enqueue(11)
    queue.print()