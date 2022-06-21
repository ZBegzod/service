from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('fast-food/', fast_food_objects, name = 'fast-food'),    
    path('fast-food/add', fast_food_add_or_update, name = 'fast-food-add'),    
    path('fast-food/update/<int:pk>', fast_food_add_or_update, name = 'fast-food-update'),    
    path('fast-food/delete/<int:pk>', fast_food_delete, name = 'fast-food-delete'),    
    path('combo/', combo_objects, name = 'combo'),
    path('combo/add', combo_add_or_update, name ='combo-add'), 
    path('combo/update/<int:pk>', combo_add_or_update, name = 'combo-update'), 
    path('combo/delete/<int:pk>', combo_delete, name = 'combo-delete'), 
    path('fast-food-class/', Fast_foodListView.as_view(), name = 'fast-food-class'), 
    path('fast-food-class/add', Fast_food_createView.as_view(), name = 'fast-food-add-class'), 
    path('fast-food-class/update/<int:pk>', Fast_food_UpdateView.as_view(), name = 'fast-food-update-class'), 
    path('fast-food-class/delete/<int:pk>', Fast_food_DeleteView.as_view(), name = 'fast-food-delete-class'), 
    path('product/', ProductListView.as_view(), name = 'product'), 
    path('product/add', ProductAddView.as_view(), name = 'product-add'), 
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name = 'product-update'), 
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name = 'product-delete'), 
    path('resurs/', ResursListView.as_view(), name = 'resurs'), 
    path('resurs/add', ResursCreateView.as_view(), name = 'resurs-add'), 
    path('resurs/update/<int:pk>', ResursUpdateView.as_view(), name = 'resurs-update'), 
    path('resurs/delete/<int:pk>', ResursDeleteView.as_view(), name = 'resurs-delete'), 
    path('orders/', OrdersListView.as_view(), name = 'orders'), 
    path('orders/add', OrdersCreateView.as_view(), name = 'orders-add'), 
    path('orders/update/<int:pk>', OrdersUpdateView.as_view(), name = 'orders-update'), 
    path('orders/delete/<int:pk>', OrdersDeleteView.as_view(), name = 'orders-delete'), 
    path('register/', user_register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('fast-food-order/', user_login_view, name='fast-food-order')
]
