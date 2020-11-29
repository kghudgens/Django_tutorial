from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    # The home page now shows all of the posts according to the list view
    path('', PostListView.as_view(), name='blog-home'),
    # created a path that uses primary key to route the individual data entries
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    # Now includes a view to create posts
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'), 

]