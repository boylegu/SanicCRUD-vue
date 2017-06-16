from sanic.response import json
from sanic import Blueprint
from sanic.views import HTTPMethodView
from playhouse.shortcuts import model_to_dict

from .models import ShanghaiPersonInfo
from .helper import list_remove_repeat

crud_bp = Blueprint(
    'crud',
    url_prefix='/api/persons'
)


class PersonsInfoListView(HTTPMethodView):

    """
    @api {GET} /api/persons   Get all or a part of person info
    @apiName GetAllInfoList
    @apiGroup Info Manage
    @apiVersion 1.0.0

    @apiExample {httpie} Example usage: (support combinatorial search)

    All person：
    http /api/persons

    You can according to 'sex | email' or 'sex & email'
    http /api/persons?sex=xxx&email=xx
    http /api/persons?sex=xxx
    http /api/persons?email=xx

    @apiParam {String} sex
    @apiParam {String} email

    @apiSuccess {String} create_datetime
    @apiSuccess {String} email
    @apiSuccess {String} id
    @apiSuccess {String} phone
    @apiSuccess {String} sex
    @apiSuccess {String} username
    @apiSuccess {String} zone

    """
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

    """
    @api {GET} /api/persons/detail/:id  details info
    @apiName GetPersonDetails
    @apiGroup Info Manage
    @apiVersion 1.0.0

    @apiExample {httpie} Example usage:

    http /api/persons/detail/1

    @apiSuccess {String} create_datetime
    @apiSuccess {String} email
    @apiSuccess {String} id
    @apiSuccess {String} phone
    @apiSuccess {String} sex
    @apiSuccess {String} username
    @apiSuccess {String} zone


    """

    """
    @api {PUT} /api/persons/detail/:id  update person info
    @apiName PutPersonDetails
    @apiGroup Info Manage
    @apiVersion 1.0.0

    @apiExample {httpie} Example usage:

    http /api/persons/detail/1

    @apiSuccess {String} create_datetime
    @apiSuccess {String} email
    @apiSuccess {String} id
    @apiSuccess {String} phone
    @apiSuccess {String} sex
    @apiSuccess {String} username
    @apiSuccess {String} zone

    """

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

    """
    @api {GET} /api/persons/sex Get all sexList
    @apiName GetAllSexList
    @apiGroup Info Manage
    @apiVersion 1.0.0

    @apiExample {httpie} Example usage:

    http /api/persons/sex

    @apiSuccess {String} label
    @apiSuccess {String} value

    """
    async def get(self, request):
        unique_list = list_remove_repeat(ShanghaiPersonInfo.values_list('sex'))
        result = [dict(label=i, value=i) for i in unique_list]
        return json(result)


crud_bp.add_route(PersonsInfoDetailView.as_view(), '/detail/<item_id>')
crud_bp.add_route(PersonsInfoListView.as_view(), '')
crud_bp.add_route(SexListView.as_view(), '/sex')
