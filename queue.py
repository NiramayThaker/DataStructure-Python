queue = []

# Elements will be added to the queue
queue.append('a')   # append will add new data to previous data 
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Elements will be removed from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
