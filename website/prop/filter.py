from prop.models import proper
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model =proper
        fields = ['location', 'price', 'area' ]
