# Graph 

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

>add vertex


```Arguments: value

Returns: The added vertex

Add a vertex to the graph
```

>add edge



```Arguments: 2 vertices to be connected by the edge, weight (optional)

Returns: nothing

Adds a new edge between two vertices in the graph

If specified, assign a weight to the edge

Both vertices should already be in the Graph
```

>get vertices


```Arguments: none

Returns all of the vertices in the graph as a collection (set, list, or similar)

Empty collection returned if there are no vertices
```

>get neighbors


```Arguments: vertex

Returns a collection of edges connected to the given vertex

Include the weight of the connection in the returned collection

Empty collection returned if there are no vertices
```

>size


```Arguments: none

Returns the total number of vertices in the graph

0 if there are none
```

>breadth first


```Write the following method for the Graph class:

breadth first
Arguments: Node
Return: A collection of nodes in the order they were visited.
Display the collection
```

>bisness trip


```Write a function called business trip
Arguments: graph, array of city names
Return: the cost of the trip (if it’s possible) or null (if not)
Determine whether the trip is possible with direct flights, and how much it would cost.
```

# whiteboard

> breadth first graph

![breadth first graph](./breadth%20first.jpg)

> business trip 

![business trip  graph](./business%20trip.jpg)

> depth first

![depth first graph](./depth%20first.jpg)

# Approach & Efficiency


>add vertex

Time Complexity: O(1)
Space Complexity: O(1)

>add edge

Time Complexity: O(1)
Space Complexity: O(1)

>get vertices

Time Complexity: O(n)
Space Complexity: O(n)

>get neighbors

Time Complexity: O(n)
Space Complexity: O(n)

>size

Time Complexity: O(1)
Space Complexity: O(1)

>breadth first

Time Complexity: O(n)
Space Complexity: O(n)

>business trip 

Time Complexity: O(n*m)
Space Complexity: O(1)

>depth first

Time Complexity: O(n+m)
Space Complexity: O(n)


# Solution

    ```
    class Graph:
        def __init__(self):
            
            self.vertices = {}
            self.size = 0
        
        def add_vertex(self, value):
            
            vertex = Vertex(value)
            self.vertices[vertex.value] = []
            self.size += 1
            return vertex
        
        def add_edge(self, vertex1, vertex2, weight=0):
            
            if not vertex1.value in self.vertices.keys():
                return "vertex does not exist"
            
            if vertex2 is None or not vertex2.value in self.vertices.keys():
                return "vertex does not exist"
            
            edge1 = Edge(vertex2, weight)
            self.vertices[vertex1.value].append(edge1)
            edge2 = Edge(vertex1, weight)
            self.vertices[vertex2.value].append(edge2)
        
        def get_vertices(self):
           
            vertices = []
            for i in self.vertices.keys():
                vertices.append(i)
            return vertices
        
        def get_neighbors(self, vertex):
           
            vertex_value = vertex.value
            return self.vertices[vertex_value]
        
        def get_size(self):
            """
            Returns the total number of vertices in the graph.
            """
            return len(self.vertices)
        
        def __str__(self):
            output = ''
            for vertex in self.adj_list.keys():
                output += f'{vertex} -> '
                for edge in self.adj_list[vertex]:
                    
                    output += f'{edge.value} -----> '
                output += '\n'
            return output
        
        def breadth_first(self, start_vertex):
            
            visited = set()
            queue = deque([start_vertex])
            result = []

            while queue:
                current_vertex = queue.popleft()
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    result.append(current_vertex.value)  # Append the value of the vertex to the result list

                    neighbors = self.get_neighbors(current_vertex)
                    for edge in neighbors:
                        neighbor_vertex = edge.vertex
                        if neighbor_vertex not in visited:
                            queue.append(neighbor_vertex)

            return result

        def business_trip(self, cities):
           
            total_cost = 0

            for i in range(len(cities) - 1):
                current_city = cities[i]
                next_city = cities[i + 1]

                neighbors = self.vertices[current_city]
                found_direct_flight = False
                for edge in neighbors:
                    if edge.vertex.value == next_city:
                        total_cost += edge.weight
                        found_direct_flight = True
                        break

                if not found_direct_flight:
                    return None

            return total_cost
        
        def dfs_recursive(current_vertex, visited, result):
            visited.add(current_vertex)
            result.append(current_vertex.value)

            for neighbor_edge in self.vertices[current_vertex.value]:
                neighbor_vertex = neighbor_edge.vertex
                if neighbor_vertex not in visited:
                    dfs_recursive(neighbor_vertex, visited, result)

            visited = set()
            result = []
            dfs_recursive(start_vertex, visited, result)
            return result
        
        
        
    class Vertex:
        def __init__(self, value):
            self.value = value
            self.weight = None
            self.next = []

        def __repr__(self):
            return str(self.value)

    class Edge:
        def __init__(self, vertex, weight=0):
            self.value = vertex.value
            self.vertex = vertex
            self.weight = weight

        def __repr__(self):
            if self.weight is not None:
                return f"{self.vertex} --({self.weight})-- {self.value}"
            else:
                return f"{self.vertex} -- {self.value}"
    ```
