from rest_framework import serializers

from library.models import Author, Book, BookIssue
from library.validators import ReturnValidator


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    def get_books(self, author):
        return [book.title for book in Book.objects.filter(author=author)]

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    books_by_same_author = serializers.SerializerMethodField
    author = AuthorSerializer

    def get_books_by_same_author(self, book):
        return Book.objects.filter(author=book.author)

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'books_by_same_author')


class BookIssueSerializer(serializers.ModelSerializer):
    return_date = serializers.DateField(validators=[ReturnValidator])

    class Meta:
        model = BookIssue
        fields = '__all__'
