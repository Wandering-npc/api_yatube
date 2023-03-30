from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise Response(status=status.HTTP_403_FORBIDDEN)
        super(PostViewSet, self).perform_update(serializer)
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise Response(status=status.HTTP_403_FORBIDDEN)
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_querryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id)'))
        return post.comments.all()
    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id)'))
        serializer.save(author=self.request.user, post=post)
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        super().perform_update(serializer)
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)


