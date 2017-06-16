"""
    sanic-crud-vue is a simple example demo with Vue 2.x. I hope pass thought this project for express new develop model.
    :copyright: (c) 2017 by Boyle Gu
    :license: MIT, see LICENSE for more details

"""
import json

from sanic import Sanic
from sanic_crudvue import crud_bp

app = Sanic('test-app')
app.blueprint(crud_bp)

settings = dict(MAX_PER_PAGE=5)
app.config.update(settings)

put_data = {'phone': '08613000001111'}
filter_params = {'sex': 'male', 'email': 'qq.com'}


def test_get_sex_list():
    request, response = app.test_client.get('/api/sex')
    return response.status == 200


def test_get_personse_list():
    request, response = app.test_client.get('/api/persons')
    assert response.status == 200


def test_get_personse_detail():
    request, response = app.test_client.get('/api/persons/detail/1')
    assert response.status == 200


def test_put_personse_item():
    request, response = app.test_client.put('/api/persons/detail/1', data=json.dumps(put_data))
    assert response.status == 200


def test_get_filter_item():
    request, response = app.test_client.get('/api/persons', params=filter_params)
    assert response.status == 200
