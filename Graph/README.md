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

# whiteboard

> breadth first graph

![breadth first graph](./breadth%20first%20graph.jpg)

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


# Solution

    ```
    from collections import deque

    class Graph:
        def __init__(self):
            
            self.vertices = {}
        
        def add_vertex(self, value):
           
            vertex = Vertex(value)
            self.vertices[vertex] = []
            return vertex
        
        def add_edge(self, vertex1, vertex2, weight=None):
            
            if vertex1 in self.vertices and vertex2 in self.vertices:
                edge = Edge(vertex1, vertex2, weight)
                self.vertices[vertex1].append(edge)
                self.vertices[vertex2].append(edge)
            else:
                raise KeyError("Both vertices should already be in the graph.")
        
        def get_vertices(self):
            
            return list(self.vertices.keys())
        
        def get_neighbors(self, vertex):
            
            if vertex in self.vertices:
                return self.vertices[vertex]
            else:
                return []
        
        def size(self):
            
            return len(self.vertices)
        
        def breadth_first(self, start_vertex):
            
            visited = set()
            queue = deque([start_vertex])
            result = []

            while queue:
                current_vertex = queue.popleft()
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    result.append(current_vertex)

                    neighbors = self.get_neighbors(current_vertex)
                    for edge in neighbors:
                        neighbor_vertex = edge.vertex1 if edge.vertex1 != current_vertex else edge.vertex2
                        if neighbor_vertex not in visited:
                            queue.append(neighbor_vertex)

            return result


    class Vertex:
        def __init__(self, value):
            self.value = value
        
        def __repr__(self):
            return str(self.value)
        

    class Edge:
        def __init__(self, vertex1, vertex2, weight=None):
            self.vertex1 = vertex1
            self.vertex2 = vertex2
            self.weight = weight
        
        def __repr__(self):
            if self.weight is not None:
                return f"{self.vertex1} --({self.weight})-- {self.vertex2}"
            else:
                return f"{self.vertex1} -- {self.vertex2}"
    ```

