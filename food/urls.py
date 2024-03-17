from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path('', views.item, name = 'item'),
    path('<int:item_id>/', views.details, name = 'details')
]