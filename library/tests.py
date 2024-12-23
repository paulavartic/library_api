from datetime import date, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from library.models import Author, Book
from library.serializers import BookSerializer
from users.models import User


class AuthorTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@example.com',)

    def test_create_author(self):
        author = Author.objects.create(
            name='N. Gogol',
        )
        self.assertEqual(author.name, 'N. Gogol')


class BookTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@example.com', )
        self.author = Author.objects.create(name='N. Gogol')

    def test_create_book(self):
        book = Book.objects.create(
            title='Viy',
            author=self.author,
            available=True
        )
        self.assertEqual(book.title, 'Viy')
        self.assertEqual(book.author, self.author)
        self.assertTrue(book.available)


class BookSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@example.com', )
        self.author = Author.objects.create(name='N. Gogol')

    def test_valid_data(self):
        data = {'title': 'TestTitle',
                'author': self.author,
                'available': True
                }
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid(), f'Errors: {serializer.errors}')

