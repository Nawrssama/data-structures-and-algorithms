def DuckDuckGoose(names, k):
    """
    Determines the last person standing in a Duck Duck Goose game.

    Args:
        names (list): A list of strings representing the names of the players.
        k (int): An integer representing the counting interval.

    Returns:
        str: The name of the last person remaining in the game.

    """
    queue = list(names)

    while len(queue) > 1:
        for _ in range(k - 1):
            # Rotate the queue by k - 1 times
            queue.append(queue.pop(0))

        # Remove the person at position k
        queue.pop(0)

    return queue[0]


# Example
names = ["nawrs", "yman", "ayah", "sham", "hisham"]
k = 3
last_person = DuckDuckGoose(names, k)
print("The last person remaining is:", last_person)