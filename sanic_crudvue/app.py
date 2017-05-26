from sanic import Sanic
from sanic_cors import CORS

from crud.views import crud_bp
from crud.models import db, ShanghaiPersonInfo

app = Sanic(__name__)
CORS(app)
app.blueprint(crud_bp)

db.create_tables([ShanghaiPersonInfo], safe=True)

app.run(host='0.0.0.0', port=8000, debug=True)
