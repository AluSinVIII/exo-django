from turtle import update
from django.urls import URLPattern, path
from . import views

app_name = 'iloveshop'
urlpatterns = [
    path('', views.create_view, name='shop'), path('<id>', views.detail_view, name="detail"), path('<id>/update', views.update_view, name="update"), path('<id>/delete', views.delete_view, name="delete")
]
 
