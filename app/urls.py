from django.urls import path
from app.views import Index, Users, Logout, Register, Card, Smartphones, Cleaner, Tvs

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Users.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('card/', Card.as_view(), name='card'),
    path('sm/', Smartphones.as_view(), name='smartphones'),
    path('tv/', Tvs.as_view(), name='tvs'),
    path('cl/', Cleaner.as_view(), name='cls'),
]