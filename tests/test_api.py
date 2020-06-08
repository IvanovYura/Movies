from unittest import mock
from unittest.mock import MagicMock

from tests.base import TestBase
from tests.fixtures.INPUT_OUTPUT import PEOPLE, FILMS, OUTPUT


class ApiTest(TestBase):
    url = '/movies'

    @mock.patch('service.utils.api')
    def test_get_movies(self, api_mock):
        api_mock.get_people.return_value = PEOPLE
        api_mock.get_films.return_value = FILMS

        response = self.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(OUTPUT, response.json)

    @mock.patch('service.external_services.requests')
    def test_connection_error(self, requests_mock):
        requests_mock.exceptions.RequestException = MockIOError
        requests_mock.get.side_effect = MockIOError

        response = self.get(self.url)

        self.assertEqual(400, response.status_code)
        self.assertEqual('Connection error in GhibliApi', response.json['message'])

    @mock.patch('service.external_services.requests')
    def test_http_error(self, requests_mock):
        response = requests_mock.get.return_value = MagicMock()

        requests_mock.exceptions.RequestException = MockIOError
        requests_mock.exceptions.HTTPError = MockHTTPError

        response.raise_for_status.side_effect = MockHTTPError

        response = self.get(self.url)

        self.assertEqual(400, response.status_code)
        self.assertEqual(f'HTTPError: ', response.json['message'])


class MockIOError(BaseException):
    pass


class MockHTTPError(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
