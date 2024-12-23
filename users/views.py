from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User, Donation
from users.serializers import UserSerializer, DonationSerializer
from users.services import create_stripe_price, create_stripe_session


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class DonationCreateAPIView(CreateAPIView):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount = create_stripe_price(payment.amount)
        session_id, payment_link = create_stripe_session(amount)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
