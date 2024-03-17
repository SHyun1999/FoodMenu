from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path('item', views.item, name = 'item'),
    path('item/<int:item_id>/', views.details, name = 'details')
]
