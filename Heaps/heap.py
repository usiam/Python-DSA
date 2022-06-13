class Heap:
    def __init__(self, capacity: int):
        """
        Initializes the heap data structure using a list implementation

        O(1)
        Args:
            capacity (int): Maximum size of the heap
        """
        self.heap = [
            None] * (capacity + 1)  # +1 because 0-th index is empty always for ease of access
        self.capacity = capacity
        self.heapSize = 0

    def peek(self):
        """
        Returns the top of the heap
        O(1)
        """
        return self.heap[1] if self.heap else None

    def heapsize(self):
        """
        Returns the length of the heap
        O(1)
        """
        return self.heapSize if self.heap else None

    def levelOrderTraversal(self):
        """
        Traverses the heap by level

        O(n) 
        """
        if not self.heap:
            return
        for i in range(1, self.heapSize + 1):
            print(self.heap[i])

    def heapifyOnInsert(self, index: int, heapType: str):
        """
        Helper method to ensure that the 2nd property (The root must be no less or no more than its children depending on the heap type) of the heap is conserved on insertion.

        O(logn)
        Args:
            index (int): The index of the current node
            heapType (str): Max or Min heap
        """
        if index <= 1:
            return

        parentIndex = index // 2
        if heapType.lower() == 'min':
            if self.heap[index] < self.heap[parentIndex]:
                self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            self.heapifyOnInsert(parentIndex, heapType)
            # can also be done iteratively using a while loop
        if heapType.lower() == 'max':
            if self.heap[index] > self.heap[parentIndex]:
                self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            self.heapifyOnInsert(parentIndex, heapType)

    def insert(self, val, heapType):
        """
        Insert into heap

        Args:
            val (_type_): _description_
            heapType (_type_): _description_
        """
        assert not self.heapSize + 1 > self.capacity, "Heap is full"
        self.heap[self.heapSize + 1] = val
        self.heapSize += 1
        self.heapifyOnInsert(self.heapSize, heapType)
        return "Value inserted into heap"

    def heapifyOnPop(self, index, heapType):
        """
        Helper method to ensure that the 2nd property (The root must be no less or no more than its children depending on the heap type) of the heap is conserved on popping.

        O(logn)
        Args:
            index (int): The index of the current node
            heapType (str): Max or Min heap
        """
        leftChildIndex, rightChildIndex = 2 * index, 2 * index + 1
        swapChildIndex = 0
        if self.heapSize < leftChildIndex:
            # this checks whether there is a child or not
            # we do a check on leftChildIndex because heaps are COMPLETE binary trees meaning
            # elements are filled top to bottom and left to right
            return
        elif self.heapSize == leftChildIndex:
            # only left child exist
            if heapType.lower() == 'min':
                if self.heap[index] > self.heap[leftChildIndex]:
                    self.heap[index], self.heap[leftChildIndex] = self.heap[leftChildIndex], self.heap[index]
                return
            else:
                if self.heap[index] < self.heap[leftChildIndex]:
                    self.heap[index], self.heap[leftChildIndex] = self.heap[leftChildIndex], self.heap[index]
                return
        else:  # both children exist
            if heapType.lower() == 'min':
                if self.heap[leftChildIndex] < self.heap[rightChildIndex]:
                    swapChildIndex = leftChildIndex
                else:
                    swapChildIndex = rightChildIndex
                if self.heap[index] > self.heap[swapChildIndex]:
                    self.heap[index], self.heap[swapChildIndex] = self.heap[swapChildIndex], self.heap[index]
            else:  # type is max
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    swapChildIndex = leftChildIndex
                else:
                    swapChildIndex = rightChildIndex
                if self.heap[index] < self.heap[swapChildIndex]:
                    self.heap[index], self.heap[swapChildIndex] = self.heap[swapChildIndex], self.heap[index]
        self.heapifyOnPop(swapChildIndex, heapType)

    def pop(self, heapType):
        """
        Pops the root of the heap

        Args:
            heapType (_type_): Max or Min heap
        """
        assert not self.heapSize + 1 > self.capacity, "Heap is full"
        # save the pop value
        popVal = self.heap[1]
        # set root value to be the last value in heap
        self.heap[1] = self.heap[self.heapSize]
        self.heap[self.heapSize] = None
        self.heapSize -= 1
        self.heapifyOnPop(1, heapType)
        return popVal

    def clear(self):
        """
        Deletes the heap

        O(1)
        """
        self.heap = None


if __name__ == '__main__':
    heap = Heap(7)
    print(heap.heapsize())
    print(heap.levelOrderTraversal())
    print("\nInserting into heap")
    print(heap.insert(4, "max"))
    print(heap.insert(1, "max"))
    print(heap.insert(3, "max"))
    print(heap.insert(15, "Max"))
    print(heap.insert(6, "max"))
    print(heap.insert(18, "max"))

    print(heap.levelOrderTraversal())

    print(f"Top value in the heap is: {heap.pop('Max')}")
    print(heap.levelOrderTraversal())
