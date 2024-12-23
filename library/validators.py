# from datetime import date, timedelta
#
# from rest_framework import serializers
#
#
# class ReturnValidator:
#     def __call__(self, value):
#         max_allowed_date = value.get('issue_date') + timedelta(days=15)
#         if value.get('return_date'):
#             if value.get('return_date') > max_allowed_date:
#                 raise serializers.ValidationError('Return date cannot be later than {max_allowed_date}.')
#         return None


    # def __call__(self, value):
    #     if value.get('return_date'):
    #         max_allowed_date = (value.get('issue_date') + timedelta(days=15))
    #         if value.get('return_date') > max_allowed_date:
    #             raise serializers.ValidationError(f"Return date cannot be later than {max_allowed_date}.")


