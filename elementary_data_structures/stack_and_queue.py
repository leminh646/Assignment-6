class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        """Push value onto the top of the stack."""
        self._data.append(value)

    def pop(self):
        """Remove and return the top value. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Return the top value without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"

class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, value):
        """Add value to the back of the queue."""
        self._data.append(value)

    def dequeue(self):
        """Remove and return the front value. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.pop(0)

    def peek(self):
        """Return the front value without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._data[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self._data)

    def __repr__(self):
        return f"Queue({self._data})"

# Stack usage
s = Stack()
print(s.is_empty())   # True
s.push(1)
s.push(2)
s.push(3)
print(s)              # Stack([1, 2, 3])
print(s.peek())       # 3
print(s.pop())        # 3
print(s)              # Stack([1, 2])

# Queue usage
q = Queue()
print(q.is_empty())   # True
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q)              # Queue(['a', 'b', 'c'])
print(q.peek())       # 'a'
print(q.dequeue())    # 'a'
print(q)              # Queue(['b', 'c'])
