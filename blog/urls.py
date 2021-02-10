from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('paper/<int:paper_id>/', views.paper_download, name='paper_download')
]
