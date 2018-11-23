from django.conf.urls import url
from .views import homePageView
from .views import commodityCreateView, myCommoditiesView, my_view, requestsShow
urlpatterns = [
    url(r'^$', homePageView, name='home'),
    url(r'^commodity/add/$', commodityCreateView, name='commodity-add'),
    url(r'^commodity/buy/$', my_view, name='commodity-buy'),
    url(r'^commodity/requests/$', requestsShow, name='requests-view'),
    url(r'^mycommodities/view/$', myCommoditiesView, name='mycommodities-view'),
]
