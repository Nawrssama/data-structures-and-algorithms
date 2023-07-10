def left_join(synonyms, antonyms):
    """
    Performs a left join operation on two hash maps, combining the synonyms and antonyms.

    Args:
        synonyms (dict): A hash map with word strings as keys and synonyms as values.
        antonyms (dict): A hash map with word strings as keys and antonyms as values.

    Returns:
        dict: A new hash map with word strings as keys, and tuples of (synonym, antonym) as values.
              If an antonym is missing for a key, the antonym value is None.
    """
    joined_data = {}

    for key in synonyms:
        if key in antonyms:
            joined_data[key] = (synonyms[key], antonyms[key])
        else:
            joined_data[key] = (synonyms[key], None)

    return joined_data

synonyms = {
    "happy": "joyful",
    "sad": "unhappy",
    "big": "large",
    "small": "tiny"
}

antonyms = {
    "happy": "sad",
    "big": "small",
    "rich": "poor"
}

# Perform the left join
result = left_join(synonyms, antonyms)

# Print the result
for key, value in result.items():
    print(f"{key}: {value}")