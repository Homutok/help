from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^guides/$''', views.QuestionsListView.as_view(), name='guide'),
    url(r'^guide/(?P<pk>\d+)$', views.QuestionsDetailView.as_view(), name='guide-detail'),
]