from collections import deque

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
    
    def breadth_first(self, start_vertex):
        """
        Performs a breadth-first search starting from the given start_vertex.

        Args:
            start_vertex: The vertex to start the breadth-first search from.

        Returns:
            A collection (list) of vertices in the order they were visited.
        """
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


# Create a new graph
graph = Graph()

# Add vertices
vertex1 = graph.add_vertex(1)
vertex2 = graph.add_vertex(2)
vertex3 = graph.add_vertex(3)

# Add edges
graph.add_edge(vertex1, vertex2, 10)
graph.add_edge(vertex2, vertex3, 5)

# Get all vertices
vertices = graph.get_vertices()
print("Vertices:", vertices)

# Get neighbors of a vertex
neighbors = graph.get_neighbors(vertex2)
print("Neighbors of vertex2:", neighbors)

# Get the size of the graph
graph_size = graph.size()
print("Graph size:", graph_size)

# Perform breadth-first search from vertex1
bfs_result = graph.breadth_first(vertex1)
print("BFS Result:", bfs_result)
