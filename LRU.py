class LinkedListNode:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, key, value):
        if self.head is None and self.tail is None:
            add = LinkedListNode(key, value, None, None)
            self.head = add
            self.tail = add
        else:
            add = LinkedListNode(key, value, None, self.head)
            self.head.set_left(add)
            self.head = add
        return self.head

    def remove_back(self):
        if self.head is None and self.tail is None:
            # cannot remove from an empty list
            return None
        
        buffer = self.tail
        if self.tail.get_left() == None:
            # only one item in the list
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_left()
            self.tail.set_right(None)
        return buffer
        

    def renew(self, node):
        # cut node out of current position
        left = node.get_left()
        right = node.get_right()
        if left is not None:
            left.set_right(right)
        if right is not None:
            right.set_left(left)

        # splice node into front of queue
        self.head.set_left(node)
        node.set_left(None)
        node.set_right(self.head)
        self.head = node

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.get_right()


class LRU:
    def __init__(self, max_size):
        self.lookup = {}
        self.queue = LinkedList()
        self.size = 0
        self.max_size = max_size

    def memo(self, key, value):
        if key in self.lookup:
            node = self.lookup[key]
            node.set_value(value)
            self.queue.renew(node)
        else:
            node = self.queue.add_front(key, value)
            self.lookup[key] = node

            if self.size == self.max_size:
                removed = self.queue.remove_back()
                del self.lookup[removed.get_key()]
            else:
                self.size += 1

    def get(self, key):
        return self.lookup[key] if key in self.lookup else None

    def __repr__(self):
        return "\n".join(
            [
                f"[index={i}, key={node.get_key()}, value={node.get_value()}]"
                for (i, node) in enumerate(self.queue)
            ]
        )
