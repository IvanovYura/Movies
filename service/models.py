from flask_restx import Model
from flask_restx.fields import String, List, Nested

person = Model('Person Model', {
    'id': String(),
    'name': String(),
    'gender': String(),
    'eye_color': String(),
    'hair_color': String(),
    'age': String(),
})

film_model = Model('Film Model', {
    'id': String(),
    'title': String(),
    'description': String(),
    'director': String(),
    'producer': String(),
    'release_date': String(),
    'rt_score': String(),
    'people': List(Nested(person)),
})
