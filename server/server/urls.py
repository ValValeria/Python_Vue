"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app.views import NotFoundView, PostsView, LogoutView, SignUpView, LoginView, LettersView, PostsSortByCategory, SearchView, CarouselView, PostView, AddLikesView, CommentsView, AddCommentView, GetLikesView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/login', LoginView.as_view()),
    re_path(r'^api/signup', SignUpView.as_view()),
    re_path(r'^api/logout', LogoutView.as_view()),
    re_path(r'^api/posts/(?P<id>\d+)', PostView.as_view()),
    re_path(r'^api/category', PostsSortByCategory.as_view()),
    re_path(r'^api/posts', PostsView.as_view()),
    re_path(r'^api/letter', LettersView.as_view()),
    re_path(r'^api/likes', AddLikesView.as_view()),
    re_path(r'^api/comments', CommentsView.as_view()),
    re_path(r'^api/comment', AddCommentView.as_view()),
    re_path(r'^api/carousel', CarouselView.as_view()),
    re_path(r'^api/user-likes', GetLikesView.as_view()),
    re_path(r'^api/search', SearchView.as_view()),
    re_path(r'^', NotFoundView.as_view())
]
