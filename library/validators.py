from datetime import date, timedelta

from rest_framework import serializers


class ReturnValidator:
    def __call__(self, value):
        if value.get('return_date') > (date.today() + timedelta(days=15)):
            raise serializers.ValidationError('You can not keep a book longer than for 15 days.')
