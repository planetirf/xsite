from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^Alfisols', views.detail, name='detail'),
    url(r'^suborders/', views.suborder_view, name='suborder_view'),
    url(r'^greatgroups/', views.greatgroup_view, name='greatgroup_view'),
    url(r'^orders/', views.soil_view, name='soil_view'),
    url(r'^[a-zA-Z]+/$', views.detail, name='detail'),
]
