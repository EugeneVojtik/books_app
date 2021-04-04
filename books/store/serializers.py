from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Book, UserBookRelations

class BookReaderSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class BookSerializer(ModelSerializer):
    #likes_count = serializers.SerializerMethodField()
    annotated_likes = serializers.IntegerField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    owner_name = serializers.CharField(source='critic.username', default='', read_only=True)
    readers = BookReaderSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'price', 'annotated_likes', 'rating', 'owner_name', 'readers']


    # def get_likes_count(self, instance):
    #     return UserBookRelations.objects.filter(book=instance, like=True).count()

class UserBookRelationsSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelations
        fields = ('book', 'like', 'bookmarks', 'rate')
