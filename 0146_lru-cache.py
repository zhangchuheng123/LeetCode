class Node(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        self.move_to_tail(self.cache[key])
        return self.cache[key].val

    def put(self, key, value):
        if key in self.cache:
            self.move_to_tail(self.cache[key])
            self.cache[key].val = value
        else:
            node = Node(key, value)
            if len(self.cache) == self.capacity:
                del self.cache[self.head.next.key]
                self.delete_node(self.head.next, do_delete=True)
            self.add_to_tail(node)
            self.cache[key] = node

    def add_to_tail(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node

    def delete_node(self, node, do_delete=False):
        node.prev.next = node.next
        node.next.prev = node.prev
        if do_delete:
            del node

    def move_to_tail(self, node):
        self.delete_node(node)
        self.add_to_tail(node)

if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
