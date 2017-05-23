from sanic import Sanic
from crud.views import crud_bp
from crud.models import db, ShanghaiPersonInfo
from sanic_crud import generate_crud

app = Sanic(__name__)
app.blueprint(crud_bp)

db.create_tables([ShanghaiPersonInfo], safe=True)
generate_crud(app, [ShanghaiPersonInfo])
app.run(host='0.0.0.0', port=8000, debug=True)
