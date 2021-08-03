from django.contrib import admin
from django_object_actions import DjangoObjectActions
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.db.models.fields.reverse_related import OneToOneRel
from django.db.models.fields.reverse_related import ManyToOneRel


def check_related_field(field):
    if type(field) in [ForeignObjectRel, ManyToOneRel, OneToOneRel]:
        return True


class ModelAdmin(DjangoObjectActions, admin.ModelAdmin):
    def get_list_display(self, request):
        if self.list_display == ('__str__',):
            return [field.name for field in self.model._meta.get_fields() if not check_related_field(field)]
        else:
            return super().get_list_display(request)
