from rest_framework import serializers
from .models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        # укажите поля, доступные только для чтения
        read_only_fields = ('author',)
        model = Post
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description',)
        model = Group
class CommentSerializer(serializers.Model.Serializer):
    class Mets:
        fields= ()
        model = Comment