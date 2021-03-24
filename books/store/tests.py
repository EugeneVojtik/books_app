from django.test import TestCase


# Create your tests here.
from store.models import Book


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
        result = operation(10, 2,  '-')
        print(result)
        self.assertEqual(result, 8)

class BookCreateTest(TestCase):
    def test_create(self):
        book = Book.objects.create(title='lonely ranger', authors='Mel Gibson', price=200.00)
        self.assertEqual(book.title,'lonely ranger')
