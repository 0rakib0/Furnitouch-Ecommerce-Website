from django.urls import path
from . import views

app_name='Admin_app'


urlpatterns = [
    path('Dashbord/', views.Admin_dashbord, name='dashbord'),
    
    # ============================> Product <======================================
    path('add-product/', views.Add_New_Product, name='add_product'),
    path('product-list/', views.ProductList, name='product_list'),
    path("update-product/<slug:slug>/", views.UpdateProduct, name="update_product"),
    path("delete-product/<slug:slug>/", views.DeleteProduct, name="product_delete"),
    
    # ============================> Main Category <======================================
    path('add-main-category/', views.Add_main_category, name='add_main_category'),
    path('view-main-category/', views.View_main_cat, name='view_main_cat'),
    path('update-main-category/<slug:slug>/', views.Update_main_cat, name='update_main_cat'),
    path('Delete-main-category/<slug:slug>/', views.Del_main_cat, name='delete_main_cat'),
    
    
    # ============================> Category <======================================
    path('Add-Category/', views.Add_category, name='add_category'),
    path('view-category/', views.View_Category, name='view_category'),
    path('update-category/<slug:slug>/', views.Update_cat, name='update_cat'),
    path('Delete-category/<slug:slug>/', views.Del_cat, name='del_cat'),
    
    path('add-sub-category/', views.Add_sub_category, name='add_sub_cat'),
    path('view-sub-category/', views.View_sub_Cat, name='view_sub_cat'),
    path('update-sub-category/<slug:slug>/', views.Update_sub_cat, name='Update_sub_cat'),
    path('delete-sub-category/<slug:slug>/', views.Del_sub_cat, name='delete_sub_cat'),
    
    
    
    # ============================> Staff <======================================
    path('Add-staff/', views.Add_Staff, name='add_staff'),
    path('staff-list/', views.Staff_List, name='staff_list'),
    path('User-deyails/<int:id>/', views.View_user_info, name='user_details'),
    path('Delete-User/<int:id>/', views.Delete_user, name='delete_user'),
    
    # ============================> Orders <=====================================
    path('Pending-Order-List/', views.Pending_Order_List, name='pending_order_list'),
    path('Delivered-Order-List/', views.Delivered_order_list, name='delivered_order_list'),
    path('Order-details/<int:id>/', views.Order_details, name='order_details'),
    path('Order-delivery/<int:id>/', views.Order_delivery, name='order_delivery'),
    
    # ============================> Banner <====================================
    path('add-product-page-banner/', views.ProductPageBannerr, name='product_page_banner'),
    path('add-home-page-banner/', views.HomePageBenner, name='home_page_banner'),
    path('offer-banner-list/', views.Banner_List, name='banner_list'),
    path('delete-banner/<int:id>/', views.Delete_banner, name='delete_banner'),
    
    # ============================> Customar <===================================
    path('customars/', views.CustomarList, name='customar_list'),
    
    # ============================> Sales Report <===============================
    path('sales-report/', views.SalesReport, name='sale_report'),
    
    # ============================> Order Traking <==============================
    path('order-traking/', views.TrackOrder, name='track_order'),
    path('add-order-traking/<int:Orderid>/', views.AddTrackingOrder, name='add_traking_order'),
    path('order-traking-update/<int:id>/', views.TrackingUpdate, name='traking_update'),
    
    # ============================> Product View <===============================
    path('product-review-list/', views.Reviews, name='product_review'),
    path('approve-review/<int:id>/', views.ReviewApprove, name='review_approve'),
    path('review-delete/<int:id>/', views.DeleteReview, name='delete_review')
]
