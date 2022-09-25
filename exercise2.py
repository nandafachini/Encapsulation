# Implement the Movie class, as shown in the class diagram below
#   a) All attributes must be private
#   b) Create get and set methods for all attributes

# In your main program, do the following implementation:
#   * Create an empty movie list
#   * Register 3 films (with the data provided by the user)
#   * Store the objects in the movie list
#   * Scroll through the list of films and print the data of all 
#     registered films on the terminal

# ----------------------
# | Movie              |
# ----------------------
# | title: str         |
# | genre: str         |
# ----------------------
# | get_title()        |
# | get_genre()        |
# | set_title(title)   |
# | set_genre(genre)   |
# ----------------------


class Movie:
    # private attributes
    def __init__(self, title, genre):
        self.__title = title
        self.__genre = genre

    # get methods
    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    # set methods
    def set_title(self,title):
        self.__title = title
        return self.__title

    def set_genre(self,genre):
        self.__genre = genre
        return self.__genre

movies = []
movie1 = Movie("The love is beatiful", "Romance")
movies.append(movie1)

movie2 = Movie("Die hard", "Action")
movies.append(movie2)

movie3 = Movie("Good day Veronica","Thriller")
movies.append(movie3)

for x in movies:
    print("Name of the movie: " , x.get_title(), "-" , "Movie genre: " , x.get_genre())
