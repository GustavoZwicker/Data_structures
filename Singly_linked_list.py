class Node:
    """This class represents a node of a linked list"""
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    '''Function that returns a string when the node class is called alone or through repr() | O(n)'''
    def __repr__(self):
        return f'{self.data} -> {self.next}'


class LinkedList:
    """This class represents a linked list"""
    def __init__(self):
        self.head = None

    '''Function that returns a string when the list class is called alone or through repr() | O(n)'''
    def __repr__(self):
        return f"[{self.head}]"

    '''Functions to insert new elements in the list | O(1)'''
    def insert_start(self, new_data):
        # creates a new node with the data to be stored
        new_node = Node(new_data)
        # makes the new node the head of the list
        new_node.next = self.head
        # makes the list head to reference the new node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given prev_node must be in the LinkedList.")
            return
        # creates a new node with the desired data
        new_node = Node(new_data)
        # makes the next of the new nobe be the next of the previous node
        new_node.next = prev_node.next
        # makes the new node the next nobe to the previous node
        prev_node.next = new_node

    '''Functions that searches the list for an element | O(n)'''
    def search(self, value):
        chain = self.head
        i=0
        while chain != None:
            if chain.data == value:
                return i
            chain = chain.next
            i += 1
        return None

    '''Function that removes the head element from the list | O(1)'''
    def remove_head(self):
        # checks if the list is empty
        if self.head == None:
            raise ValueError('Empty List')
        # node to be removed is the head of the list
        self.head = self.head.next

    '''Function that removes an given element from the list | O(n)'''
    def remove(self, value):
        # checks if the list is empty
        if self.head == None:
            raise ValueError('Empty List')
        # node to be removed is the head of the list
        elif self.head.data == value:
            self.head = self.head.next
            return True
        # finds the position of the element to be removed
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == value:
                    ancestor.next = pointer.next
                    pointer.next = None
                pointer = pointer.next
                ancestor = ancestor.next
            return True

    '''Function that returns the value of the top of the list | O(1)'''
    def top(self):
        return self.head.data



# testing the code
# creating the list
linkedl = LinkedList()
for i in range(10):
    linkedl.insert_start(i)
print(linkedl)

print('---' * 25)
# inserting a new element at the beginning of the list
linkedl.insert_start(10)
print(linkedl)

print('---' * 25)
# insering a new element after the given node
linkedl.insert_after(linkedl.head, 9.5)
print(linkedl)

print('---' * 25)
# searching for an element in the list
i = 9
element = linkedl.search(i)
if element:
    print(f'The element {i} is present in the list at position {element}')
else:
    print(f'The element {i} is not present in the list')

print('---' * 25)
# removing an element from the list
print(linkedl)
linkedl.remove(7)
print(linkedl)

print('---' * 25)
# showing the value from the top of the list
print(f'Value from the top of the list: {linkedl.top()}')
print('---' * 25)
print(linkedl)

linkedl.insert_start(120)
print(linkedl)
print(f'Value from the top of the list: {linkedl.top()}')

print('---' * 25)
# removing the head element from the top of the list
linkedl.remove_head()
print(linkedl)
print('---' * 25)