from django.urls import path
# Импортируем созданные нами представления
from .views import (ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete)

urlpatterns = [

   path('', ProductsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),
   path('create/', ProductCreate.as_view(), name='product_create'),
   path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
]