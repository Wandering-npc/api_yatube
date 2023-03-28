from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter




from .views import PostViewSet, GroupViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [    
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]