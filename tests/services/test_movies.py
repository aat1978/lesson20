import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Title 1"

    def test_create(self):
        movie_d = {
            "id": 4,
            "title": "Title 4",
            "description": "description 4",
            "trailer": "trailer 4",
            "year": 2004,
            "rating": 1.4,
            "genre_id": 1,
            "director_id": 1,
        }
        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "Title 3",
            "description": "description 3",
            "trailer": "trailer 3",
            "year": 2022,
            "rating": 1.3,
            "genre_id": 3,
            "director_id": 3,
        }
        assert self.movie_service.update(movie_d)

    def test_delete(self):
        assert self.movie_service.delete(1) is None
