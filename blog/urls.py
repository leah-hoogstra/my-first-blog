from django.conf.urls import url
from . import views

# add url patterns
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
