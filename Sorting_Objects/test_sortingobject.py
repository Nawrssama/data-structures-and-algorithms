import pytest
from Sorting_Objects.SortingObjects import sort_by_title, sort_by_year


def test_sort_by_year():
    movies = [
        {'title': 'The Matrix', 'year': 1999},
        {'title': 'Inception', 'year': 2010},
        {'title': 'A Clockwork Orange', 'year': 1971},
    ]

    sorted_movies = sort_by_year(movies)

    assert sorted_movies[0]['title'] == 'Inception'
    assert sorted_movies[1]['title'] == 'The Matrix'
    assert sorted_movies[2]['title'] == 'A Clockwork Orange'

def test_sort_by_year_empty_list():
    movies = []

    sorted_movies = sort_by_year(movies)

    assert sorted_movies == []

def test_sort_by_title():
    movies = [
        {'title': 'The Matrix', 'year': 1999},
        {'title': 'Inception', 'year': 2010},
        {'title': 'A Clockwork Orange', 'year': 1971},
    ]

    sorted_movies = sort_by_title(movies)

    assert sorted_movies[0]['title'] == 'A Clockwork Orange'
    assert sorted_movies[1]['title'] == 'Inception'
    assert sorted_movies[2]['title'] == 'The Matrix'

def test_sort_by_title_with_leading_articles():
    movies = [
        {'title': 'The Dark Knight', 'year': 2008},
        {'title': 'An Inconvenient Truth', 'year': 2006},
        {'title': 'A Beautiful Mind', 'year': 2001},
    ]

    sorted_movies = sort_by_title(movies)

    assert sorted_movies[0]['title'] == 'A Beautiful Mind'
    assert sorted_movies[1]['title'] == 'The Dark Knight'
    assert sorted_movies[2]['title'] == 'An Inconvenient Truth'