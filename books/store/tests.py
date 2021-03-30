from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from rest_framework.generics import ListAPIView

from store.models import Book
from store.serializers import BookSerializer


def operation(a, b, c):
    if c == '+':
        return a + b
    else:
        return a - b


class SomeTest(TestCase):
    def test_plus(self):
        result = operation(10, 2, '+')
        print(result)
        self.assertEqual(result, 12)

    def test_minus(self):
        result = operation(10, 2, '-')
        print(result)
        self.assertEqual(result, 8)


class BookCreateTest(TestCase):
    def test_create(self):
        book = Book.objects.create(title='lonely ranger', authors='Mel Gibson', price=200.00)
        self.assertEqual(book.title, 'lonely ranger')


class UserBookCreate(TestCase):
    def test_user_create(self):
        book = Book.objects.create(title='UserTestCreate', authors='Mike Brawling', price=1500.00)
        book.owner = User.objects.first()
        self.assertEqual(book.owner, User.objects.first(), 'Alright in there')


class BookSerializerTest(TestCase):
    def test_serializer(self):
        book1 = Book.objects.create(title='test_ser1', authors='Alex Volkanovski', price=250, \
                                    description='something to describe')
        book2 = Book.objects.create(title='test_ser2', authors='Shmalex Volkanovski', price=3050,
                                    description='something to describe')

        data = BookSerializer([book1, book2], many=True).data
        print(data)
        self.assertEqual(book1, book2, 'some thing to tell ya')