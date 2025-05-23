import django_filters
from .models import Post
from django import forms

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    author__user__username = django_filters.CharFilter(
        field_name='author__user__username',
        label='Автор'
    )
    created_at = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата после'
    )

    class Meta:
        model = Post
        fields = ['title', 'author__user__username', 'created_at']
