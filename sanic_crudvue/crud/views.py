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


class PersonsInfoListView(HTTPMethodView):
    async def get(self, request):
        max_per_page = request.app.config['MAX_PER_PAGE']
        page = int(request.args.get('page', 1))
        sex, email = request.args.get('sex'), request.args.get('email')
        qs = ShanghaiPersonInfo.filters(sex=sex, email=email, page_number=page,
                                        items_per_page=max_per_page)
        result = [model_to_dict(row) for row in qs.result.iterator()]

        return json(
            {
                'results': result,
                'count': max_per_page,
                'page': page,
                'total': ShanghaiPersonInfo.filters(sex=sex, email=email).counts()
            }
        )


class PersonsInfoDetailView(HTTPMethodView):
    async def get(self, request, item_id):
        data = ShanghaiPersonInfo.get(id=item_id)
        return json(model_to_dict(data))

    async def put(self, request, item_id):
        update_data = eval(request.body.decode())
        qs = ShanghaiPersonInfo.update(**update_data).where(ShanghaiPersonInfo.id == item_id)
        qs.execute()
        new_data = ShanghaiPersonInfo.get(id=item_id)
        return json(model_to_dict(new_data))


class SexListView(HTTPMethodView):
    async def get(self, request):
        unique_list = list_remove_repeat(ShanghaiPersonInfo.values_list('sex'))
        result = [dict(label=i, value=i) for i in unique_list]
        return json(result)


crud_bp.add_route(PersonsInfoDetailView.as_view(), '/detail/<item_id>')
crud_bp.add_route(PersonsInfoListView.as_view(), '')
crud_bp.add_route(SexListView.as_view(), '/sex')
