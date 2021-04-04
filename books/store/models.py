from django.contrib.auth.models import User
from django.db import models

from store.logic import set_rating


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    owner = models.ManyToManyField(User, null=True, related_name='my_books')
    readers = models.ManyToManyField(User, through='UserBookRelations', related_name='books')
    discount = models.IntegerField(null=True, blank=True)
    critic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='critic_book', null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)

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

    def save(self, *args, **kwargs):

        creating = not self.pk
        old_rating = self.rate
        super().save(*args, **kwargs)

        new_rating = self.rate

        if old_rating != new_rating or creating:
            set_rating(self.book)

        set_rating(self, self.book)
