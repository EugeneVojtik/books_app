from django.db.models import Avg

from store.models import UserBookRelations


def set_rating(book):
    rating = UserBookRelations.objects.filter(book=book).aggregate(rating=Avg('rate'))
    book.rating = rating
    book.save()