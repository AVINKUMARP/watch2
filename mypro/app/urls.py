
from django.urls import path

from . import views
urlpatterns = [

    path('',views.index,name='index'),
    # path('watch/<int:watch_id>/',views.details,name='details'),
    # path('add/',views.add_watch,name='add_watch'),
    # path('update/<int:id>/',views.update,name="update"),
    # path('delete/<int:id>/',views.delete,name="delete"),
    path('signup/',views.signup,name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('support/', views.support, name="support"),
    path('mec/', views.mec, name="mec"),
    path('auto/', views.auto, name="auto"),
    path('smt/', views.smt, name="smt"),
    path('qur/', views.qur, name="qur"),
    path('cro/', views.cro, name="cro"),
    path('about/', views.about, name="about"),
    path('details/<int:id>/', views.details, name="details"),
#     path('cart/', views.view_cart, name='view_cart'),
#     path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    ]