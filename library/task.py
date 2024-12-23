from celery import shared_task
from django.core.mail import send_mail

from config import settings
from library.models import BookIssue
from users.models import User


@shared_task
def send_confirmation(email):
    """Sends email confirmation."""
    send_mail(
         subject='Issue confirmation',
         message='Hello! Thank you for choosing us. Do not forget to return the book on time.',
         from_email=settings.EMAIL_HOST_USER,
         recipient_list=[email],
    )
