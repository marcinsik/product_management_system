from django.urls import path,include
from products import views


urlpatterns = [
path('warehouse/', views.WarehouseView.as_view(), name = 'warehouse'),
path('warehouse/<int:warehouse_id>/',views.WarehouseDetailView.as_view(), name ='warehouse-detail'),
path('product/', views.ProductView.as_view(), name = 'product'),
path('product/<int:product_id>/', views.ProductDetailView.as_view(), name= 'product-detail')
    ]