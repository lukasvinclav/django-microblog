from django import forms
from django.contrib import admin

from .models import Category, Post


class PostFormAdmin(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'vLargeTextField fullwidth',
                'rows': 32,
            })
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostFormAdmin
    list_display = ['title', 'slug', 'category', 'is_visible', 'created']
    list_filter = ['is_visible', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = PostFormAdmin
    list_display = ['title', 'created']
