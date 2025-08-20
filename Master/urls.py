from django.urls import path
from Master.views.home import Home
from Master.views.product import ProductMasterAPI, AddToCartAPI  # Import the AddToCartAPI
from Master.views.dummy import upload_excel  # Import the upload_excel view

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('product/', ProductMasterAPI.as_view(), name='product_api'),  # All products
    path('product/<int:pk>/', ProductMasterAPI.as_view(), name='product_detail_api'),  # Specific product
    path('add-to-cart/', AddToCartAPI.as_view(), name='add_to_cart_api'),  # Add product to cart
    path('add-to-cart/<int:product_id>/', AddToCartAPI.as_view(), name='cart_by_product_api'),  # Get or remove a product from the cart
    path('upload-excel/', upload_excel, name='upload_excel'),  # Endpoint for uploading Excel files
]
