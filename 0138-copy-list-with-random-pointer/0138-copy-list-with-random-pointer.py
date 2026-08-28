"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {None: None}
        current_node = head

        while current_node:
            copy_node = Node(current_node.val)
            original_to_copy[current_node] = copy_node
            current_node = current_node.next

        current_node = head
        while current_node:
            copy_node = original_to_copy[current_node]
            copy_node.next = original_to_copy[current_node.next]
            copy_node.random = original_to_copy[current_node.random]
            current_node = current_node.next

        return original_to_copy[head]


"""Let me first make sure I understand the problem: I've got a linked list where each node has a normal next pointer plus a random pointer that can point anywhere in the list or to null, and I need to build a totally separate deep copy that preserves both sets of pointers. The key thing I notice is that whenever I copy a node, its random pointer might point to something I haven't created yet, so I need a way to look up "what's the copy of this original node" regardless of order. That makes me think a hash map is the right tool, since it gives me constant time lookups between an old node and its new counterpart as I build things up. So my approach is two passes: first, I walk the list once and just create a new node for every original node, storing old-to-new in the map as I go, including mapping None to None so I don't have to special-case null later. Then, in a second pass, I go through the original list again, and for each node I grab its copy and set copy.next and copy.random by looking up the original's next and random in the map — since every node's already in there by this point, it doesn't matter if the pointer goes forward or backward. The reason I split it into two passes is exactly to avoid that problem of needing a node's copy before it exists. At the end I just return the map's entry for head. Time complexity is O(n) since it's two linear passes, and space is O(n) for the hash map.

The core difficulty here is that random pointers can point forward to nodes I haven't created copies of yet during a single pass, so if I try to wire up next and random while creating nodes in one traversal, I'll sometimes need to reference a copy that doesn't exist yet — the fix is to separate 'creating all the copies' from 'wiring their pointers' into two distinct passes, using a hash map from original node to its copy as the bridge between them, so by the time I wire pointers in the second pass, every copy I could possibly need already exists in the map. I seed the map with None: None specifically so that when a node's next or random is null, the lookup still resolves cleanly to None instead of requiring a separate null-check at every pointer assignment. I chose the two-pass hash map approach over the O(1)-extra-space interleaving trick (splicing each copy node directly after its original, using the interwoven structure itself to resolve random pointers without a map, then unweaving at the end) because the hash map version is far more readable and less error-prone to get right under interview pressure, though I'd name the interleaving trick as the follow-up answer if asked to reduce space complexity. This runs in O(n) time, since each of the two passes visits every node exactly once, and O(n) space for the hash map storing one entry per original node."""