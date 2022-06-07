class Stack:
    def __init__(self, capacity):
        """
        Stack is initiated as a python list
        """
        self.stack = []
        self.capacity = capacity

    def __repr__(self) -> str:
        """
        Function to print out the stack
        O(1)

        Returns:
            str: string representation of the class
        """
        return " ".join([str(val) for val in self.stack])

    def push(self, data: object) -> None:
        """
        Function to push data into the stack

        Args:
            data (object): data to be inserted at the top of the stack
        """
        assert (not self.isFull(
        )), "Stack has reached capacity"  # raises assertion if condition is false

        self.stack.append(data)

    def pop(self) -> object:
        """
        Function to return and remove data from the top of the stack
        O(1)

        Returns:
            object: Data to be returned and removed from the top of the stack
        """
        assert not self.isEmpty(), "Stack is empty"
        return self.stack.pop()

    def peek(self) -> object:
        """
        Function to only return data from the top of the stack
        O(1)

        Returns:
            object: Data to be returned from the top of the stack
        """
        assert not self.isEmpty(), "Stack is empty"
        return self.stack[-1]

    def isEmpty(self) -> bool:
        """
        Check whether the stack is empty

        Returns:
            bool: True if stack is empty else False
        """
        return self.stack == []

    def isFull(self) -> bool:
        """
        Check whether the stack has reached max capacity

        Returns:
            bool: True if len(stack) is the max capacity
        """
        return len(self.stack) == self.capacity

    def deleteStack(self) -> None:
        """
        Function to delete the entire stack
        """
        self.stack = []


if __name__ == "__main__":
    stack = Stack(5)
    print(stack.isEmpty())
    print(stack.isFull())
    stack.push(4)
    stack.push(-2)
    stack.push(-2)
    stack.push(10)
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)
    stack.push(1)
    stack.push(10)
    stack.push(12)  # raises an error
