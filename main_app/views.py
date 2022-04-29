from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json

# Create your views here.
from django.views import View
from .forms import SomeForm
from .models import Some


class Index(View):

    def get(self, request):
        return render(request, 'html_pages/index.html', context={'Form': SomeForm})

    def post(self, request):
        form = SomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return HttpResponse(":(")


class Api(View):

    def get(self, request):
        return JsonResponse(data)
