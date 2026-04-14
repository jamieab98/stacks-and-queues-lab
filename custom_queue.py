import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # TODO: Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # TODO: Remove and return the item from the front of the queue
        popped = self.items.pop(0)
        return(popped)

    def peek(self):
        # TODO: Return the item at the front of the queue without removing it
        next = self.items[0]
        return(next)

    def is_empty(self):
        # TODO: Return True if the queue is empty
        if self.items == []:
            return True

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        # TODO: Implement winner selection and dequeue process
        random_position = random.randint(0, len(self.items)-1)
        winner = self.items[random_position]
        i = 0
        while i < random_position + 1:
            self.dequeue()
            i += 1
        return (f'Customer # {random_position + 1}')

q = Queue()
q.enqueue("Jamie")
q.enqueue("Michael")
q.enqueue("Bobby")
q.enqueue("Labby")
q.enqueue("Hannah")
q.enqueue("Kallen")
print(q.select_and_announce_winner())