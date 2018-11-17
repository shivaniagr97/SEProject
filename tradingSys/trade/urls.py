from django.conf.urls import url
from .views import homePageView
from .views import commodityCreateView
urlpatterns = [
    url(r'^$', homePageView, name='home'),
    url(r'^commodity/add/$', commodityCreateView, name='commodity-add'),
]
