class ListNode:
    def __init__(self, val: object = None, next=None, prev=None):
        """
        Single Node Object for Linked List
         O(1)

        Args:
            val (_type_, optional): Data stored in the node. Defaults to None.
            next (_type_, optional): Pointer to the next node. Defaults to None.
            prev (_type_, optional): Pointer to the previous node. Defaults to None.
        """
        self.val = val
        self.next = next
        self.prev = prev


class CircularDoublyLinkedList:
    def __init__(self):
        """
        Constructor for a circular doubly linked list
        O(1)
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        """
        Iterator to iterate over the doubly linked list
        O(n)
        """
        curr = self.head
        while curr:
            yield curr
            if curr.next == self.head:  # to ensure there is no infinite loop
                break
            curr = curr.next

    def createCircularDoublyLinkedList(self, value: object) -> None:
        """
        Creates a circular doubly linked list
        O(1)

        Args:
            value (object): Value for the first node in the DBLList
        """

    def insert(self, value: object, index: int) -> None:
        """
        Insert a node in the circular doubly linked list
        O(n)

        Args:
            value (_type_): Value to be stored in the new list node
            index (int): location of the new list node
        """

    def traverse(self) -> None:
        """
        Traverse through a circular doubly linked list
        O(n)
        """

    def search(self, value: object) -> bool:
        """
        Search for a specified value in circular doubly linked list
        O(n)

        Args:
            value (object): Value to be queried
        Returns:
            bool: True if value is found else False
        """

    def deleteByIndex(self, index: int):
        """
        Delete a node from the circular doubly linked list at a given index
        O(n)

        Args:
            index (int): Index of node to be deleted
        """

    def deleteCircularDoublyLinkedList(self):
        """
        Delete the entire circular doubly linked list
        O(1)
        """
