from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        # укажите поля, доступные только для чтения
        read_only_fields = ('author')
        model = Post
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description',)
        model = Group
class CommentSerializer(serializers.Model.Serializer):
    class Mets:
        fields= ('id', 'text', 'author', 'created')
        read_only_fields = ('author',)
        model = Comment
