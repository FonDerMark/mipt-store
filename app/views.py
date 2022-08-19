from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from app.forms import AuthForm
from django.views import View
from app.models import Notebook, Smartphone, Cleaners, TV, ToCard

context = {
    'hidden': 'hidden=hidden',
}


@method_decorator(csrf_exempt, name='dispatch')
class Logout(View):

    def get(self, request):
        logout(request)
        return render(request, 'html_base/index.html')


@method_decorator(csrf_exempt, name='dispatch')
class Register(View):

    def get(self, request):
        return render(request, 'html_base/register.html')

    def post(self, request):
        register_form = AuthForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            try:
                User.objects.get(username=username)
                return render(request, template_name='html_base/register.html',
                              context={'error': 'Пользователь с данным именем уже зарегистрированн'})
            except:
                User.objects.create_user(username=username, password=password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
        else:
            return redirect('register')


@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.notebooks = list(Notebook.objects.all())

    def get(self, request):
        try:
            return render(request, template_name='html_base/notebooks.html',
                          context={'notebook': self.notebooks,
                                   'orders': [i.articl for i in list(ToCard.objects.filter(user=request.user))]})
        except:
            return render(request, template_name='html_base/notebooks.html',
                          context={'notebook': self.notebooks})

    def post(self, request):
        try:
            art = request.POST.get('article')
            name = request.user
            new_order = ToCard.objects.create(user=name, articl=art)
            new_order.save()
            return redirect('index')
        except:
            return redirect('login')


@method_decorator(csrf_exempt, name='dispatch')
class Smartphones(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.smartphone = list(Smartphone.objects.all())

    def get(self, request):
        try:
            return render(request, template_name='html_base/smartphones.html',
                          context={'smartphone': self.smartphone,
                                   'orders': [i.articl for i in list(ToCard.objects.filter(user=request.user))]})
        except:
            return render(request, template_name='html_base/notebooks.html',
                          context={'notebook': self.smartphone})

    def post(self, request):
        try:
            art = request.POST.get('article')
            name = request.user
            new_order = ToCard.objects.create(user=name, articl=art)
            new_order.save()
            return redirect('smartphones')
        except:
            return redirect('login')


@method_decorator(csrf_exempt, name='dispatch')
class Tvs(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tv = list(TV.objects.all())

    def get(self, request):
        try:
            return render(request, template_name='html_base/tvs.html',
                          context={'tv': self.tv,
                                   'orders': [i.articl for i in list(ToCard.objects.filter(user=request.user))]})
        except:
            return render(request, template_name='html_base/notebooks.html',
                          context={'notebook': self.tv})

    def post(self, request):
        try:
            art = request.POST.get('article')
            name = request.user
            new_order = ToCard.objects.create(user=name, articl=art)
            new_order.save()
            return redirect('tvs')
        except:
            return redirect('login')


@method_decorator(csrf_exempt, name='dispatch')
class Cleaner(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cleaner = list(Cleaners.objects.all())

    def get(self, request):
        try:
            return render(request, template_name='html_base/cleaners.html',
                          context={'cleaner': self.cleaner,
                                   'orders': [i.articl for i in list(ToCard.objects.filter(user=request.user))]})
        except:
            return render(request, template_name='html_base/notebooks.html',
                          context={'notebook': self.cleaner})

    def post(self, request):
        try:
            art = request.POST.get('article')
            name = request.user
            new_order = ToCard.objects.create(user=name, articl=art)
            new_order.save()
            return redirect('cls')
        except:
            return redirect('login')


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):

    def get(self, request):
        return render(request, 'html_base/login.html')

    def post(self, request):
        login_form = AuthForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                return render(request, template_name='html_base/login.html',
                              context={'error': 'Данный пользователь не найден'})


class Card(LoginRequiredMixin, View):
    def __init__(self):
        super().__init__()
        self.all_groups = list(Notebook.objects.all()) + list(Smartphone.objects.all()) + \
                          list(Cleaners.objects.all()) + list(TV.objects.all())
        self.card = []

    def get(self, request):
        order_arts = [i.articl for i in ToCard.objects.filter(user=request.user)]
        for item in self.all_groups:
            if item.articl in order_arts:
                self.card.append(item)

        return render(request, template_name='html_base/card.html', context={'orders': self.card})

    def post(self, request):
        art = request.POST.get('art')
        user = request.user
        ToCard.objects.filter(user=user, articl=art).delete()
        return redirect('card')
