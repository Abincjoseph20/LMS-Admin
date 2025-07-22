from django.urls import path
from . import views

urlpatterns = [
   path('assign_permissions/<int:user_id>/', views.guest_assign_permissions, name='guest_assign_permissions'),
   path('success_page/<int:user_id>/', views.guest_success, name='guest_success_page'),
   path('profile/edit/', views.profile_edit, name='guest_profile_edit'),
   path('profile/delete/', views.profile_delete, name='guest_profile_delete'),
   
   
   path('guest_add_category/', views.add_category, name='guest_add_category'),
   path('guest_category_list/', views.category_list, name='guest_category_list'), 
   path('guest_update_category/<int:category_id>/', views.update_category, name='guest_update_category'), 
   path('guest_delete_category/<int:category_id>/', views.delete_category, name='guest_delete_category'),
   
   
   
]