from unittest.mock import MagicMock
import pytest
from setup_db import db

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    director1 = Director(id=1, name="Director 1")
    director2 = Director(id=2, name="Director 2")
    director3 = Director(id=3, name="Director 3")

    directors = {
        1: director1,
        2: director2,
        3: director3,
    }

    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=director1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    genre1 = Genre(id=1, name="Genre 1")
    genre2 = Genre(id=2, name="Genre 2")
    genre3 = Genre(id=3, name="Genre 3")

    genres = {
        1: genre1,
        2: genre2,
        3: genre3,
    }

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genre1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    movie1 = Movie(id=1,
                   title="Title 1",
                   description="description 1",
                   trailer="trailer 1",
                   year=2000,
                   rating=1.1,
                   genre_id=1,
                   director_id=1)
    movie2 = Movie(id=2,
                   title="Title 2",
                   description="description 2",
                   trailer="trailer 2",
                   year=2002,
                   rating=1.2,
                   genre_id=2,
                   director_id=2)
    movie3 = Movie(id=3,
                   title="Title 3",
                   description="description 3",
                   trailer="trailer 3",
                   year=2003,
                   rating=1.3,
                   genre_id=3,
                   director_id=3)

    movies = {
        1: movie1,
        2: movie2,
        3: movie3,
    }

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=movie1)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
