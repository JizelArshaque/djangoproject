from django. urls import path
from . import views
app_name='app8'
urlpatterns=[
    path('',views.index,name='hello'),
    path('gallery/',views.gallery,name='gallery'),
    path('pic1/<int:id>',views.pic1,name='pic1'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('logout',views.logout,name='logout'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
]
