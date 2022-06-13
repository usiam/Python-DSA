class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # will allow us to dequeue in O(1)
        self.tail = None  # will allow us to enqueue in O(1)

    def __iter__(self) -> ListNode:
        """
        Iterator to iterate over the singly linked list
        O(n)
        """
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def __repr__(self) -> str:
        """
        Function to print out the queue
        O(1)

        Returns:
            str: string representation of the class
        """
        return " ".join([str(node.val) for node in self.queue])

    def enqueue(self, data) -> None:
        """        
        Function to enqueue data into the end of queue
        O(n)
        Args:
            data (object): data to be inserted at the beginning of the queue
        """
        node = ListNode(data, None)
        if self.isEmpty():
            self.queue.head = node
            self.queue.tail = node
        else:
            self.queue.tail.next = node
            self.queue.tail = node

    def dequeue(self):
        """
        Function to dequeue data from the start of queue
        O(n)
        Args:
            data (object): data to be inserted at the beginning of the queue
        """
        assert not self.isEmpty(), "Queue is empty"

        retVal = self.queue.head.val
        if self.queue.head == self.queue.tail:
            self.queue.head = self.queue.tail = None
        else:
            self.queue.head = self.queue.head.next
        return retVal

    def peek(self) -> object:
        """
        Function to only return data from the top of the queue
        O(1)

        Returns:
            object: Data to be returned from the top of the queue
        """
        assert not self.isEmpty(), "Queue is empty"

        return self.queue.head.val

    def isEmpty(self) -> bool:
        """
        Check whether the queue is empty
        O(1)

        Returns:
            bool: True if queue is empty else False
        """
        return self.queue.head == None

    def deleteQueue(self) -> None:
        """
        Function to delete the entire queue
        O(1)
        """
        self.queue.head = None
        self.queue.tail = None


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
