def binary_search(seq, key, prio): # Complexity: O(log n)
    '''
    Takes in a sorted list and a key, then tries to find the key inside the list
    verifying the middle position of the list, if the value is found, returns the position,
    if the value is higher or lower, respectively discards the value checked and all lower or higher values
    then proceeds to execute the same method until the value is found or the list ends.
    '''
    first = 0
    last = len(seq) - 1
    found = -1

    while first<=last and found == -1:
        midpoint = (first + last) // 2
        if seq[midpoint][1] == key:
            found = midpoint
        else:
           if prio > seq[midpoint][0]:
               last = midpoint - 1
           else:
               first = midpoint + 1

    return found

class PriorityQueueList(object):
    # Creates an priority queue structure with lists.
    # self.queue = queue
    def __init__(self):
        self.queue = []

    # Returns a string with all elements from the priority queu when the object is called/ O(n)
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # Checking if the queue is empty or not / O(1)
    def isEmpty(self):
        return len(self.queue) == 0

    # Checking if the queue is empty or not / O(1)
    def size(self):
        return len(self.queue)  

    # Inserting an element in the queue / O(N log N)
    def insert(self, data, prio):
        self.queue.append((prio, data))
        self.queue.sort(reverse=True)

    # Popping an element based on priority / O(1)
    def remove(self):
        if not self.isEmpty():
            item = self.queue.pop()
            return item

    # Getting the first element based on priority / O(1)        
    def first(self):
        if not self.isEmpty():
            return self.queue[-1]

    # Searching for a element inside the queue / O(log n)
    def search(self, item, prio):
        return binary_search(self.queue, item, prio)
                

# Testing the code using a random queue as example
if __name__ == '__main__':
    prio_queue = PriorityQueueList()
    prio_queue.insert(15, 1)
    prio_queue.insert(8, 2)
    prio_queue.insert(10, 3)
    prio_queue.insert(1, 4)
    prio_queue.insert(42, 5)
    prio_queue.insert(66, 6)
    prio_queue.insert(54, 7)
    print(prio_queue)

    print(prio_queue.remove())
    print(prio_queue.size())
    print(prio_queue.first())
    print(prio_queue.search(10, 3))
    print(prio_queue)

