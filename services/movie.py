from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: int = None,
        actors_ids: int = None) -> QuerySet[Movie, Movie]:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie | None:
    queryset = Movie.objects.filter(id=movie_id)
    return queryset.first()


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[str] | None = None,
        actors_ids: list[str] | None = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)

    return movie
