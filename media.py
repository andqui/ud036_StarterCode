
class Movie:
    """ A class representing a movie data model.

        Attributes:
            title (str): The movie title.
            poster_image_url (str): An url to an poster thumbnail image.
            trailer_youtube_url (str): An url to a movie trailer.

        """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
