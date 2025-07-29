class Node:
    """A single node in a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    """A basic singly linked list with head pointer."""
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        """Insert a new node with value at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node with value at the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_after(self, target_value, value):
        """
        Insert a new node with value immediately after
        the first node whose value is target_value.
        """
        curr = self.head
        while curr and curr.value != target_value:
            curr = curr.next
        if not curr:
            raise ValueError(f"Value {target_value} not found in list.")
        new_node = Node(value)
        new_node.next = curr.next
        curr.next = new_node

    def delete_by_value(self, value):
        """Delete the first node found with the given value."""
        curr = self.head
        prev = None
        while curr and curr.value != value:
            prev = curr
            curr = curr.next
        if not curr:
            raise ValueError(f"Value {value} not found in list.")
        if prev:
            prev.next = curr.next
        else:
            # deleting the head
            self.head = curr.next

    def delete_at_position(self, position):
        """
        Delete the node at zero-based index position.
        Raises IndexError if position is out of bounds.
        """
        if position < 0:
            raise IndexError("Position must be non-negative.")
        curr = self.head
        prev = None
        idx = 0
        while curr and idx < position:
            prev = curr
            curr = curr.next
            idx += 1
        if not curr:
            raise IndexError("Position out of bounds.")
        if prev:
            prev.next = curr.next
        else:
            # deleting the head
            self.head = curr.next

    def traverse(self):
        """Traverse the list, yielding each node’s value."""
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __iter__(self):
        return self.traverse()

    def __repr__(self):
        values = list(self.traverse())
        return "SinglyLinkedList([" + " → ".join(map(str, values)) + "])"

# Create an empty list
lst = LinkedList()

# Insert some elements
lst.insert_at_head(3)    # 3
lst.insert_at_head(2)    # 2 → 3
lst.insert_at_tail(4)    # 2 → 3 → 4
lst.insert_after(3, 3.5) # 2 → 3 → 3.5 → 4
print(lst)               # SinglyLinkedList([2 → 3 → 3.5 → 4])

# Delete by value
lst.delete_by_value(3.5) # 2 → 3 → 4
print(lst)               # SinglyLinkedList([2 → 3 → 4])

# Delete by position
lst.delete_at_position(0)  # removes 2
print(lst)                 # SinglyLinkedList([3 → 4])

# Traverse / iterate
for value in lst:
    print(value)           # prints 3 then 4
