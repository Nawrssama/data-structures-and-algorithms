def business_trip(graph, cities):
    """
    Calculate the cost of a business trip with direct flights between cities.

    Parameters:
        graph (dict): A dictionary representing a graph of cities and their direct flights.
                      
        cities (list): A list of city names in the order of the trip itinerary.

    Returns:
        str or None: If the trip is possible with direct flights, it returns the total cost of
                     the trip as a string with a '$' sign. If there is no direct flight available
                     between any pair of consecutive cities, it returns None.
    """
    total_cost = 0

    for i in range(len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]

        if current_city not in graph :
            return None  
        if next_city not in graph[current_city]:
            return None

        total_cost += graph[current_city][next_city]

    return f"${total_cost}"

# Example given on the CC requirements
graph = {
    "Metroville": { "Pandora": 82, "Arendelle": 99, "New Monstropolis": 105, "Naboo": 26, "Narnia": 37 },
    "Pandora": { "Metroville": 82, "Arendelle": 150 },
    "Arendelle": { "Metroville": 99, "New Monstropolis": 42, "Pandora": 150 },
    "New Monstropolis": { "Arendelle": 42, "Metroville": 105, "Naboo": 73 },
    "Naboo": { "Metroville": 26, "New Monstropolis": 73, "Narnia": 250 },
}

print(business_trip(graph, ["Metroville", "Pandora"]))  # Output: $82
print(business_trip(graph, ["Arendelle", "New Monstropolis", "Naboo"]))  # Output: $115
print(business_trip(graph, ["Naboo", "Pandora"]))  # Output: None
print(business_trip(graph, ["Narnia", "Arendelle", "Naboo"]))  # Output: None
