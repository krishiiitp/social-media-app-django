from django.contrib import admin
from django.urls import path
from django.conf import settings
from userauth import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup/',views.signup),
    path('login/',views.loginn),
    path('logout/',views.logoutt),
    path('upload',views.upload),
    path('like-post/<str:id>',views.likes,name='like-post'),
    path('#<str:id>',views.home_posts),
    path('explore',views.explore),
    path('profile/<str:id_user>',views.profile),
    path('follow',views.follow,name='follow'),
    path('search-results/', views.search_results, name='search_results'),
]