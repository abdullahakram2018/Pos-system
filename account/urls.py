from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('billing/order', views.sales_bill, name='order'),
    path('sales_bill/', views.sales_bill_pdf, name='sales_bill'),
    path('create/', views.create, name='create'),
    path('order/', views.order_try, name='order'),
    path('createmu/', views.createMu, name='createmu'),

]
