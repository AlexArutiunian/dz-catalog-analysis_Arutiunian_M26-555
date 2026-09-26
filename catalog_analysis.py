import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Этап 1. Числа и math

def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return oldest, newest, average


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


# Этап 2. Условия и match

def rating_tier(rating):
    if rating >= 7:
        return "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы

def print_non_comedy_titles(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    index = 0
    found_movie = None

    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            found_movie = movie
            break
        index += 1
    else:
        print("Шедевров не найдено")

    return found_movie


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Этап 4. Строки

def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:]
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)


def make_slug(title):
    normalized_title = normalize_title(title)
    return normalized_title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


# Этап 5. Списки

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# Этап 6. Словари

def count_by_genre(movies):
    counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1

    return counts


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])

    return filmography


def ratings_above_average(movies):
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }


# Этап 7. Множества

def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres


def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b


# Этап 8. Итераторы и генераторы

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated_movies(movies, min_rating=8.0):
    for movie in iter_high_rated(movies, min_rating):
        print(format_report_line(movie))


def total_duration_above_seven(movies):
    return sum(
        movie["duration_min"]
        for movie in movies
        if movie["rating"] > 7
    )


# Этап 9. Итоговый отчет

def build_report(movies):
    average = average_rating(movies)
    _, _, average_age = catalog_age_stats(movies)

    print("ОТЧеТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average}")
    print(f"Средний возраст фильмов: {average_age} лет")

    print("\nТоп-3 фильма:")
    top_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )[:3]
    for movie in top_movies:
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")

    genres = ", ".join(sorted(all_genres(movies)))
    print(f"\nВсе жанры каталога: {genres}")


if __name__ == "__main__":
    build_report(movies)
