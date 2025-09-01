# Task: Movie Rental System 🎬

# Requirements:
# Create a class Movie, which has:
## title – the movie title,
# director – the director,
# is_rented – a boolean flag (default False) indicating whether the movie is rented.
## Add a __str__ method, which should return the description of the movie in the form:
# # "🎞️ Rented: 'Inception' - Christopher Nolan"
# "📀 Available: 'The Matrix' - Wachowski Brothers".
## Create a class MovieRental, which has:
## an internal list of movies,
## method add_movie(movie) – adds a movie to the rental store,
## method rent_movie(title) – sets is_rented=True for the movie with the given title (if available),
## method return_movie(title) – sets is_rented=False (the movie is returned),
## method show_movies() – displays all movies in a readable format.
## Handle edge cases:
## If you try to rent a movie that doesn’t exist → ValueError("No such movie in the rental store"),
## If the movie is already rented → ValueError("The movie is already rented").
## 👉 This task works exactly the same way as the Library/Book example, just in the world of movies 🎬.
# This way you will practice:
## the __init__ constructor,
# instance attributes,
# instance methods,
# validation,
# __str__.


class Movie:
    def __init__(self, title, director, is_rented=False):
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def __str__(self):
        if self.is_rented is False:
            return f"Rental status: {self.is_rented}-  {self.title} - {self.director}"
        elif self.is_rented is True:
            return f"Rental Status: {self.is_rented}-  {self.title} - {self.director}"
        else:
            return f" {self.title} from  {self.director} is unavailable"


class MovieRental:

    def __init__(self):
        """will create an instance of list, so that in future if mulitple lists will be required,we can manage those"""
        self.list_of_movies = []

    def add_movie(self, movie):
        """film is added to the move library"""
        self.list_of_movies.append(movie)
        # print('Method "show_movies" will be called in a sec')
        # self.show_movies()
        # print('Method "show_movies" was executed')

    # Operator 'is', checks if two objects point to the exact memory

    def check_film_in_records(self, title):
        if isinstance(title, Movie): #check if the title/film is an instance of MOvie class
            film_on_shelf = next(
                (film for film in self.list_of_movies if film == title), None
            )
            # print("Recognizing object as  instance of Movie class")
            if film_on_shelf is None:
                # print("Film not recognized")
                return None
            else:
                return film_on_shelf

        else: # to manage a situation in case the title is received as string 
            film_on_shelf = next(
                (film for film in self.list_of_movies if film.title == title), None
            )
            if not film_on_shelf:
                return None
            else:
                return film_on_shelf

    def rent_movie(self, title):
        film_on_shelf = self.check_film_in_records(title)

        if film_on_shelf is None:
            raise ValueError (f'Movie with title: "{title}" is unavailable in our records')

        elif not film_on_shelf.is_rented:  # checks if the flag is set to False
            print(f'{film_on_shelf.is_rented}')
            film_on_shelf.is_rented = True
            print(f"\nFilm {title} was just rented")
            self.show_movies()

        elif film_on_shelf.is_rented:
            print(f'{film_on_shelf.is_rented}')
            raise ValueError (f'Film "{title}" is already rented')
            


    def return_movie(self,title):
        film_on_shelf = self.check_film_in_records(title)

        if film_on_shelf is None:
            print(f"Movie with title: {title} is unavailable in our records ")
            raise IndexError

        elif  film_on_shelf.is_rented:  #  checks if the flag is set to True
            film_on_shelf.is_rented = False
            print(f"\nFilm {title} was just returned")
            self.show_movies()

        elif not film_on_shelf.is_rented:
            print(f"\nFilm {title} is already returned / in libraries record")



    def show_movies(self):
        print("\nList of films with current status is:\n")
        for film in self.list_of_movies:
            print(film)


m1 = Movie("Lord of the rings", "Peter JAckson")
m2 = Movie("The Matrix", "Wachowski Brothers")
m3 = Movie("Harry Potter", "Chris Columbus")

rental_company = MovieRental()

rental_company.add_movie(m1)
rental_company.add_movie(m2)
rental_company.rent_movie("The Matrix")  # title is in the library, will work
# rental_company.rent_movie('The Matrix 2' ) # title is not in the library, film is not there.

rental_company.rent_movie(m1)

# rental_company.rent_movie("The Matrix") # should fail, as the film was already rented

rental_company.return_movie("The Matrix")
rental_company.return_movie(m1)


