class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0,item) # 비효율적이다.
    
    def dequeue(self):
        if self.items:
            return self.items.pop()
        else:
            print('Queue is empty!')
    
    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __repr__(self):
        return repr(self.items)

if __name__ == '__main__':
    queue = Queue()
    print(f'큐가 비었습니까? : {queue.isEmpty()}')
    for i in range(3):
        queue.enqueue(i)

    print(queue)
    print(f'peek : {queue.peek()}')
    print(f'dequeue : {queue.dequeue()}')
    print(f'peek : {queue.peek()}')
    print(queue)