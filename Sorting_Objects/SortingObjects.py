movies = [
    {'title': 'The Matrix', 'year': 1999, 'genres': ['Action', 'Sci-Fi']},
    {'title': 'Inception', 'year': 2010, 'genres': ['Action', 'Sci-Fi', 'Thriller']},
    {'title': 'Kimetsu no Yaiba: Mugen Train', 'year': 2020, 'genres': ['Action', 'Fantasy', 'Adventure', 'Supernatural']},
    {'title': 'One Piece: Stampede', 'year': 2019, 'genres': ['Action', 'Adventure', 'Comedy', 'Fantasy']},
    {'title': 'Interstellar', 'year': 2014, 'genres': ['Adventure', 'Drama', 'Sci-Fi', 'Thriller']},
    {'title': 'John Wick: Chapter 4', 'year': 2022, 'genres': ['Action', 'Crime', 'Thriller']},
    {'title': 'The Dark Knight', 'year': 2008, 'genres': ['Action', 'Crime', 'Drama']},
    {'title': 'The Lord of the Rings', 'year': 2001, 'genres': ['Adventure', 'Fantasy']},
]



def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def sort_by_title(movies):
    def remove_leading_articles(title):
        articles = ['A ', 'An ', 'The ']
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    return sorted(movies, key=lambda movie: remove_leading_articles(movie['title']))



# Testing
sorted_by_year = sort_by_year(movies)
print([movie['year'] for movie in sorted_by_year])

sorted_by_title = sort_by_title(movies)
print([movie['title'] for movie in sorted_by_title])