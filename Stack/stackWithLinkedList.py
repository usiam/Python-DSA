class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self) -> ListNode:
        """
        Iterator to iterate over the singly linked list
        O(n)
        """
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        """
        Stack is initiated as a python list
        O(1)
        """
        self.stack = LinkedList()

    def __repr__(self) -> str:
        """
        Function to print out the stack
        O(1)

        Returns:
            str: string representation of the class
        """
        return " ".join([str(node.val) for node in self.stack])

    def push(self, data: object) -> None:
        """
        Function to push data into the stack
        O(1)
        Args:
            data (object): data to be inserted at the top of the stack
        """
        node = ListNode(data)
        node.next = self.stack.head
        self.stack.head = node

    def pop(self) -> object:
        """
        Function to return and remove data from the top of the stack
        O(1)

        Returns:
            object: Data to be returned and removed from the top of the stack
        """
        assert not self.isEmpty(), "Stack is empty"
        retVal = self.stack.head.val
        self.stack.head = self.stack.head.next
        return retVal

    def peek(self) -> object:
        """
        Function to only return data from the top of the stack
        O(1)

        Returns:
            object: Data to be returned from the top of the stack
        """
        assert not self.isEmpty(), "Stack is empty"

        return self.stack.head.val

    def isEmpty(self) -> bool:
        """
        Check whether the stack is empty
        O(1)

        Returns:
            bool: True if stack is empty else False
        """
        return self.stack.head == None

    def deleteStack(self) -> None:
        """
        Function to delete the entire stack
        O(1)
        """
        self.stack.head = None


if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    stack.push(2)
    stack.push(-2)
    stack.push(4)
    stack.push(1)
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)
