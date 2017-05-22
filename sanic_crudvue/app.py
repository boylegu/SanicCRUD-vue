from sanic import Sanic
# from crud import crud_bp
from crud.views import crud_bp

app = Sanic(__name__)
app.blueprint(crud_bp)


app.run(host='0.0.0.0', port=8000, debug=True)
