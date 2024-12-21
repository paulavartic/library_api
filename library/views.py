from rest_framework.viewsets import ModelViewSet

from library.models import Author, Book, BookIssue
from library.serializers import AuthorSerializer, BookSerializer, BookIssueSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookIssueViewSet(ModelViewSet):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer

