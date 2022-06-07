class Queue:
    def __init__(self):
        self.queue = []

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
        Function to enqueue data into the end of queue
        O(n)
        Args:
            data (object): data to be inserted at the beginning of the queue
        """
        self.queue.append(data)

    def dequeue(self):
        """
        Function to dequeue data from the start of queue
        O(n)
        Args:
            data (object): data to be inserted at the beginning of the queue
        """
        assert not self.isEmpty(), "Queue is empty"
        return self.queue.pop(0)

    def peek(self) -> object:
        """
        Function to only return data from the top of the queue
        O(1)

        Returns:
            object: Data to be returned from the top of the queue
        """
        assert not self.isEmpty(), "Queue is empty"
        return self.queue[0]

    def isEmpty(self) -> bool:
        """
        Check whether the queue is empty
        O(1)

        Returns:
            bool: True if queue is empty else False
        """
        return self.queue == []

    def deleteQueue(self) -> None:
        """
        Function to delete the entire queue
        O(1)
        """
        self.queue = None


if __name__ == "__main__":
    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue(2)
    queue.enqueue(-2)
    queue.enqueue(4)
    queue.enqueue(1)
    print(queue)
    print(queue.peek())
    print(queue.dequeue())
    print(queue)
