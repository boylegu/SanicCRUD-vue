from sanic.response import json
from sanic import Blueprint

crud_bp = Blueprint(
    'crud',
    url_prefix='/crud/api'
)


@crud_bp.route('/list')
async def test(request):
    return json({"hello": "vue"})
