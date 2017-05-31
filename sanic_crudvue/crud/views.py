from sanic.response import json
from sanic import Blueprint
from sanic.views import HTTPMethodView
from playhouse.shortcuts import model_to_dict

from crud.models import ShanghaiPersonInfo
from .helper import list_remove_repeat

crud_bp = Blueprint(
    'crud',
    url_prefix='/api/persons'
)


class PersonsInfoView(HTTPMethodView):
    async def get(self, request, *args, **kwargs):
        page = int(request.args.get('page', 1))
        sex, email = request.args.get('sex'), request.args.get('email')
        qs = ShanghaiPersonInfo.filters(sex=sex, email=email, page_number=page, items_per_page=5)
        result = [model_to_dict(row) for row in qs.result]

        return json(
            {
                'results': result,
                'count': 5,
                'page': page,
                'total': ShanghaiPersonInfo.filters(sex=sex, email=email).counts()
            }
        )


class SexListView(HTTPMethodView):
    async def get(self, request):
        unique_list = list_remove_repeat(ShanghaiPersonInfo.values_list('sex'))
        result = [dict(label=i, value=i) for i in unique_list]
        return json(result)


crud_bp.add_route(PersonsInfoView.as_view(), '')
crud_bp.add_route(SexListView.as_view(), '/sex')
