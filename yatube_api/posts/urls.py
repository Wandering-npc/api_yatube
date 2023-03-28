from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter


import .views
from .views import PostViewSet


router = SimpleRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups/', GroupViewSet)
router.register('')

urlpatterns = [    
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/', api_posts),
    path('api/v1/posts/{post_id}/', api_posts_detail),
    path('api/v1/groups/', api_groups),
    path('api/v1/groups/{group_id}/', api_groups_detail),
    path('api/v1/posts/{post_id}/comments/', api_comments),
    path('api/v1/posts/{post_id}/comments/{comment_id}/', api_comments_detail),
]
