"""
HASH SET – COMMENT EXPLANATION

A Hash Set is a data structure that stores ONLY UNIQUE values.

It does not store values in key–value pairs; instead, it stores individual
elements.

Each element is passed through a HASH FUNCTION to determine its storage index.

Duplicate values are NOT allowed in a Hash Set.

If multiple elements map to the same index, collisions are handled using
techniques like CHAINING or OPEN ADDRESSING.

Hash Sets are mainly used when fast lookup and uniqueness are required.

Average Time Complexity:
- Add: O(1)
- Search: O(1)
- Remove: O(1)
"""

# HashSet class implementation
class HashSet:
    def __init__(self, size):
        # Size of hash table
        self.size = size
        # Create empty buckets
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        Converts key into an index
        hash() → generates integer
        % size → keeps index in range
        """
        return hash(key) % self.size

    def add(self, key):
        # Get index using hash function
        index = self.hash_function(key)

        # Insert only if key is not already present
        if key not in self.table[index]:
            self.table[index].append(key)

    def contains(self, key):
        # Get index using hash function
        index = self.hash_function(key)

        # Check if key exists
        return key in self.table[index]

    def remove(self, key):
        # Get index using hash function
        index = self.hash_function(key)

        # Remove key if present
        if key in self.table[index]:
            self.table[index].remove(key)

    def display(self):
        # Display hash set
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# ------------------- Example Usage -------------------

# Create Hash Set of size 5
hs = HashSet(5)

# Add elements
hs.add(10)
hs.add(20)
hs.add(15)
hs.add(10)  # Duplicate (ignored)

# Display Hash Set
hs.display()

# Search element
print("Contains 15:", hs.contains(15))

# Remove element
hs.remove(20)

# Display after removal
hs.display()
