from django.conf.urls import url

from lists.views import new_list, view_list

urlpatterns = [
    url(r'^(\d+)/$', view_list, name='view_list'),
    url(r'^new$', new_list, name='new_list'),
]
