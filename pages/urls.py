from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('tariffs', views.tariffs, name='tariffs'),
    path('set_cookie', views.set_cookie, name='set_cookie'),
    path('terms', views.terms, name='terms'),
    path('instructions', views.instructions, name='instructions'),
    path('implementation', views.implementation, name='implementation'),
    path('<name_slug>', views.page, name='page'),




]
