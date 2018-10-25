from django.conf.urls import url
from .views import homePageView
from .views import commodityCreateView

urlpatterns = [
    url('', homePageView, name='home'),
    url('trade/add_commodity',commodityCreateView, name='create'),
]
