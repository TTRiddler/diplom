from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name="main"),
    url(r'^numeric-systems/$', views.numeric, name="numeric"),
    url(r'^algebraic-systems/$', views.algebraic, name="algebraic"),
]
