from django.conf.urls import url
from .views import homePageView


urlpatterns = [
    url('', homePageView, name='home')
]
