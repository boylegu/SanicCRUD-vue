from peewee import CharField, DateTimeField, SqliteDatabase, Model, TextField
import datetime


db = SqliteDatabase('info.db')

class BaseModel(Model):
    class Meta:
        database = db

class ShanghaiPersonInfo(BaseModel):
    route_url = '/api/shanghai/person'

    create_datetime = DateTimeField(default=datetime.datetime.utcnow(), null=True)
    username = CharField()
    email = CharField()
    phone = CharField()
    sex = CharField()
    zone =  TextField()

