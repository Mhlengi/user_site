from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet

User = get_user_model()


class UserFilterSet(FilterSet):
    class Meta:
        model = User
        fields = {
            'email': ['iexact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }
