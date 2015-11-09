from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /ssapp/
    url(r'^$', views.index, name='index'),
    # ex: /ssapp/family/5/
    url(r'^family/(?P<family_id>[0-9]+)/$', views.family, name='family'),
    # ex: /ssapp/person/5/
    url(r'^person/(?P<person_id>[0-9]+)/$', views.person, name='person'),

    url(r'^detail/$', views.detail, name='detail'),

    url(r'^setup/$', views.setup, name='setup'),

]