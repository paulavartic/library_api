from datetime import timedelta, date

from django.db import models

from users.models import NULLABLE, User


class Author(models.Model):
    """Author model."""
    name = models.CharField(
        verbose_name='Author',
        help_text='Enter the name of the author',
        max_length=255,
    )
    biography = models.TextField(
        verbose_name='Biography of the author',
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book model."""
    title = models.CharField(
        verbose_name='Title',
        help_text='Enter the title of the book',
        max_length=300,
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Author',
    )
    genre = models.CharField(
        verbose_name='Genre',
        help_text='Enter the genre of the book',
        max_length=150,
    )
    publication_date = models.DateField(
        verbose_name='Date of publication',
        **NULLABLE,
    )
    available = models.BooleanField(
        default=True,
        verbose_name='Availability'
    )

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class BookIssue(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='Book',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
    )
    issue_date = models.DateField(
        auto_now_add=True,
        verbose_name='Issue Date',
    )
    return_date = models.DateField(
        verbose_name='Return date',
        default=(date.today() + timedelta(days=15))
    )

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'

    def __str__(self):
        return f'{self.book.title} issued to {self.user.username}'
