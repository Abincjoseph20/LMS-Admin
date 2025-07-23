from django.urls import path
from . import views
from .views import InstructorListView

urlpatterns = [
   path('assign_permissions/<int:user_id>/', views.guest_assign_permissions, name='guest_assign_permissions'),
   path('success_page/<int:user_id>/', views.guest_success, name='guest_success_page'),
   path('profile/edit/', views.profile_edit, name='guest_profile_edit'),
   path('profile/delete/', views.profile_delete, name='guest_profile_delete'),
   
   
   path('guest_add_category/', views.add_category, name='guest_add_category'),
   path('guest_category_list/', views.category_list, name='guest_category_list'), 
   path('guest_update_category/<int:category_id>/', views.update_category, name='guest_update_category'), 
   path('guest_delete_category/<int:category_id>/', views.delete_category, name='guest_delete_category'),
   
   
   path('guest_create_instructor/',views.create_instructor, name='guest_create_instructor'),
   path('guest_Instructor_ListView/',InstructorListView.as_view(), name='guest_InstructorListView'),
   path('guest_update_instructor/update/<int:pk>/', views.update_instructor, name='guest_update_instructor'),
   path('guest_delete_instructor/delete/<int:pk>/', views.delete_instructor, name='guest_delete_instructor'), 
   
   
   path('guest_level_list', views.level_list, name='guest_level_list'),
   path('guest_add_level', views.add_level, name='guest_add_level'),
   path('guest_update_level/<int:pk>/', views.update_level, name='guest_update_level'),
   path('guest_delete_level/<int:pk>/', views.delete_level, name='guest_delete_level'),
   
   
    # language
    path('guest_add_language/', views.add_language, name='guest_add_language'),
    path('guest_language_list', views.language_list, name='guest_language_list'),
    path('guest_update_language/<int:pk>/', views.update_language, name='guest_update_language'),
    path('guest_delete_language/<int:pk>/', views.delete_language, name='guest_delete_language'),
   
   
    #course
    path('guest_add_course', views.add_course, name='guest_add_course'),
    path('guest_course_list/', views.course_list, name='guest_course_list'),
    path('guest_courses/<int:course_id>/edit/', views.update_course, name='guest_update_course'),
    path('guest_courses/<int:course_id>/delete/', views.delete_course, name='guest_delete_course'),
    path('guest_course_detail/<int:course_id>/', views.course_detail, name='guest_course_detail'),
    
    
   # lesson 
    path('guest_add_lesson/', views.add_lesson, name='guest_add_lesson'),
    path('guest_lessons/', views.lesson_list, name='guest_lesson_list'),
    path('guest_update_lesson/<int:lesson_id>/', views.update_lesson, name='guest_update_lesson'),
    path('guest_delete_lesson/<int:lesson_id>/', views.delete_lesson, name='guest_delete_lesson'),
    
    
    # course resources 
    path('guest_resources/add/', views.add_course_resource, name='guest_add_resource'),
    path('guest_resources/', views.resource_list, name='guest_resource_list'),
    path('guest_resources/update/<int:resource_id>/', views.update_course_resource, name='guest_update_resource'),
    path('guest_resources/delete/<int:resource_id>/', views.delete_course_resource, name='guest_delete_resource'),
    
    
    #what you learn
    path('guest_add_what_u_learn/', views.add_what_u_learn, name='guest_add_what_u_learn'),
    path('guest_what_u_learn_list/', views.what_u_learn_list, name='guest_what_u_learn_list'),
    path('guest_update_what_u_learn/edit/<int:entry_id>/', views.update_what_u_learn, name='guest_update_what_u_learn'),
    path('guest_delete_what_u_learn/<int:entry_id>/', views.delete_what_u_learn, name='guest_delete_what_u_learn'),
    
    
    # course requirement
    path('guest_add_requirement/', views.add_requirement, name='guest_add_requirement'),
    path('guest_requirement_list/', views.requirement_list, name='guest_requirement_list'),
    path('guest_update_requirement/<int:requirement_id>/', views.update_requirement, name='guest_update_requirement'),
    path('guest_delete_requirement/<int:requirement_id>/', views.delete_requirement, name='guest_delete_requirement'),
    
    
    # course video file
    path('guest_create_video',views.create_video, name='guest_create_video'),
    path('guest_view_video',views.view_video, name='guest_view_video'),
    path('guest_video_update/<int:video_id>/',views.video_update, name='guest_video_update'),
    path('guest_delete_videos/<int:video_id>/', views.delete_videos, name='guest_delete_videos'),
    
    
    # quiz crud
    path('guest_create_quiz/', views.create_quiz, name='guest_create_quiz'),
    path('guest_quiz/<int:quiz_id>/add_questions/', views.add_questions, name='guest_add_questions'),
    path('guest_list_quiz/', views.list_quiz, name='guest_list_quiz'),
    path('guest_delete_quiz/<int:quiz_id>', views.delete_quiz, name='guest_delete_quiz'),
    path('guest_edit_quiz/<int:quiz_id>', views.edit_quiz, name='guest_edit_quiz'),
    
    
    # quiz results
    path('guest_quiz_results/<int:quiz_id>', views.get_quiz_results_for_course, name='guest_quiz_results'),
    path('guest_verify_result/<int:quiz_result_id>', views.verify_result, name='guest_verify_result'),
    # path('Instructor_ListView/',InstructorListView.as_view(), name='InstructorListView'),
    
    
    
]