"""
HASH MAP (HASH TABLE / DICTIONARY)

A Hash Map is a data structure that stores data in KEY–VALUE pairs.

How it works:
1. A HASH FUNCTION converts the key into an array index.
2. The value is stored at that index.
3. If two keys generate the same index (collision),
   we handle it using CHAINING (a list at each index).

Key Properties:
- Fast insertion, search, and deletion
- Average time complexity: O(1)
- Does not maintain order of elements
"""

class HashMap:
    def __init__(self, size):
        # Total number of buckets
        self.size = size
        
        # Create empty buckets (lists) for chaining
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        Converts a key into a valid index.
        hash(key) → built-in Python hash value
        % size → keeps index within table range
        """
        return hash(key) % self.size

    def put(self, key, value):
        # Get index for the key
        index = self.hash_function(key)

        # Check if key already exists and update value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Insert new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        # Get index for the key
        index = self.hash_function(key)

        # Search for key in the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None  # Key not found

    def remove(self, key):
        # Get index for the key
        index = self.hash_function(key)

        # Remove key-value pair if found
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True

        return False  # Key not found

    def display(self):
        # Display entire hash map
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# ------------------- Example Usage -------------------

# Create Hash Map with 5 buckets
hm = HashMap(5)

# Insert key-value pairs
hm.put("name", "Rahul")
hm.put("age", 22)
hm.put("city", "Mumbai")

# Display Hash Map
hm.display()

# Get value using key
print("Name:", hm.get("name"))

# Remove a key
hm.remove("age")

# Display after removal
hm.display()
