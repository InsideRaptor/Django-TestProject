from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('first-cat/', views.first_cat_view, name='first_cat'),
    path('second-cat/', views.second_cat_view, name='second_cat'),
    path('adds/', views.adds_view, name='adds'),
]
