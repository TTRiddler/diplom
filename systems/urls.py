from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^numeric-systems/(?P<subsection_id>\d+)/$', views.infoPage_num, name="infoPage_num"),
	url(r'^algebraic-systems/(?P<subsection_id>\d+)/$', views.infoPage_alg, name="infoPage_alg"),
    url(r'^$', views.mainPage, name="main"),
    url(r'^numeric-systems/$', views.numeric, name="numeric"),
    url(r'^algebraic-systems-1/$', views.algebraic, name="algebraic"),
    url(r'^algebraic-systems-2/$', views.algebraic2, name="algebraic2"),
    url(r'^about/$', views.about, name="about"),
]
