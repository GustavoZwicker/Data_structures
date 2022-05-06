import heapq
from random import randint

class PriorityQueueHeap(object): 
    # Creates an priority queue structure with heaps.
    # self.queue = queue
    def __init__(self):
        self.queue = []

    # Returns a string with all contents from the priority queu when the object is called/ O(n)
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # Checking if the queue is empty or not / O(1)
    def isEmpty(self):
        return len(self.queue) == 0

    # Checking if the queue is empty or not / O(1)
    def size(self):
        return len(self.queue)  

    # Inserting an element in the queue / O(log n)
    def insert(self, data, prio):
        heapq.heappush(self.queue, (prio, data))

    # Popping an element based on priority / O(log n)
    def remove(self):
        if not self.isEmpty():
            return heapq.heappop(self.queue)

    # Getting the first element based on priority / O(1)        
    def first(self):
        if not self.isEmpty():
            return self.queue[0]

    # Searching for a element inside the queue(heap) / O(n) 
    def search(self, item):
        if not self.isEmpty():
            for i in range(len(self.queue)):
                if self.queue[i][1] == item:
                    return i

# Testing the code using a random queue as example
if __name__ == '__main__':
    prio_queue = PriorityQueueHeap()
    for x in range(10):
        prio_queue.insert(randint(0, 40), randint(1, 10))
        print(prio_queue)
    print(prio_queue.size())
    print(prio_queue.first())
    print(prio_queue.search(15))
    while not prio_queue.isEmpty():
        print(prio_queue)
        print(prio_queue.remove())
    print(prio_queue)
    print(prio_queue.isEmpty())
