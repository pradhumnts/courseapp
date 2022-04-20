from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.course, name='course'),
    path('profile/', views.profile, name='profile'),
    path('pricing/', views.pricing, name='pricing'),
    path('course-list/', views.course_list, name='course-list'),
] 

