import media
import fresh_tomatoes

""" Create instances of class Movie for films
    (title, storyline, poster_image_url, trailer_youtube_url """

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A successful but distracted Hollywood "
                                "screenwriter, and his fiancee, spend "
                                "time in Paris.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

school_of_rock = media.Movie("School of Rock",
                             "Struggling rock singer and guitarist "
                             "Dewey Finn is kicked out of his band "
                             "and subsequently disguises as a substitute"
                             "at a prestigious prep school.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Two hit men are out to retrieve "
                           "a suitcase stolen from their employer.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

star_wars = media.Movie("Star Wars: Episode VII - The Force Awakens",
                        "A scavenger called Rey has come into contact "
                        "with a droid that contains a map to the "
                        "legendary Luke Skywalker",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

hunger_games = media.Movie("The Hunger Games",
                           "Katniss Everdeen voluntarily takes "
                           "her younger sister's place in the "
                           "Hunger Games, a televised competition.",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=hmVi-GPUpy8")

""" Create a list of the movie instances defined above. """
movies = [avatar, midnight_in_paris, school_of_rock,
          pulp_fiction, star_wars, hunger_games]

""" Use the list of movies as an argument
to open_movies_page() function. """
fresh_tomatoes.open_movies_page(movies)
