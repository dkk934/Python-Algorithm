'''HASH MAP (TABLE) – COMMENT EXPLANATION

A Hash Map (also called a Hash Table) is a data structure that stores data in
KEY–VALUE pairs.

Each key is passed through a HASH FUNCTION which converts the key into an
index of an array.

The value is stored at the calculated index.

If two different keys produce the same index, this situation is called a
COLLISION. Collisions are commonly handled using CHAINING, where multiple
key–value pairs are stored in a list at the same index.

Hash Maps provide very fast operations for insertion, searching, and deletion.

Average Time Complexity:
- Insert: O(1)
- Search: O(1)
- Delete: O(1)
'''
# HashTable class implementation
class HashTable:
    def __init__(self, size):
        # Initialize hash table with empty lists (buckets)
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        Converts a key into an index.
        hash() gives an integer hash value,
        modulo (%) ensures index is within table size.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        # Find the index using hash function
        index = self.hash_function(key)

        # Check if key already exists in bucket
        for pair in self.table[index]:
            if pair[0] == key:
                # Update value if key exists
                pair[1] = value
                return

        # If key not found, add new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        # Get index using hash function
        index = self.hash_function(key)

        # Search for key in the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return value if found

        return None  # Key not found

    def delete(self, key):
        # Get index using hash function
        index = self.hash_function(key)

        # Search and remove key-value pair
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True

        return False  # Key not found

    def display(self):
        # Display the hash table
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# ------------------- Example Usage -------------------

# Create hash table of size 5
ht = HashTable(5)

# Insert key-value pairs
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city", "Delhi")

# Display hash table
ht.display()

# Search for a key
print("Search 'name':", ht.search("name"))

# Delete a key
ht.delete("age")

# Display after deletion
ht.display()
