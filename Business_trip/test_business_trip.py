import pytest
from business_trip import business_trip

# Test 1: Va.lid direct flight route
def test_valid_direct_flight():
    graph = {
        "Metroville": { "Pandora": 82, "Arendelle": 99, "New Monstropolis": 105, "Naboo": 26, "Narnia": 37 },
        "Pandora": { "Metroville": 82, "Arendelle": 150 },
        "Arendelle": { "Metroville": 99, "New Monstropolis": 42, "Pandora": 150 },
        "New Monstropolis": { "Arendelle": 42, "Metroville": 105, "Naboo": 73 },
        "Naboo": { "Metroville": 26, "New Monstropolis": 73, "Narnia": 250 },
    }
    cities = ["Metroville", "Pandora"]
    assert business_trip(graph, cities) == "$82"

# Test 2: Valid direct flight route with multiple cities
def test_valid_direct_flight_multiple_cities():
    graph = {
        "Metroville": { "Pandora": 82, "Arendelle": 99, "New Monstropolis": 105, "Naboo": 26, "Narnia": 37 },
        "Pandora": { "Metroville": 82, "Arendelle": 150 },
        "Arendelle": { "Metroville": 99, "New Monstropolis": 42, "Pandora": 150 },
        "New Monstropolis": { "Arendelle": 42, "Metroville": 105, "Naboo": 73 },
        "Naboo": { "Metroville": 26, "New Monstropolis": 73, "Narnia": 250 },
    }
    cities = ["Metroville", "Pandora", "Arendelle", "New Monstropolis"]
    assert business_trip(graph, cities) == "$274"

# Test 3: Invalid route with no direct flight
def test_no_direct_flight():
    graph = {
        "Metroville": { "Pandora": 82, "Arendelle": 99, "New Monstropolis": 105, "Naboo": 26, "Narnia": 37 },
        "Pandora": { "Metroville": 82, "Arendelle": 150 },
        "Arendelle": { "Metroville": 99, "New Monstropolis": 42, "Pandora": 150 },
        "New Monstropolis": { "Arendelle": 42, "Metroville": 105, "Naboo": 73 },
        "Naboo": { "Metroville": 26, "New Monstropolis": 73, "Narnia": 250 },
    }
    cities = ["Naboo", "Pandora"]
    assert business_trip(graph, cities) is None