from flask_restx import Namespace, Resource, abort

from service import cache, BaseConfig
from service.models import film_model, person
from service.utils import get_movies

ns = Namespace(
    name='Movies',
    description='Returns movies with the people appeared in it',
    path='/',
)

# register models
ns.models[film_model.name] = film_model
ns.models[person.name] = person


@ns.route('/movies')
class Api(Resource):
    @ns.response(200, 'Success', film_model)
    @ns.response(400, 'Bad Request')
    @ns.marshal_list_with(film_model)
    @cache.cached(timeout=BaseConfig.CACHE_TIMEOUT)
    def get(self):
        try:
            return get_movies()
        except ValueError as e:
            abort(400, str(e))
