import webbrowser


class Movie():
    """ This class provides a way to store movie related information.

    Attributes:
        movie_title: The name of the movie.
        movie_storyline: The storyline of the movie.
        poster_image: The URL of the poster image.
        trailer_youtube: The URL of the Youtube trailer.

    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        """ Initialise properties for the class Movie. """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open the webbrowser with the given URL to play trailer. """
        webbrowser.open(self.trailer_youtube_url)
