from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books')
    readers = models.ManyToManyField(User, through='UserBookRelations', related_name='books')
    discount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} ~ {self.title}"


class UserBookRelations(models.Model):
    RATE_CHOICES = (
        (1, 'ok'),
        (2, 'fine'),
        (3, 'good'),
        (4, 'amazing'),
        (5, 'incredible'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='users_book')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_user")
    like = models.BooleanField(default=False)
    bookmarks = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.book.title}: {self.user.username}, {self.rate}'
