from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.index, name='index'),
    url('notes/add/$', views.add, name='add'),
    url('notes/edit/(?P<note_uuid>[0-9A-Fa-f-]+)/$', views.edit, name='edit'),
    url('notes/delete/(?P<note_uuid>[0-9A-Fa-f-]+)/$', views.delete, name='delete'),
    url('notes/history/(?P<note_uuid>[0-9A-Fa-f-]+)/$', views.note_history, name='note_history'),
    url('notes/history/$', views.history, name='history'),
]
