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


class DoublyLinkedList:
    def __init__(self):
        """
        Constructor for a doubly linked list
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
            curr = curr.next

    def createDoublyLinkedList(self, value: object) -> None:
        """
        Create a Doubly Linked List
        O(1)

        Args:
            value (object): value of first node in the doubly linked list
        """
        node = ListNode(value)
        self.head = node
        self.tail = node
        node.next = None
        node.prev = None
        self.length += 1
        print("Created DoublyLinkedList")

    def insert(self, value: object, index: int) -> None:
        """
        Insert a node in the doubly linked list        
        O(n)

        Args:
            value (_type_): Value to be stored in the new list node
            index (int): location of the new list node
        """

        if not self.head:
            print("The head reference is None")
            return

        node = ListNode(value)
        if index == 0:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

        elif index == -1:
            node.next = None
            node.prev = self.tail
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

        self.length += 1

    def traverse(self, reverse: bool = False) -> None:
        """
        Traverse the doubly linked list
        O(n)

        Args:
            reverse (bool): If True then traverse the doubly linked list backwards. 
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

    def traverseReverse(self) -> None:
        """
        Traverse the doubly linked list in reverse
        O(n)
        """
        if not self.head:
            print("The head reference is None")
            return
        curr = self.tail
        while curr:
            print(curr.val, end=" ")
            curr = curr.prev

    def search(self, value: object) -> bool:
        """
        Search for a value in the doubly linked list
        O(n)

        Args:
            value (object): Value to be queried

        Returns:
            bool: True if value is found, False otherwise
        """
        if not self.head:
            print("The head reference is None")
            return False
        curr = self.head
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False

    def deleteByIndex(self, index: int) -> None:
        """
        Delete a doubly linked list node by index
        O(n)

        Args:
            index (int): Index of node to delete
        """
        if not self.head:
            print("The head reference is None")
            return

        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

        elif index == -1:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

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

    def deleteDoublyLinkedList(self) -> None:
        """
        Deletes the entire doubly linked list
        O(n)
        """
        if not self.head:
            print("The head reference is None")
            return
        # remove all the references to the nodes in the linked list
        curr = self.head
        while curr:
            curr.prev = None
            curr = curr.next
        self.head = None
        self.tail = None
        print("Deleted the entire Doubly Linked List")


if __name__ == '__main__':
    dbll = DoublyLinkedList()
    dbll.createDoublyLinkedList(1)
    print([node.val for node in dbll])
    dbll.insert(1, -1)  # insert 1 at tail
    dbll.insert(2, -1)  # insert 2 at tail
    dbll.insert(3, 0)  # insert 3 at head
    dbll.insert(4, 2)  # insert 4 at index 2
    print([node.val for node in dbll])
    dbll.traverse(reverse=True)
    print(dbll.search(2))
