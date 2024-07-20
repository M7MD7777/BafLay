from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryViews, ProductViews, UserViews, BrancheView,views,ParentCategpryView

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("register/", UserViews.register, name="register"),

    path('branche/create/', BrancheView.branche_create, name='branche_create'),
    path('branche/', BrancheView.branche_list, name='branche_list'),
    path('branche/update/<int:pk>/', BrancheView.branche_update, name='branche_update'),
    path('branche/delete/<int:pk>', BrancheView.branche_delete, name='branche_delete'),


    path('parent_category/create/', ParentCategpryView.parent_category_create, name='parent_category_create'),
    path('parent_category/', ParentCategpryView.parent_categories_list, name='parent_category_list'),
    path('parent_category/update/<int:pk>/', ParentCategpryView.parent_category_update, name='parent_category_update'),
    path('parent_category/delete/<int:pk>', ParentCategpryView.parent_category_delete, name='parent_category_delete'),

 
    path('category/create/', CategoryViews.category_create, name='category_create'),
    path('category/', CategoryViews.categories_list, name='category_list'),
    path('category/update/<int:pk>/', CategoryViews.category_update, name='category_update'),
    path('category/delete/<int:pk>', CategoryViews.category_delete, name='category_delete'),



    path('product/product/', ProductViews.product_create, name='product_create'),
    path('product/', ProductViews.product_list, name='product_list'),
    path('product/update/<int:pk>/', ProductViews.product_update, name='product_update'),
    path('product/delete/<int:pk>', ProductViews.product_delete, name='product_delete'),


    path('branche/<int:branche_id>/', views.branche_categories, name='branche_categories'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('parent_category/<int:parent_category_id>/', views.parent_category_items, name='parent_category_items'),
    
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
