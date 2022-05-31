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


class SinglyLinkedList:
    def __init__(self):
        """
        Constructor for a singly linked list
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
            node = node.next

    def insert(self, value: object, index: int) -> None:
        """
        Insert a node in the singly linked list        
        O(n)

        Args:
            value (_type_): Value to be stored in the new list node
            index (int): location of the new list node
        """
        node = ListNode(value)
        # If linked list has no node
        if not self.head or not self.tail:
            self.head = node
            self.tail = node

        # insert at head
        elif index == 0:
            node.next = self.head
            self.head = node

        # insert at tail
        elif index == -1:
            node.next = None
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

            if curr == self.tail:
                self.tail = node

    def traverse(self) -> None:
        """
        Traverse through a singly linked list
        O(n)
        """
        if not self.head:
            print("Singly Linked List does not exist")
            return
        curr = self.head
        while curr:
            # do something
            print(curr.val, end=" ")
            # update curr
            curr = curr.next
        print("(End of Singly Linked List reached)")
        return

    def search(self, value: object) -> bool:
        """
        Search for a specified value in singly linked list
        O(n)

        Args:
            value (object): Value to be queried
        Returns:
            bool: True if value is found else False
        """
        if not self.head:
            print("Singly Linked List does not exist")
            return False
        curr = self.head
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False

    def deleteByIndex(self, index: int):
        """
        Delete a node from the singly linked list at a given index
        O(n)

        Args:
            index (int): Index of node to be deleted
        """
        if not self.head:
            print("Singly Linked List does not exist")
            return
        if index == 0:
            if self.head == self.tail:  # i.e. there's only one node
                self.head, self.tail = None, None
            else:
                self.head = self.head.next
        elif index == -1:
            if self.head == self.tail:  # i.e. there's only one node
                self.head, self.tail = None, None
            else:
                curr = self.head
                while curr.next is not self.tail:
                    curr = curr.next
                curr.next = None
                self.tail = curr
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

    def deleteByValue(self, value: object) -> ListNode:
        """
        Delete a node from the singly linked list with a given value
        O(n)

        Args:
            value (object): Value of node to be deleted

        Returns:
            ListNode: Returns the singly linked list with the values removed
        """
        if not self.head:
            print("Singly Linked List does not exist")
            return

        dummy = ListNode(0)
        dummy.next = self.head
        prev = dummy
        curr = self.head
        while curr:
            if curr.val == value:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

    def deleteSinglyLinkedList(self):
        """
        Delete the entire singly linked list
        O(1)
        """
        if not self.head:
            print("Singly linked list does not exist")
            return
        self.head, self.tail = None, None


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert(1, -1)  # insert 1 at tail
    sll.insert(2, -1)  # insert 2 at tail
    sll.insert(3, 0)  # insert 3 at head
    sll.insert(4, 2)  # insert 4 at index 2
    sll.insert(5, 3)  # insert 4 at index 2
    sll.insert(6, 0)  # insert 4 at index 2
    sll.insert(9, -1)  # insert 4 at index 2
    sll.insert(7, 4)  # insert 4 at index 2
    print([node.val for node in sll])
    sll.deleteByIndex(0)
    sll.deleteByIndex(-1)
    sll.deleteByIndex(1)
    print(f"{sll.tail.val} is the tail value")
    sll.deleteByValue(2)
    sll.deleteByValue(5)
    print([node.val for node in sll])
    sll.traverse()
    print(f"{sll.tail.val} is the tail value and {sll.head.val} is the head value.")
