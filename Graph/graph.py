from collections import deque

class Graph:
    def __init__(self):
        """
        Initializes an empty graph with an empty dictionary to store vertices and their edges.
        """
        self.vertices = {}
        self.size = 0
    
    def add_vertex(self, value):
        """
        Adds a vertex to the graph with the given value.

        Args:
            value: The value of the vertex to be added.

        Returns:
            The added vertex.
        """
        vertex = Vertex(value)
        self.vertices[vertex.value] = []
        self.size += 1
        return vertex
    
    def add_edge(self, vertex1, vertex2, weight=0):
        """
        Adds a new edge between two vertices in the graph.

        Args:
            vertex1: The first vertex to be connected by the edge.
            vertex2: The second vertex to be connected by the edge.
            weight: The weight of the edge (default is None).

        Raises:
            KeyError: If either vertex1 or vertex2 is not present in the graph.
        """
        if not vertex1.value in self.vertices.keys():
            return "vertex does not exist"
        
        if vertex2 is None or not vertex2.value in self.vertices.keys():
            return "vertex does not exist"
        
        edge1 = Edge(vertex2, weight)
        self.vertices[vertex1.value].append(edge1)
        edge2 = Edge(vertex1, weight)
        self.vertices[vertex2.value].append(edge2)
    
    def get_vertices(self):
         """this function is called with no arguments and returns a list of vertices"""
         vertices = []
         for i in self.vertices.keys():
             vertices.append(i)
         return vertices
    
    def get_neighbors(self, vertex):
        """
        Returns a collection of edges connected to the given vertex.

        Args:
            vertex: The vertex to get the neighbors of.

        Returns:
            A collection (list) of edges connected to the given vertex.
        """
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
                result.append(current_vertex.value)  # Append the value of the vertex to the result list

                neighbors = self.get_neighbors(current_vertex)
                for edge in neighbors:
                    neighbor_vertex = edge.vertex
                    if neighbor_vertex not in visited:
                        queue.append(neighbor_vertex)

        return result

    def business_trip(self, cities):
        """
        Calculate the cost of a business trip with direct flights between cities.

        Args:
            cities: A list of city vertices representing the business trip path.

        Returns:
            The total cost of the business trip.
        """
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
    
    def depth_first(self, start_vertex):
        """
        Performs a depth-first search starting from the given start_vertex.

        Args:
            start_vertex: The vertex to start the depth-first search from.

        Returns:
            A collection (list) of vertices in their pre-order depth-first traversal order.
        """
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


# Create a new graph
graph = Graph()

# Add vertices
vertexe1 = graph.add_vertex(1)
vertexe2 = graph.add_vertex(2)
vertexe3 = graph.add_vertex(3)

# Add edges
graph.add_edge(vertexe1, vertexe2, 10)
graph.add_edge(vertexe2, vertexe3, 5)

# Get all vertices
vertices = graph.get_vertices()
print("Vertices:", vertices)

# Get neighbors of a vertex
neighbors = graph.get_neighbors(vertexe2)
print("Neighbors of vertexe2:", neighbors)

# Get the size of the graph
graph_size = graph.get_size()
print("Graph size:", graph_size)

# Perform breadth-first search from vertexe1
bfs_result = graph.breadth_first(vertexe1)
print("BFS Result:", bfs_result)

# Calculate business trip cost
cities = [1, 2, 3]
total_cost = graph.business_trip(cities)
print("Business Trip Cost:", total_cost)

cities = [1, 3]
total_cost = graph.business_trip(cities)
print("Business Trip Cost:", total_cost)

cities = [1, 2, 1]
total_cost = graph.business_trip(cities)
print("Business Trip Cost:", total_cost)

cities = [2, 3, 1]
total_cost = graph.business_trip(cities)
print("Business Trip Cost:", total_cost)

# Perform depth-first search starting from vertexe1
dfs_result = graph.depth_first(vertexe1)
print("DFS Result:", dfs_result)