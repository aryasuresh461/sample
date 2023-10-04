from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name='crud'),
    path('add_product/', views.add_product, name='add_product'),  # Added a comma here
    path('show_products/', views.show_products, name='show_products'),

    path('edit_product/<int:pk>/', views.edit_product_details, name='edit_product_details'),  
    path('deletepage/<int:pk>/', views.deletepage, name='deletepage'),
    path('update_image/<int:pk>/', views.update_product_image, name='update_product_image'),
]
