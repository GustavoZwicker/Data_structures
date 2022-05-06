class Stack:
    # Class used to create and manipulate a stack. / Time Complexity: O(n) 
    def __init__(self):
        """
        Class constructor.
        Creates a variable that will contain the stack.
        """
        self.stack = []
    
    def empty(self):
        # Returns if the stack is empty / Time Complexity: O(1)
        return len(self.stack) == 0
    
    def size(self):
        # Returns the stack size / Time Complexity: O(1)
        return len(self.stack)

    def push(self, value):
        # Adds a value to the stack, through the rule of First In First Out / Time Complexity: O(1)
        self.stack.append(value)

    def pop(self):
        # Removes a value from the stack, through the rule of First In First Out / Time Complexity: O(1)
        self.stack.pop()

    def top(self):
        # Returns the stack size / Time Complexity: O(1)
        return self.stack[-1]
    
class Queue:
    # Class used to create and manipulate a queue. / Time Complexity: O(n)
    def __init__(self):
        """
        Class constructor.
        Creates a variable that will contain the queue.
        """
        self.queue = []

    def empty(self):
        # Returns if the queue is empty / Time Complexity: O(1)
        return len(self.queue) == 0

    def size(self):
        # Returns the queue size / Time Complexity: O(1)
        return len(self.queue)

    def enqueue(self, value):
        # Adds a value to the queue, through the rule Last In First Out  / Time Complexity: O(1)
        self.queue.append(value)

    def dequeue(self):
        # Removes a value from the queue, through the rule Last In First Out  / Time Complexity: O(1)
        self.queue.pop(0)

    def front(self):
        # Returns the front value from the list / Time Complexity: O(1)
        return self.queue[0]

    def rear(self):
        # Returns the front value from the list / Time Complexity: O(1)
        return self.queue[-1]



stack_1 = Stack() # Defines a stack.

# If statement that checks if the stack is empty.
if stack_1.empty():
    print('The stack is empty')
else:
    print("The stack isn't empty")

# Push 0 to 9 values to the stack.
for x in range(10):
    stack_1.push(x)

print(f'Stack size: {stack_1.size()}')
print(f'Stack top value: {stack_1.top()}')

# Pop three values from the stack.
for x in range(3):
    stack_1.pop()

print('\nAfter popping 3 values:')
print(f'Stack size: {stack_1.size()}')
print(f'Stack top value : {stack_1.top()}')

print('\n') 

queue_1 = Queue() # Defines a queue.

# If statement that checks if the queue is empty.
if queue_1.empty():
    print('The queue is empty')
else:
    print("The queue isn't empty")

# Enqueue 0-9 values to the queue.
for x in range(10):
    queue_1.enqueue(x)

print(f'Queue size: {queue_1.size()}')
print(f'Queue front value: {queue_1.front()}')
print(f'Queue last value: {queue_1.rear()}')

# Dequeue three values from the queue.
for x in range(3):
    queue_1.dequeue()

print('\nAfter dequeuing 3 values:')
print(f'Queue size: {queue_1.size()}')
print(f'Queue front value: {queue_1.front()}')
print(f'Queue last value: {queue_1.rear()}')

# Enqueue 10,19 values to the queue.
for x in range(10,20):
    queue_1.enqueue(x)
    
print('\nAfter enqueuing 10 more values:')
print(f'Queue size: {queue_1.size()}')
print(f'Queue front value: {queue_1.front()}')
print(f'Queue last value: {queue_1.rear()}')