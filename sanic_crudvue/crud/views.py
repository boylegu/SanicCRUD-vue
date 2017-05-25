from sanic.response import json
from sanic import Blueprint
from sanic.views import HTTPMethodView
from crud.models import ShanghaiPersonInfo

crud_bp = Blueprint(
    'crud',
    url_prefix='/api/persons'
)


class PersonsInfoView(HTTPMethodView):
    async def get(self, request):
        return json(ShanghaiPersonInfo.all())


class UsernameListView(HTTPMethodView):
    async def get(self, request):
        return json(ShanghaiPersonInfo.values_list('username'))


crud_bp.add_route(PersonsInfoView.as_view(), '/')
crud_bp.add_route(UsernameListView.as_view(), '/name')