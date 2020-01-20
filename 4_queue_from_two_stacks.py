class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        elif self.in_stack and self.out_stack:
            self.in_stack.reverse()
            self.out_stack = self.in_stack + self.out_stack
            self.in_stack.clear()
        
    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))
    
    def push(self, item):
        self.in_stack.append(item)
    
    def pop(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print('Queue is empty!')
    
    def peek(self):
        if not self.out_stack:
            self._transfer
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print('Queue is empty!')
    
    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def __repr__(self):
        self._transfer()
        return repr(self.out_stack)
    
if __name__ == '__main__':
    queue = Queue()
    print(f'스텍이 비었습니까? : {queue.isEmpty()}')
    for i in range(3):
        queue.push(i)
    print(queue)

    for i in range(3,10):
        queue.push(i)
    
    print(queue)
    print(f'size : {queue.size()}')
    print(f'스텍이 비었습니까? : {queue.isEmpty()}')
    print(f'peek : {queue.peek()}')
    print(f'pop : {queue.pop()}')
    print(f'peek : {queue.peek()}')
    print(queue)
    print(f'size :{queue.size()}')