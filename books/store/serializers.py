from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Book, UserBookRelations


class BookSerializer(ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    annotated_likes = serializers.IntegerField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    max_rating = serializers.IntegerField()
    min_rating = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'price', 'likes_count', 'annotated_likes', 'rating', 'max_rating',
                  'min_rating']

    def get_likes_count(self, instance):
        return UserBookRelations.objects.filter(book=instance, like=True).count()

    # def get_discount_price(self, instance):
    #     ubr = UserBookRelations.objects.filter(book=instance)
    #     return ubr.book.price - ubr.book.discount

class UserBookRelationsSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelations
        fields = ('book', 'like', 'bookmarks', 'rate')
