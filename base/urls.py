from django.urls import path

from . import views
urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('register' , views.registerUser,name="register"),
    path('',views.home,name="home"),
    path('profile/<str:pk>',views.userProfile ,name="profile"),
    path('room/<str:pk>',views.room , name="room"),
    path('creat-room/',views.creatRoom,name="creat-room"),
    path('update-room/<str:pk>',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>',views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>',views.deleteMessage,name="delete-message"),
    path('update-user/',views.updateUser,name="update-user"),
    path('topics/',views.topicPage,name="topics"),
    path('activity/',views.activityPage,name="activity"),



]