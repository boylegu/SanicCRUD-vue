from sanic import Sanic
from crud.views import crud_bp
from crud.models import db, ShanghaiPersonInfo

app = Sanic(__name__)
app.blueprint(crud_bp)

db.create_tables([ShanghaiPersonInfo], safe=True)

app.run(host='0.0.0.0', port=8000, debug=True)
