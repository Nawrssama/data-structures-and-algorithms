import pytest
from Graph.graph import Graph

@pytest.fixture
def graph():
    # Create a new graph
    graph = Graph()

    # Add vertices
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)

    # Add edges
    graph.add_edge(vertex1, vertex2, 10)
    graph.add_edge(vertex2, vertex3, 5)

    return graph

def test_add_vertex(graph):
    vertex4 = graph.add_vertex(4)
    vertices = graph.get_vertices()
    assert vertex4.value in vertices

def test_add_edge(graph):
    vertex4 = graph.add_vertex(4)
    vertex5 = graph.add_vertex(5)
    graph.add_edge(vertex4, vertex5, 7)
    neighbors = graph.get_neighbors(vertex4)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == 5
    assert neighbors[0].weight == 7

def test_get_vertices(graph):
    vertices = graph.get_vertices()
    assert len(vertices) == 3
    assert vertices == [1, 2, 3]


def test_get_neighbors():
    # Create a new graph
    graph = Graph()

    # Add vertices
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)

    # Add edges
    graph.add_edge(vertex1, vertex2, 10)
    graph.add_edge(vertex2, vertex3, 5)

    # Get neighbors for vertex2
    neighbors = graph.get_neighbors(vertex2)
    
    assert len(neighbors) == 2
    assert (neighbors[0].vertex.value, neighbors[0].weight) == (1, 10)
    assert (neighbors[1].vertex.value, neighbors[1].weight) == (3, 5)


def test_size(graph):
    size = graph.get_size()
    assert size == 3

def test_single_vertex_graph():
    graph = Graph()
    vertex = graph.add_vertex(1)
    vertices = graph.get_vertices()
    assert len(vertices) == 1
    assert vertices[0] == vertex.value

def test_graph_six():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a, b, 2)
    graph.add_edge(a, c, 3)
    graph.add_edge(c, b, 3)
    graph.add_edge(d, b, 4)
    graph.add_edge(d, c, 5)

    actual = [str(vertex) for vertex in graph.breadth_first(a)]
    expected = ['A', 'B', 'C', 'D']
    assert actual == expected

def test_graph_seven():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")

    graph.add_edge(a, b, 2)
    graph.add_edge(a, c, 3)
    graph.add_edge(c, b, 3)
    graph.add_edge(d, b, 4)
    graph.add_edge(d, c, 5)

    actual = [str(vertex) for vertex in graph.breadth_first(a)]
    expected = ['A', 'B', 'C', 'D']
    assert actual == expected

def test_graph_eight():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")

    graph.add_edge(a, b, 2)
    graph.add_edge(a, c, 3)
    graph.add_edge(c, b, 3)
    graph.add_edge(d, b, 4)
    graph.add_edge(d, c, 5)

    actual = [str(vertex) for vertex in graph.breadth_first(e)]
    expected = ['E']
    assert actual == expected

def test_business_trip_with_direct_flights():
    # Create a new graph
    graph = Graph()

    # Add vertices
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)

    # Add edges
    graph.add_edge(vertex1, vertex2, 10)
    graph.add_edge(vertex2, vertex3, 5)

    # Calculate business trip cost
    cities = [1, 2, 3]
    total_cost = graph.business_trip(cities)
    assert total_cost == 15

def test_business_trip_with_missing_flight():
    # Create a new graph
    graph = Graph()

    # Add vertices
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)

    # Add edges
    graph.add_edge(vertex1, vertex2, 10)

    # Calculate business trip cost
    cities = [1, 2, 3]
    total_cost = graph.business_trip(cities)
    assert total_cost is None

def test_business_trip_with_invalid_flight():
    # Create a new graph
    graph = Graph()

    # Add vertices
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)

    # Add edges
    graph.add_edge(vertex1, vertex2, 10)
    graph.add_edge(vertex2, vertex3, 5)

    # Calculate business trip cost
    cities = [1, 2, 4]
    total_cost = graph.business_trip(cities)
    assert total_cost is None

def test_depth_first_empty_graph():
    graph = Graph()
    start_vertex = graph.add_vertex(1)
    result = graph.depth_first(start_vertex)
    assert result == [1]

def test_depth_first_single_vertex_graph():
    graph = Graph()
    start_vertex = graph.add_vertex(1)
    result = graph.depth_first(start_vertex)
    assert result == [1]

def test_depth_first():
    graph = Graph()

    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)
    vertex4 = graph.add_vertex(4)

    graph.add_edge(vertex1, vertex2, 10)
    graph.add_edge(vertex1, vertex3, 5)
    graph.add_edge(vertex2, vertex4, 7)

    result = graph.depth_first(vertex1)
    assert result == [1, 2, 4, 3]