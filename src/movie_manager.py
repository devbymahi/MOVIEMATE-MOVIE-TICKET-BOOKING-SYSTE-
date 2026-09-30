from data.movie_data import languages, movies, show_times
from src.utils import line, pause, sad_message, movie_fun_message


def display_languages():
    line()
    print("                    LANGUAGE PREFERENCE")
    line()

    for number, language in languages.items():
        print(f"{number}. {language}")

    print("0. Show All Languages")

    line()


def choose_language():
    display_languages()

    try:
        choice = int(input("🌐 Select preferred language: "))
    except ValueError:
        sad_message()
        return "All"

    if choice == 0:
        return "All"

    if choice not in languages:
        sad_message()
        return None

    selected_language = languages[choice]

    print(
        f"\n🎬 Great! Showing movies available in {selected_language}."
    )

    return selected_language


def get_filtered_movies(language):
    if language == "All":
        return movies

    filtered_movies = {}

    for number, movie in movies.items():
        if movie["language"] == language:
            filtered_movies[number] = movie

    return filtered_movies


def display_movies(language="All"):
    filtered_movies = get_filtered_movies(language)

    line()

    if language == "All":
        print("                         ALL MOVIES")
    else:
        print(f"                     {language.upper()} MOVIES")

    line()

    if not filtered_movies:
        print("😢 No movies available in this language.")
        return

    for number, movie in filtered_movies.items():
        print(f"\n{number}. 🎬 {movie['name']}")
        print(f"   Language   : {movie['language']}")
        print(f"   Genre      : {movie['genre']}")
        print(f"   Duration   : {movie['duration']}")
        print(f"   Rating     : {movie['rating']}")
        print(f"   Actors     : {movie['actors']}")
        print(f"   Director   : {movie['director']}")
        print(f"   Ticket     : ₹{movie['price']}")

    line()


def display_movie_details(movie):
    line()
    print("                       MOVIE DETAILS")
    line()

    print(f"🎬 Movie       : {movie['name']}")
    print(f"🌐 Language    : {movie['language']}")
    print(f"🎭 Genre       : {movie['genre']}")
    print(f"⏱️ Duration    : {movie['duration']}")
    print(f"⭐ Rating      : {movie['rating']}")
    print(f"👤 Actors      : {movie['actors']}")
    print(f"🎥 Director    : {movie['director']}")
    print(f"🎟️ Ticket Price: ₹{movie['price']}")

    line()


def display_show_times():
    line()
    print("                         SHOW TIMES")
    line()

    for number, time_value in show_times.items():
        print(f"{number}. 🕐 {time_value}")

    line()