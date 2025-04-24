import hashlib
import bisect
from collections import defaultdict

class ConsistentHash:
    def __init__(self, replicas=3):
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []
        self.nodes = set()

    def _hash(self, key):
        """Hash a key using MD5 and convert to an integer."""
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_server(self, server):
        """Add a server with virtual replicas to the hash ring."""
        self.nodes.add(server)
        for i in range(self.replicas):
            virtual_node_key = f"{server}#{i}"
            h = self._hash(virtual_node_key)
            self.ring[h] = server
            bisect.insort(self.sorted_keys, h)

    def remove_server(self, server):
        """Remove a server and all its virtual replicas."""
        self.nodes.discard(server)
        for i in range(self.replicas):
            virtual_node_key = f"{server}#{i}"
            h = self._hash(virtual_node_key)
            del self.ring[h]
            self.sorted_keys.remove(h)

    def get_server(self, key):
        """Get the server for a given request key."""
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect(self.sorted_keys, h)
        if idx == len(self.sorted_keys):
            idx = 0
        return self.ring[self.sorted_keys[idx]]

# ------------------- Example Usage -------------------

if __name__ == "__main__":
    ch = ConsistentHash(replicas=5)

    # Add servers
    ch.add_server("Server-A")
    ch.add_server("Server-B")
    ch.add_server("Server-C")

    # Simulate distributing 10 requests
    request_keys = [f"user:{i}" for i in range(10)]
    distribution = defaultdict(list)

    for key in request_keys:
        server = ch.get_server(key)
        distribution[server].append(key)

    for server, keys in distribution.items():
        print(f"{server} handles requests: {keys}")
