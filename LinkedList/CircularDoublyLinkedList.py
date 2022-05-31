class ListNode:
    def __init__(self, val: object = None, next=None, prev=None) -> None:
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
    def __init__(self) -> None:
        """
        Constructor for a circular doubly linked list
        O(1)
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self) -> ListNode:
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
        node = ListNode(value)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node

    def insert(self, value: object, index: int) -> None:
        """
        Insert a node in the circular doubly linked list
        O(n)

        Args:
            value (_type_): Value to be stored in the new list node
            index (int): location of the new list node
        """
        assert index >= -1, "Index cannot be less than -1"

        if not self.head:
            print("The head reference is None")
            return

        node = ListNode(value)
        if index == 0:
            node.prev = self.tail
            node.next = self.head
            self.head.prev = node
            self.tail.next = node
            self.head = node

        elif index == -1:
            node.prev = self.tail
            node.next = self.head
            self.head.prev = node
            self.tail.next = node
            self.tail = node

        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node.next = curr.next
            node.prev = curr
            curr.next.prev = node
            curr.next = node

    def traverse(self, reverse: bool = False) -> None:
        """
        Traverse through a circular doubly linked list
        O(n)

        Args:
            reverse (bool, optional): If True then traverse the doubly linked list backwards.
            Defaults to False.

        """
        if reverse:
            self.traverseReverse()
            return

        if not self.head:
            print("The head reference is None")
            return

        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
            if curr == self.tail.next:
                break

    def traverseReverse(self) -> None:
        """
        Traverse the circular doubly linked list in reverse
        O(n)
        """
        if not self.head:
            print("The head reference is None")
            return
        curr = self.tail
        while curr:
            print(curr.val, end=" ")
            curr = curr.prev
            if curr == self.head.prev:
                break

    def search(self, value: object) -> bool:
        """
        Search for a specified value in circular doubly linked list
        O(n)

        Args:
            value (object): Value to be queried
        Returns:
            bool: True if value is found else False
        """
        if not self.head:
            print("The head reference is None")
            return False

        curr = self.head
        while curr:
            if curr.val == value:
                return True
            if curr == self.tail:
                break
            curr = curr.next
        return False

    def deleteByIndex(self, index: int):
        """
        Delete a node from the circular doubly linked list at a given index
        O(n)

        Args:
            index (int): Index of node to be deleted
        """
        assert index >= -1, "Index cannot be less than -1"

        if not self.head:
            print("The head reference is None")
            return

        if index == 0:
            if self.head == self.tail:
                self.head.prev, self.head.next = None, None
                self.head, self.tail = None, None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
        elif index == -1:
            if self.head == self.tail:
                self.head.prev, self.head.next = None, None
                self.head, self.tail = None, None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
        else:
            if index < self.length//2:
                curr = self.head
                for _ in range(index - 1):
                    curr = curr.next
                curr.next = curr.next.next
                curr.next.prev = curr
            else:
                curr = self.tail
                for _ in range(self.length - index - 2):
                    curr = curr.prev
                curr.prev = curr.prev.prev
                curr.prev.next = curr

    def deleteCircularDoublyLinkedList(self):
        """
        Delete the entire circular doubly linked list
        O(n)
        """
        if not self.head:
            print("The head reference is None")
            return

        curr = self.head
        while curr:
            curr.prev = None
            curr = curr.next
        self.tail.next = None
        self.head = None
        self.tail = None


if __name__ == '__main__':
    cdll = CircularDoublyLinkedList()
    cdll.createCircularDoublyLinkedList(1)
    cdll.insert(1, -1)  # insert 1 at tail
    cdll.insert(2, -1)  # insert 2 at tail
    cdll.insert(3, 0)  # insert 3 at head
    cdll.insert(4, 2)  # insert 4 at index 2
    cdll.insert(5, 3)  # insert 4 at index 2
    cdll.insert(6, 0)  # insert 4 at index 2
    cdll.insert(9, -1)  # insert 4 at index 2
    cdll.insert(7, 4)  # insert 4 at index 2
    print([node.val for node in cdll])
    cdll.deleteByIndex(0)
    cdll.deleteByIndex(2)
    cdll.deleteByIndex(-1)
    print([node.val for node in cdll])
    cdll.deleteCircularDoublyLinkedList()
    print([node.val for node in cdll])
