from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from .models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(instance)



class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):



@api_view(['GET', 'POST'])
def api_posts(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_posts_detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    # напишем обработчик для метода GET
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
        # получаем пользователя из запроса
    user = request.user
        # если пользователь, обратившийся к API, не является автором поста,
    # то к методам, идущим после GET, мы его не пропускаем
    # и возвращаем ответ со статусом 403
    if user != post.author:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def api_groups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_groups_detail(request, pk):
    group = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(group)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def api_comments(request, pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    post = get_object_or_404(Post, pk)
    comments = post.comments.all()
    serializer = CommentSerializer(comments)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_comments_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment = get_object_or_404(Comment, id=)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
        # получаем пользователя из запроса
    user = request.user
    if user != post.author:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)