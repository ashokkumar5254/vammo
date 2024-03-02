from django.urls import path
from . import views

urlpatterns=[
    path('<int:id>',views.product_view,name='product'),
    path('single/<str:product_name>',views.single_view,name='single'),
    path('cart',views.cart,name='cart'),
    path('cart_items/<int:id>',views.cart_item,name='cart_item'),
    path('increament/<int:id>',views.increament,name='increament'),
    path('decreament/<int:id>',views.decreament,name='decreament'),
    path('checkout_payment/<int:id>',views.checkout_payment,name='checkout_payment'),
    path('success',views.success,name='success'),
    path('cancel',views.cancel,name='cancel')
]