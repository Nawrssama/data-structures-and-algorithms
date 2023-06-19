# Sorting Object

## write Two functions 

> one function for sorting the objects based on years 

> one function for sorting the objects based on names without considring leading article which are (A , An , The)

# Solution 

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