import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        """Return a hash value for a given key."""
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node):
        """Add a node, represented by its identifier, to the ring."""
        for i in range(self.replicas):
            virtual_node_id = f"{node}:{i}"
            key = self._hash(virtual_node_id)
            self.ring[key] = node
            bisect.insort(self.sorted_keys, key)

    def remove_node(self, node):
        """Remove a node and its replicas from the ring."""
        for i in range(self.replicas):
            virtual_node_id = f"{node}:{i}"
            key = self._hash(virtual_node_id)
            self.ring.pop(key, None)
            index = bisect.bisect_left(self.sorted_keys, key)
            if index < len(self.sorted_keys) and self.sorted_keys[index] == key:
                self.sorted_keys.pop(index)

    def get_node(self, key_str):
        """Get the node responsible for the given key."""
        if not self.ring:
            return None
        key = self._hash(key_str)
        print(f"key: {key}, sorted_keys: {self.sorted_keys}")
        index = bisect.bisect(self.sorted_keys, key)
        if index == len(self.sorted_keys):
            index = 0
        return self.ring[self.sorted_keys[index]]

# Example usage:
if __name__ == "__main__":
    nodes = ['node1', 'node2', 'node3']
    ring = ConsistentHashRing(nodes)

    # Assign keys to nodes
    keys = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
    for key in keys:
        node = ring.get_node(key)
        print(f"Key '{key}' is assigned to node '{node}'")
