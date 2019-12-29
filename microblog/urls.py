from django.urls import path

from .views import PostDetailView, PostListView


app_name = 'microblog'

urlpatterns = [
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('', PostListView.as_view(), name='list')
]
