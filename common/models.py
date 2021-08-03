from django.db import models
from pydash import py_



class Model(models.Model):
    representative_field = None

    @classmethod
    def get_representative_field(cls):
        if cls.representative_field:
            return cls.representative_field
        elif py_.get(cls, 'name'):
            return 'name'
        else:
            return 'id'

    class Meta:
        abstract = True

    def __str__(self):
        return str(py_.get(self, self.get_representative_field()))


class TimeStampedModel(Model):
    created = models.DateTimeField('생성', auto_now_add=True)
    updated = models.DateTimeField('업데이트', auto_now=True)

    class Meta:
        abstract = True

