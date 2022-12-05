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

