from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^suborders/', views.suborder_view, name='suborder_view'),
    url(r'^greatgroups/', views.greatgroup_view, name='greatgroup_view'),
]
