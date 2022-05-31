class ListNode:
    def __init__(self, val: object = None, next=None):
        """
        Single Node Object for Linked List
         O(1)

        Args:
            val (_type_, optional): Data stored in the node. Defaults to None.
            next (_type_, optional): Pointer to the next node. Defaults to None.

        """
        self.val = val
        self.next = next


class CircularSinglyLinkedList:
    def __init__(self):
        """
        Constructor for a circular singly linked list
        O(1)
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Iterator to iterate over the singly linked list
        O(n)
        """
        node = self.head
        while node:
            yield node
            if node.next == self.head:  # to ensure there is no infinite loop
                break
            node = node.next

    def createCircularSinglyLinkedList(self, value: object) -> None:
        """
        Creates a circular singly linked list
        O(1)

        Args:
            value (object): Value for the first node in the CSLList
        """
        node = ListNode(value)
        node.next = node
        self.head = node
        self.tail = node
        print("CSLList has been created!")

    def insert(self, value: object, index: int) -> None:
        """
        Insert a node in the circular singly linked list
        O(n)

        Args:
            value (_type_): Value to be stored in the new list node
            index (int): location of the new list node
        """
        node = ListNode(value)
        # If linked list has no node
        if not self.head:
            print("The head reference is None")
            return

        # insert at head
        elif index == 0:
            node.next = self.head
            self.head = node
            self.tail.next = node

        # insert at tail
        elif index == -1:
            node.next = self.head
            self.tail.next = node
            self.tail = node

        # insert at some index
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            temp = curr.next
            curr.next = node
            node.next = temp

    def traverse(self) -> None:
        """
        Traverse through a circular singly linked list
        O(n)
        """
        if not self.head:
            print("The head reference is None")
            return
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
            if curr == self.tail.next:
                break

    def search(self, value: object) -> bool:
        """
        Search for a specified value in circular singly linked list
        O(n)

        Args:
            value (object): Value to be queried
        Returns:
            bool: True if value is found else False
        """
        if not self.head:
            print("Circular Singly Linked List does not exist")
            return False
        curr = self.head
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
            if curr == self.tail.next:
                break
        return False

    def deleteByIndex(self, index: int):
        """
        Delete a node from the circular singly linked list at a given index
        O(n)

        Args:
            index (int): Index of node to be deleted
        """
        if not self.head:
            print("Circular Singly Linked List does not exist")
            return
        if index == 0:
            if self.head == self.tail:  # i.e. there's only one node
                self.head.next, self.head, self.tail = None, None, None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif index == -1:
            if self.head == self.tail:  # i.e. there's only one node
                self.head.next, self.head, self.tail = None, None, None
            else:
                curr = self.head
                while curr.next is not self.tail:
                    curr = curr.next
                curr.next = self.head
                self.tail = curr
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

    def deleteCircularSinglyLinkedList(self):
        """
        Delete the entire circular singly linked list
        O(1)
        """
        if not self.head:
            print("Singly linked list does not exist")
            return
        self.head, self.tail.next, self.tail = None, None, None


if __name__ == '__main__':
    csll = CircularSinglyLinkedList()
    csll.createCircularSinglyLinkedList(1)
    csll.insert(1, -1)  # insert 1 at tail
    csll.insert(2, -1)  # insert 2 at tail
    csll.insert(3, 0)  # insert 3 at head
    csll.insert(4, 2)  # insert 4 at index 2
    csll.insert(5, 3)  # insert 4 at index 2
    csll.insert(6, 0)  # insert 4 at index 2
    csll.insert(9, -1)  # insert 4 at index 2
    csll.insert(7, 4)  # insert 4 at index 2
    print([node.val for node in csll])
    csll.deleteByIndex(0)
    csll.deleteByIndex(2)
    csll.deleteByIndex(-1)
    print([node.val for node in csll])
    csll.deleteCircularSinglyLinkedList()
    print([node.val for node in csll])
