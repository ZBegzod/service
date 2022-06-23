from django.urls import include, path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',test_api_view),
    path('api-view-combo/list', ComboListview.as_view(), name = 'combo-list-view'),
    path('api-view-combo/create', ComboCreate.as_view(), name = 'combo-create-view'),
    path('api-view-combo/update/<int:pk>', ComboUpdate.as_view(), name = 'combo-update-view'),
    path('api-view-combo/delete/<int:pk>', ComboDelete.as_view(), name = 'combo-delete-view'),
    path('api-view-product/list', ProductListview.as_view(), name = 'product-list-view'),
    path('api-view-product/create', ProductCreate.as_view(), name = 'product-create-view'),
    path('api-view-product/update/<int:pk>', ProductUpdate.as_view(), name = 'product-update-view'),
    path('api-view-product/delete/<int:pk>', ProductDelete.as_view(), name = 'product-delete-view'),
    path('api-view-resurs/list', ResursListview.as_view(), name = 'resurs-list-view'),
    path('api-view-resurs/create', ResursCreate.as_view(), name = 'resurs-create-view'),
    path('api-view-resurs/update/<int:pk>', ResursUpdate.as_view(), name = 'resurs-update-view'),
    path('api-view-resurs/delete/<int:pk>', ResursDelete.as_view(), name = 'resurs-delete-view'),
    path('api-view-fast-food/list', Fast_food_Listview.as_view(), name = 'fast-food-list-view'),
    path('api-view-fast-food/create', Fast_food_Create.as_view(), name = 'fast-food-create-view'),
    path('api-view-fast-food/update/<int:pk>', Fast_food_Update.as_view(), name = 'fast-food-update-view'),
    path('api-view-fast-food/delete/<int:pk>', Fast_food_Delete.as_view(), name = 'fast-food-delete-view'),
    path('api-view-orders/list', OrdersListview.as_view(), name = 'orders-list-view'),
    path('api-view-orders/create', OrdersCreate.as_view(), name = 'orders-create-view'),
    path('api-view-orders/update/<int:pk>', OrdersUpdate.as_view(), name = 'orders-update-view'),
    path('api-view-orders/delete/<int:pk>', OrdersDelete.as_view(), name = 'orders-delete-view'),
    path('api-view/<int:pk>', combo_api_view),
    path('api-auth/', include('rest_framework.urls')),
    path('token-auth/', obtain_auth_token)
]