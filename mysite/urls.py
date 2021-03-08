from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.index, name='index'),
    url('notes/add/$', views.add, name='add'),
    url('notes/edit/(?P<note_uuid>[0-9A-Fa-f-]+)', views.edit),
    url('notes/history/(?P<note_uuid>[0-9A-Fa-f-]+)', views.history),
]
