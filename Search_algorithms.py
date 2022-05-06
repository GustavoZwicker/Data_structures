# Time library import for real time analysis.
import time

def linear_search(seq, key):
    ''' 
    Takes in a list and a key, then tries to find the key inside the list
    verifying each position of the list, then return the position if the key is found
    or -1 if it's not.
    '''
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return -1

def binary_search(seq, key):
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
        if seq[midpoint] == key:
            found = midpoint
        else:
           if key < seq[midpoint]:
               last = midpoint - 1
           else:
               first = midpoint + 1

    return found







print('Linear Search')

# Saves the current time inside a variable.
start_time = time.time()

# Returns the position of the key value inside the given list.
print(f'Position: {linear_search([x for x in range(0, 32768)], 16384)}')

# Saves the end time inside a variable.
end_time = time.time() - start_time

# Print the time spent on the algorithm execution.
print(f'Time spent executing the linear search algorithm:\n{time.time() - start_time} seconds\n')


print('Binary Search')

# Saves the current time inside a variable.
start_time = time.time()

# Returns the position of the key value inside the given list.
print(f'Position: {binary_search([x for x in range(0, 32768)], 16384)}')

# Saves the end time inside a variable.
end_time = time.time() - start_time

# Print the time spent on the algorithm execution.
print(f'Time spent executing the binary search algorithm:\n{time.time() - start_time} seconds\n')
