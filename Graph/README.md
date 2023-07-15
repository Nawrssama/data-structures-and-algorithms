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


# Solution

    ```
    class Graph:
        def __init__(self):
            """
            Initializes an empty graph with an empty dictionary to store vertices and their edges.
            """
            self.vertices = {}
        
        def add_vertex(self, value):
            """
            Adds a vertex to the graph with the given value.

            Args:
                value: The value of the vertex to be added.

            Returns:
                The added vertex.
            """
            vertex = Vertex(value)
            self.vertices[vertex] = []
            return vertex
        
        def add_edge(self, vertex1, vertex2, weight=None):
            """
            Adds a new edge between two vertices in the graph.

            Args:
                vertex1: The first vertex to be connected by the edge.
                vertex2: The second vertex to be connected by the edge.
                weight: The weight of the edge (default is None).

            Raises:
                KeyError: If either vertex1 or vertex2 is not present in the graph.
            """
            if vertex1 in self.vertices and vertex2 in self.vertices:
                edge = Edge(vertex1, vertex2, weight)
                self.vertices[vertex1].append(edge)
                self.vertices[vertex2].append(edge)
            else:
                raise KeyError("Both vertices should already be in the graph.")
        
        def get_vertices(self):
            """
            Returns all of the vertices in the graph.

            Returns:
                A collection (list) of all vertices in the graph.
            """
            return list(self.vertices.keys())
        
        def get_neighbors(self, vertex):
            """
            Returns a collection of edges connected to the given vertex.

            Args:
                vertex: The vertex to get the neighbors of.

            Returns:
                A collection (list) of edges connected to the given vertex.
            """
            if vertex in self.vertices:
                return self.vertices[vertex]
            else:
                return []
        
        def size(self):
            """
            Returns the total number of vertices in the graph.
            """
            return len(self.vertices)


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

