from django.urls import path
from rest_framework.routers import SimpleRouter

from library.apps import LibraryConfig
from library.views import (
    BookViewSet,
    BookCreateAPIView,
    BookRetrieveAPIView,
    BookUpdateAPIView,
    BookDestroyAPIView,
    AuthorCreateAPIView,
    AuthorListAPIView,
    AuthorUpdateAPIView,
    AuthorDestroyAPIView,
    BookIssueListAPIView,
    BookIssueCreateAPIView,
)

app_name = LibraryConfig.name

router = SimpleRouter()
router.register('', BookViewSet)


urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name='authors_list'),
    path('authors/create/', AuthorCreateAPIView.as_view(), name='authors_create'),
    path('authors/<int:pk>/edit/', AuthorUpdateAPIView.as_view(), name='authors_edit'),
    path('authors/<int:pk>/delete/', AuthorDestroyAPIView.as_view(), name='authors_delete'),
    path('books/create/', BookCreateAPIView.as_view(), name='books_create'),
    path('books/<int:pk>/', BookRetrieveAPIView.as_view(), name='books_retrieve'),
    path('books/<int:pk>/edit/', BookUpdateAPIView.as_view(), name='books_edit'),
    path('books/<int:pk>/delete/', BookDestroyAPIView.as_view(), name='books_delete'),
    path('issues/', BookIssueListAPIView.as_view(), name='books_issues_list'),
    path('issues/create/', BookIssueCreateAPIView.as_view(), name='books_issues_create'),
]

urlpatterns += router.urls
