import collections
from collections import deque

# deque is same like a list but it stores each char as an element

if __name__ == "__main__":

    d = deque('hello')      # Add as string
    print(d)
    d.append(2)
    d.appendleft(1)         # store at front
    print(d)
    d.pop()
    d.popleft()             # Pop at front
    print(d)
    d.clear()
    print(d)
    d.extend('World123')    # Add multiple elements
    print(d)
    d.extend([4,5,6])       # Add as int
    print(d)
    d.extendleft("hey")     # Store as y e h
    print(d)
    d.rotate(-1)            # Rotate left one element
    print(d)
    d.rotate(1)             # Rotate right one element
    print(d)
    d = deque('maxlen', maxlen=6)   # Set size of deque = 6
    print(d)
    d.append(1)                     # If one more add, first element will pop.
    print(d)
    d.extend('23')
    print(d)
    
    # maxlen can't be changed. But can be printed.
    print(d.maxlen)