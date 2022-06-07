class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.start = -1
        self.end = -1

    def __repr__(self) -> str:
        """
        Function to print out the queue
        O(1)

        Returns:
            str: string representation of the class
        """
        return " ".join([str(val) for val in self.queue])

    def enqueue(self, data) -> None:
        """        
        Function to enqueue data into the end of the queue
        O(n)
        Args:
            data (object): data to be inserted at the beginning of the queue
        """
        assert not self.isFull(), "Queue is full"

        # if end pointer is at the end then we change it to 0
        if self.end + 1 == self.capacity:
            self.end = 0
        else:
            self.end += 1
            if self.start == -1:  # if this is the first element being inserted
                self.start = 0
        self.queue[self.end] = data

    def dequeue(self):
        """
        Function to dequeue data from the start of the queue
        O(n)
        Args:
            data (object): data to be inserted at the beginning of the queue
        """
        assert not self.isEmpty(), "Queue is empty"

        deqItem = self.queue[self.start]
        start = self.start
        if self.start + 1 == self.capacity:
            self.start = 0
        elif self.start == self.end:  # if this is the only item in the queue
            self.start = self.end = -1
        else:
            self.start += 1
        self.queue[start] = None
        return deqItem

    def peek(self) -> object:
        """
        Function to only return data from the start of the queue
        O(1)

        Returns:
            object: Data to be returned from the top of the queue
        """
        assert not self.isEmpty(), "Queue is empty"
        return self.queue[self.start]

    def isFull(self) -> bool:
        """
        Check whether the queue has reached max capacity

        Returns:
            bool: True if len(queue) is the max capacity
        """
        if self.end + 1 == self.start:
            return True
        elif self.start == 0 and self.end + 1 == self.capacity:
            return True
        else:
            return False

    def isEmpty(self) -> bool:
        """
        Check whether the queue is empty
        O(1)

        Returns:
            bool: True if end pointer of queue is at -1 else False
        """
        return self.end == -1

    def deleteQueue(self) -> None:
        """
        Function to delete the entire queue
        O(1)
        """
        self.queue = [None] * self.capacity
        self.start = -1
        self.end = -1


if __name__ == "__main__":
    queue = Queue(5)
    print(queue.isEmpty())
    queue.enqueue(2)
    queue.enqueue(-2)
    queue.enqueue(4)
    queue.enqueue(1)
    print(queue.isFull())
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    print(queue)
