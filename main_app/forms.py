from django.forms import forms, modelform_factory
from .models import Some


SomeForm = modelform_factory(Some, fields='__all__')