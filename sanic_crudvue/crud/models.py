import datetime

from peewee import CharField, DateTimeField, SqliteDatabase, Model, TextField
from playhouse.shortcuts import model_to_dict

db = SqliteDatabase('info.db')


class BaseModel(Model):
    class Meta:
        database = db
        indexes = (
            # create a no-unique on username and email
            (('sex', 'email'), False),
        )

    @classmethod
    def all(cls):
        data = cls.select().iterator()
        return [model_to_dict(row) for row in data]

    @classmethod
    def values_list(cls, *args, **kwargs):
        result = []
        for arg in args:
            qs_expression = "{0}.select({0}.{1}).iterator()".format(cls.__name__, arg)
            for row in eval(qs_expression):
                result.append(eval('row.{0}'.format(arg)))
        return result


class ShanghaiPersonInfo(BaseModel):
    create_datetime = DateTimeField(default=datetime.datetime.utcnow(), null=True)
    username = CharField()
    email = CharField()
    phone = CharField()
    sex = CharField()
    zone = TextField()
