import media
import fresh_tomatoes

if __name__ == '__main__':
    # Create the various movies
    toy_story = media.Movie("Toy Story", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    avatar = media.Movie("Avatar", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    # Make a call to render page and open web browser
    fresh_tomatoes.open_movies_page([toy_story, avatar])
