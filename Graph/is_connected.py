from Graph.graph import Graph

def is_connected(graph:Graph, start_vertex, target_vertex):
    """
    Checks if there is a path between the start_vertex and the target_vertex in the given graph.

    Args:
        graph: The Graph object.
        start_vertex: The vertex to start the traversal from.
        target_vertex: The vertex we want to find a path to.

    Returns:
        True if there is a path between the start_vertex and the target_vertex, False otherwise.
    """
    stack = [start_vertex]
    visited = set()

    while stack:
        current_vertex = stack.pop()
        if current_vertex == target_vertex:
            return True

        if current_vertex not in visited:
            visited.add(current_vertex)

            neighbors = graph.vertices[current_vertex.value]
            for neighbor_edge in neighbors:
                neighbor_vertex = neighbor_edge.vertex
                if neighbor_vertex not in visited:
                    stack.append(neighbor_vertex)

    return False


# Create a new graph
graph = Graph()

# Add vertices
vertex_a = graph.add_vertex('A')
vertex_b = graph.add_vertex('B')
vertex_c = graph.add_vertex('C')
vertex_d = graph.add_vertex('D')
vertex_e = graph.add_vertex('E')

# Add edges
graph.add_edge(vertex_a, vertex_b)
graph.add_edge(vertex_a, vertex_c)
graph.add_edge(vertex_b, vertex_d)
graph.add_edge(vertex_c, vertex_d)
graph.add_edge(vertex_d, vertex_e)

# Test the is_connected function
start_vertex = vertex_a
target_vertex = vertex_e
result = is_connected(graph, start_vertex, target_vertex)
print("Is Node A connected to Node E?", result)  # Output: True

start_vertex = vertex_b
target_vertex = vertex_e
result = is_connected(graph, start_vertex, target_vertex)
print("Is Node B connected to Node E?", result)  # Output: True

start_vertex = vertex_d
target_vertex = vertex_a
result = is_connected(graph, start_vertex, target_vertex)
print("Is Node D connected to Node A?", result)  # Output: False