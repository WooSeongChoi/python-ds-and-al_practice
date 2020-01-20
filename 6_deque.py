from queue import Queue

class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)
    
    def dequeue_front(self):
        if self.items:
            return self.items.pop(0)
        else:
            print('Deque is empty!')

if __name__ == '__main__':
    deque = Deque()
    print(f'덱이 비었습니까? : {deque.isEmpty()}')
    for i in range(3):
        deque.enqueue_back(i)
    print(deque)
    
    for i in range(3,7):
        deque.enqueue(i)
    print(deque)

    print(f'덱이 비었습니까? : {deque.isEmpty()}')
    deque.dequeue_front()
    print(deque)
    print(f'size : {deque.size()}')
    print(f'peek : {deque.peek()}')