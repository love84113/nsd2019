from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin_index'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
]