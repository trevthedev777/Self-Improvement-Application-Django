from django.contrib import admin
from .models import Post, Reply
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['content', 'title']


@admin.register(Reply)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'content', 'status', 'created_on')
    list_filter = ['created_on']
    search_fields = ['name', 'email_address', 'body']

