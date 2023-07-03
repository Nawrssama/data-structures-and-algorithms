def repeated_word(s):
    """
    Find the first word that occurs more than once in a given string.

    Arguments:
    s (str)

    Returns:
    str or None
    """
    words = s.lower().split()
    word_count = {}

    for word in words:
        word = word.strip(".,!?")

        if word in word_count:
            return word
        else:
            word_count[word] = 1

    return None

input_string = "This is a test string to test the function."
print(repeated_word(input_string))