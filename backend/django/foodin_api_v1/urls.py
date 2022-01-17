from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'foodin_api_v1'

urlpatterns = [
    path(
        'product',
        views.ProductAPIView.as_view(),
        name='product'
    ),
    path(
        'product/<int:pk>',
        views.ProductAPIView.as_view(),
        name='product'
    ),
]


"""

Otra forma de hacerlo

urlpatterns = [
    path(
        'product/',
        views.product_get,
        name='product_get_all'
    ),
    path(
        'product/<int:pk>/',
        views.product_get,
        name='product_get'
    ),

    path(
        'product/<int:pk>/',
        views.product_post,
        name='product_post'
    ),
    path(
        'product/<int:pk>/',
        views.product_put,
        name='product_put'
    ),
    path(
        'product/<int:pk>/',
        views.product_delete,
        name='product_delete'
    ),
]
"""

