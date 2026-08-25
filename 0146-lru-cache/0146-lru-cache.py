class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}  # map key to node

        # dummy_head marks the least-recently-used end, dummy_tail marks the most-recently-used end.
        # Neither holds real data, they just give every real node a guaranteed prev/next so we never special-case an empty list.
        self.dummy_head, self.dummy_tail = Node(0, 0), Node(0, 0)
        self.dummy_head.next, self.dummy_tail.prev = self.dummy_tail, self.dummy_head

    def remove(self, node):
        previous_node, next_node = node.prev, node.next
        previous_node.next, next_node.prev = next_node, previous_node

    def insert(self, node):
        # Always insert right before dummy_tail, i.e., the most-recent end.
        previous_node, next_node = self.dummy_tail.prev, self.dummy_tail
        previous_node.next = next_node.prev = node
        node.next, node.prev = next_node, previous_node

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
            self.insert(self.key_to_node[key])
            return self.key_to_node[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
        self.key_to_node[key] = Node(key, value)
        self.insert(self.key_to_node[key])
        if len(self.key_to_node) > self.capacity:
            # The node right after dummy_head is always the
            # least-recently-used real node -- evict it.
            least_recently_used_node = self.dummy_head.next
            self.remove(least_recently_used_node)
            del self.key_to_node[least_recently_used_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""The O(1)-for-both-operations requirement is the whole design constraint here: a hash map alone gives O(1) key lookup but no notion of recency ordering, and a plain array or list gives ordering but O(n) removal/reinsertion from the middle, so I need both simultaneously — a hash map for O(1) 'does this key exist and where is it,' and a doubly linked list for O(1) removal and reinsertion at either end without shifting anything, since a doubly linked list lets me unlink and relink a node using only its own prev/next pointers, no traversal required. I use two dummy nodes marking the least-recently-used and most-recently-used ends so I never have to special-case an empty list or a list with one node when inserting or removing — every real node always has a genuine prev and next to manipulate. Every get that hits an existing key, and every put, moves that key's node to the most-recently-used end by removing and reinserting it, and put additionally evicts the node just after the least-recently-used dummy if capacity is exceeded. I chose hash map + doubly linked list over Python's built-in OrderedDict (which technically solves this in a few lines via move_to_end and popitem) because I assume implementing the mechanism directly is the actual point of this problem in an interview setting, and over a singly linked list because removal from a singly linked list requires knowing the previous node, which would cost O(n) to find without storing extra back-references. This runs in O(1) average time for both get and put, since hash map lookup and doubly linked list insertion/removal are both constant time regardless of cache size, and O(capacity) space for storing at most capacity nodes and their corresponding hash map entries."""