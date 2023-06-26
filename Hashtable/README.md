# hashtable

## Implement a Hashtable Class with the following methods:

> set

Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.

> get

Arguments: key
Returns: Value associated with that key in the table

> has

Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

> keys

Returns: Collection of keys

> hash
Arguments: key
Returns: Index in the collection for that key

# Solution 

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