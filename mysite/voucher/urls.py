from django.urls import path
from . import views

urlpatterns = [
	#urls to views here
	path('', views.voucher, name='Merry Christmas'),
    path('redeem/', views.redeem, name="redeem"),
	path('success/', views.success, name="success"),
]
