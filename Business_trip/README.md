# business trip

```
Write a function called business trip

Arguments: graph, array of city names

Return: the cost of the trip (if it’s possible) or null (if not)
```

# Approach & Efficiency

> Time ==> O(n)

> space ==> O(n)

# white-board

## business trip
![ business trip ](./business%20trip.jpg)

# Solution 

    def business_trip(graph, cities):
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