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
    assert vertex4 in vertices

def test_add_edge(graph):
    vertex4 = graph.add_vertex(4)
    vertex5 = graph.add_vertex(5)
    graph.add_edge(vertex4, vertex5, 7)
    neighbors = graph.get_neighbors(vertex4)
    assert len(neighbors) == 1
    assert neighbors[0].vertex2 == vertex5
    assert neighbors[0].weight == 7

# def test_get_vertices(graph):
#     vertices = graph.get_vertices()
#     assert len(vertices) == 3
#     assert vertices == [1, 2, 3]

def test_get_neighbors(graph):
    vertex2 = graph.get_vertices()[1]
    neighbors = graph.get_neighbors(vertex2)
    assert len(neighbors) == 2
    assert neighbors[0].vertex1 == vertex2 or neighbors[0].vertex2 == vertex2
    assert neighbors[1].vertex1 == vertex2 or neighbors[1].vertex2 == vertex2

def test_get_neighbors_with_weight(graph):
    vertex2 = graph.get_vertices()[1]
    neighbors = graph.get_neighbors(vertex2)
    assert neighbors[0].weight == 10 or neighbors[1].weight == 10
    assert neighbors[0].weight == 5 or neighbors[1].weight == 5

def test_size(graph):
    size = graph.size()
    assert size == 3

def test_single_vertex_graph():
    graph = Graph()
    vertex = graph.add_vertex(1)
    vertices = graph.get_vertices()
    assert len(vertices) == 1
    assert vertices[0] == vertex
