import unittest
import vcr

from pytest import fixture
from trywrapper import TV


@fixture
def tv_keys():
    """Responsible only for returning the test data"""
    return [
        'id', 'origin_country', 'poster_path', 'name', 'overview',
        'popularity', 'backdrop_path', 'first_air_date', 'vote_count',
        'vote_average'
    ]


@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml',
                  filter_query_parameters=['api_key'])
def test_tv_info(tv_keys):
    """tests an API to get a TV show's info"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response["id"] == 1396
    assert set(tv_keys).issubset(response.keys())


@vcr.use_cassette('tests.vcr_cassettes/tv-popular.yml',
                  filter_query_parameters=['api_key'])
def test_tv_popularity():
    """Tests an API call to get popular tv shows"""

    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert set(tv_keys()).issubset(response['results'][0].keys())
