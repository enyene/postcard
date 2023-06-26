"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import (
    PostListView,
    PostTagListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = "post"

urlpatterns = [
    path('', PostListView.as_view(), name='list'),

    path('tag/<slug:tag>/', PostTagListView.as_view(), name='tag'),

    path('photo/<int:pk>/', PostDetailView.as_view(), name='detail'),

    path('photo/create/', PostCreateView.as_view(), name='create'),

    path('photo/<int:pk>/update/', PostUpdateView.as_view(), name='update'),

    path('photo/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
