from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.logins),
    path('adminlogin',views.adminlogin,name="adminloginn"),
    path('home', views.home,name="home"),
    path('view_user', views.view_user,name="view_user"),
    path('view_nutritionist', views.view_nutritionist,name="view_nutritionist"),
    path('add_nutritionist', views.add_nutritionist,name="add_nutritionist"),
    path('add_nutritionist1', views.add_nutritionist1,name="add_nutritionist1"),
    path('view_notification', views.view_notification,name="view_notification"),
    path('add_notification', views.add_notification,name="add_notification"),
    path('add_notification1', views.add_notification1,name="add_notification1"),
    path('edit_notification/<int:id>', views.edit_notification,name="edit_notification"),
    path('edit_notification1/', views.edit_notification1,name="edit_notification1"),
    path('delete_notification/<int:id>', views.delete_notification,name="delete_notification"),
    path('view_healthblog', views.view_healthblog,name="view_healthblog"),
    path('add_healthblog', views.add_healthblog,name="add_healthblog"),
    path('add_healthblog1', views.add_healthblog1,name="add_healthblog1"),
    path('edit_healthblog/<int:id>', views.edit_healthblog,name="edit_healthblog"),
    path('edit_healthblog1/', views.edit_healthblog1,name="edit_healthblog1"),
    path('delete_healthblog/<int:id>', views.delete_healthblog,name="delete_healthblog"),
    path('view_feedback', views.view_feedback,name="view_feedback"),
    path('reply_feedback/<int:id>', views.reply_feedback,name="reply_feedback"),
    path('reply_feedback1', views.reply_feedback1,name="reply_feedback1"),
















    #############################################################
    path('logincode', views.logincode, name="logincode"),
    path('reg', views.reg, name="reg"),
    path('hinfo', views.hinfo, name="hinfo"),




]
