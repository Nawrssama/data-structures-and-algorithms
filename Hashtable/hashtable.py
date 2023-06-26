class Hashtable:
    def __init__(self):
        """
        Initializes a Hashtable with an initial size and an empty table.
        """
        self.size = 10  # Initial size of the hashtable
        self.table = [[] for _ in range(self.size)]  # List of empty buckets

    def set(self, key, value):
        """
        Sets the key-value pair in the hashtable, handling collisions as needed.
        """
        index = self.hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value  # If key already exists, replace the value
                return
        self.table[index].append([key, value])  # Add new key-value pair

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hashtable.
        """
        index = self.hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]  # Return the value associated with the key
        return None  # Key not found

    def has(self, key):
        """
        Checks if the given key exists in the hashtable.
        """
        index = self.hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return True  # Key found
        return False  # Key not found

    def keys(self):
        """
        Returns a collection of keys present in the hashtable.
        """
        keys = []
        for bucket in self.table:
            for entry in bucket:
                keys.append(entry[0])  # Append keys from all entries
        return keys

    def hash(self, key):
        """
        Hashes the given key to calculate the index in the hashtable.
        """
        index = 0
        for char in str(key):
            index += ord(char)
        return index % self.size
    

ht = Hashtable()
ht.set('apple', 5)
ht.set('banana', 7)
ht.set('cherry', 3)

print(ht.get('banana'))  # Output: 7
print(ht.has('apple'))  # Output: True
print(ht.has('grape'))  # Output: False
print(ht.keys())  # Output: ['apple', 'banana', 'cherry']