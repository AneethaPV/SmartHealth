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
    path('edit_nutritionist/<int:id>', views.edit_nutritionist,name="edit_nutritionist"),
    path('edit_nutritionist1/', views.edit_nutritionist1,name="edit_nutritionist1"),
    path('delete_nutritionist/<int:id>', views.delete_nutritionist,name="delete_nutritionist"),

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
    path('search', views.search, name="search"),

    path('view_foodcalories', views.view_foodcalories,name="view_foodcalories"),
    path('add_foodcalories', views.add_foodcalories,name="add_foodcalories"),
    path('add_foodcalories1', views.add_foodcalories1,name="add_foodcalories1"),
    path('delete_foodcalories/<int:id>', views.delete_foodcalories,name="delete_foodcalories"),


    path('view_feedback', views.view_feedback,name="view_feedback"),
    path('reply_feedback/<int:id>', views.reply_feedback,name="reply_feedback"),
    path('reply_feedback1', views.reply_feedback1,name="reply_feedback1"),

    path('graph/<int:id>', views.graph,name="graph"),

    path('view_review', views.view_review,name="view_review"),

    path('nutrreview', views.nutrreview,name="nutrreview"),



















    #############################################################
    path('logincode', views.logincode, name="logincode"),
    path('reg', views.reg, name="reg"),
    path('hinfo', views.hinfo, name="hinfo"),

    path('viewmedcond', views.viewmedcond, name="viewmedcond"),
    path('medcond', views.medcond, name="medcond"),
    path('updatemedcond', views.updatemedcond, name="updatemedcond"),

    path('viewprofile', views.viewprofile, name="viewprofile"),
    path('updateprofile', views.updateprofile, name="updateprofile"),
    path('viewhealth', views.viewhealth, name="viewhealth"),
    path('updatehealth', views.updatehealth, name="updatehealth"),

    path('addrem', views.addrem, name="addrem"),
    path('updaterem', views.updaterem, name="updaterem"),
    path('viewreminder', views.viewreminder, name="viewreminder"),
    path('viewrem', views.viewrem, name="viewrem"),
    path('delreminder', views.delreminder, name="delreminder"),

    path('pics', views.pics, name="pics"),
    # path('hblog', views.hblog, name="hblog"),

    path('addfeedback', views.addfeedback, name="addfeedback"),
    path('nutritionistdata', views.nutritionistdata, name="nutritionistdata"),
    path('nutritionistsearch', views.nutritionistsearch, name="nutritionistsearch"),

    path('foodcal', views.foodcal, name="foodcal"),
    path('foodsearch', views.foodsearch, name="foodsearch"),

    path('adddose', views.adddose, name="adddose"),
    path('viewdose', views.viewdose, name="viewdose"),
    path('ndose', views.ndose, name="ndose"),
    path('editdose', views.editdose, name="editdose"),

    path('notification1', views.notification1, name="notification1"),
    path('reminder1', views.reminder1, name="reminder1"),
    path('rating', views.rating, name="rating"),

    path('predict', views.predict, name="predict"),
    path('predict1', views.predict1, name="predict1"),
]
