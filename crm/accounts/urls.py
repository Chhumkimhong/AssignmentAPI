from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('', views.Index,name='Home'),
    path('Home', views.Index,name='Home'),
    path('Shop',views.Shop,name='Shop'),
    path('Shop_Detail',views.ShopDetail,name='Shop_Detail'),
    # path('',views.Shopdetail,name='ShopDetail'),
    path('ShopDetail/<int:pk>/',views.Shopdetail,name='ShopDetail'),
    path('AddCart/<int:product_id>/',views.Cart,name='AddCart'),
    path('AddtoCart/<int:pk>/',views.AddtoCart,name='AddtoCart'),
    path('Cart',views.Cart,name='Cart'),
    # path('Cart',views.Cart,name='Cart'),
    path('Pages',views.Pages,name='Pages'),
    path('CheckOut',views.CheckOut,name='CheckOut'),
    path('Testimonial',views.Testimonial,name='Testimonial'),
    path('Contact',views.Contact,name='Contact'),
    path('products', views.products),
    path('customer', views.customer),
    path('payment/',views.payment,name='payment'),
    path('BestSeller',views.bestSeller,name='BestSeller'),
    path('CartBestSeller/<int:pk>/',views.AddtoCartBestSeller,name='CartBestSeller'),

    path("signup/",authView, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/", include("authView.urls")),
    # path("accounts/", include("accounts.urls", namespace='accounts')),

    path('Pros/', ProductsListCreate.as_view(), name='ProList'),
    path('Pros/<int:pk>/', ProductsDetail.as_view(), name='ProDetail'),
    
    path('Category/', CategoryListCreate.as_view(), name='CategoryList'),
    path('Category/<int:pk>/', CategoryDetail.as_view(), name='CategoryDetail'),

    path('BestSeller/', BestSellerListCreate.as_view(), name='BestSellerList'),
    path('BestSeller/<int:pk>/', BestSellerDetail.as_view(), name='BestSellerDetail'),

    path('CustomerList/', CustomerListCreate.as_view(), name='CustomerCreate'),
    path('CustomerEdit/<int:pk>/', CustomerDetail.as_view(), name='CustomerDetail'),

    path('Suppier/', SupplierListCreate.as_view(), name='SuppierList'),
    path('Suppier/<int:pk>/', SupplierDetail.as_view(), name='SuppierDetail'),

    path('Clients/', ClientsListCreate.as_view(), name='ClientsList'),
    path('Clients/<int:pk>/', ClientsDetail.as_view(), name='ClientsDetail'),

    path('FreshOrganics/', FreshOrganicsListCreate.as_view(), name='FreshOrganicsList'),
    path('FreshOrganics/<int:pk>/', FreshOrganicsDetail.as_view(), name='FreshOrganicsDetail'),

    path('Sildes/', SildesListCreate.as_view(), name='SildesList'),
    path('Sildes/<int:pk>/', SildesDetail.as_view(), name='SildesDetail'),

    path('SubTopMenu/', SubTopMenuListCreate.as_view(), name='SubTopMenuList'),
    path('SubTopMenu/<int:pk>/', SubTopMenuDetail.as_view(), name='SubTopMenuDetail'),

    path('TopMenu/', TopMenuListCreate.as_view(), name='TopMenuList'),
    path('TopMenu/<int:pk>/', TopMenuDetail.as_view(), name='TopMenuDetail'),
]
