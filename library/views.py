from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from library.models import Author, Book, BookIssue
from library.serializers import AuthorSerializer, BookSerializer, BookIssueSerializer, BookDetailSerializer
from users.permissions import IsAdmin, IsOwner


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)


class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated, IsAdmin,)

    def perform_create(self, serializer):
        author = serializer.save()
        author.save()


class AuthorUpdateAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated, IsAdmin,)


class AuthorDestroyAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated, IsAdmin,)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ('author', 'genre', 'available',)
    ordering_fields = ('title', 'author',)
    search_fields = ('title', 'author', 'genre')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer

    def perform_create(self, serializer):
        book = serializer.save()
        book.save()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = (IsAuthenticated, IsAdmin,)
        elif self.action == 'retrieve':
            self.permission_classes = (AllowAny,)
        return super().get_permissions()


class BookIssueListAPIView(ListAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)


class BookIssueCreateAPIView(CreateAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)

    def perform_create(self, serializer):
        book_issue = serializer.save()
        book_issue.book.available = False
        book_issue.user = self.request.user
        book_issue.save()


class BookIssueRetrieveAPIView(RetrieveAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)


class BookIssueUpdateAPIView(UpdateAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)


class BookIssueDestroyAPIView(DestroyAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)
