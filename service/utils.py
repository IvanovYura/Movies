from collections import defaultdict
from typing import List
from urllib.parse import urlsplit

from service.external_services import api


def get_movies() -> List[dict]:
    people = api.get_people()
    films = api.get_films()

    movie_people_map = defaultdict(list)

    for person in people:
        for film in person.pop('films'):
            film_id = _get_film_id(film)
            movie_people_map[film_id].append(person)

    for film in films:
        film['people'] = movie_people_map[film['id']]

    return films


def _get_film_id(film_url: str) -> str:
    return urlsplit(film_url).path.split('/films/')[-1]
