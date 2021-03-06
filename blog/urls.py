from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('my_cv/', views.my_cv, name = 'my_cv'),
    path('my_cv/edit/', views.my_cv_edit, name = 'my_cv_edit'),

    path('public_cvs_list/', views.public_cvs_list, name = 'public_cvs_list'),
    path('public_cv/<int:pk>/', views.public_cv_detail, name = 'public_cv_detail'),
    path('public_cv/new/', views.public_cv_new, name='public_cv_new'),
    path('public_cv/<int:pk>/edit/', views.public_cv_edit, name='public_cv_edit'),

]