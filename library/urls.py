from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from library.apps import LibraryConfig
from library.views import (
    BookViewSet,
    AuthorCreateAPIView,
    AuthorListAPIView,
    AuthorUpdateAPIView,
    AuthorDestroyAPIView,
    BookIssueListAPIView,
    BookIssueCreateAPIView, BookIssueRetrieveAPIView, BookIssueUpdateAPIView, BookIssueDestroyAPIView,
)

app_name = LibraryConfig.name

router = SimpleRouter()
router.register('', BookViewSet)


urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(permission_classes=(AllowAny,)), name='authors_list'),
    path('authors/create/', AuthorCreateAPIView.as_view(), name='authors_create'),
    path('authors/<int:pk>/edit/', AuthorUpdateAPIView.as_view(), name='authors_edit'),
    path('authors/<int:pk>/delete/', AuthorDestroyAPIView.as_view(), name='authors_delete'),
    path('issues/', BookIssueListAPIView.as_view(), name='book_issues_list'),
    path('issues/create/', BookIssueCreateAPIView.as_view(), name='book_issues_create'),
    path('issues/<int:pk>/retrieve/', BookIssueRetrieveAPIView.as_view(), name='book_issues_retrieve'),
    path('issues/<int:pk>/edit/', BookIssueUpdateAPIView.as_view(), name='book_issues_edit'),
    path('issues/<int:pk>/delete/', BookIssueDestroyAPIView.as_view(), name='book_issues_delete'),
]

urlpatterns += router.urls
