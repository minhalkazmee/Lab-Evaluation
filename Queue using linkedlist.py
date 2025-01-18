class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue
        self.size = 0      # Keeps track of the queue size

    # Add an item to the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:  # If queue is not empty
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:  # If the queue was empty
            self.front = new_node
        self.size += 1

    # Remove and return the front item from the queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:  # If the queue is empty after dequeue
            self.rear = None
        self.size -= 1
        return dequeued_node.value

    # Return the front item without removing it
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value

    # Check if the queue is empty
    def isEmpty(self):
        return self.size == 0

    # Get the current queue size
    def queueSize(self):
        return self.size

    # Display the entire queue
    def displayQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
# Create a queue and test the methods
myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")  # Use displayQueue to show the queue
myQueue.displayQueue()

print("Dequeue: ", myQueue.dequeue())  # Dequeue and show front item
print("Peek: ", myQueue.peek())  # Show front item without removing it
print("isEmpty: ", myQueue.isEmpty())  # Check if queue is empty
print("Size: ", myQueue.queueSize())  # Show current queue size
