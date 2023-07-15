from Hash_table.hash_table import Hashtable

def is_unique_string(string):
    char_set = set()  # Hashset to store unique characters

    lower_string = string.lower()  # Convert the string to lowercase

    for char in lower_string:
        if char != ' ':
            if char in char_set:
                return False
            char_set.add(char)

    return True

# Example usage
print(is_unique_string("The quick brown fox jumps over the lazy dog"))
print(is_unique_string("I love cats"))
print(is_unique_string("Donald the duck"))