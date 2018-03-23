from django.conf.urls import url
from . import views

app_name = "uploadfile"
urlpatterns = [
  url(r'^$', views.FileFormCreate.as_view(), name='index'),

]