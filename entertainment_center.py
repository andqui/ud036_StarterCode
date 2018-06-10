import media
import fresh_tomatoes

if __name__ == '__main__':
    # Create the various movies
    toy_story = media.Movie("Toy Story",
                            "https://upload.wikimedia.org/wikipedia/" +
                            "en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    avatar = media.Movie("Avatar",
                         "https://upload.wikimedia.org/wikipedia/" +
                         "en/b/b0/Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=6ziBFh3V1aM")

    die_hard = media.Movie("Die Hard",
                           "https://upload.wikimedia.org/wikipedia/" +
                           "en/7/7e/Die_hard.jpg",
                           "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

    # Make a call to render page and open web browser
    fresh_tomatoes.open_movies_page([toy_story, avatar, die_hard])
