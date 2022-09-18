from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class BeerReviewAdmin(SummernoteModelAdmin):

    list_filter = ('approved', 'timestamp', 'brewery', 'type', 'author', 'served_as')
    list_display = ('name', 'type', 'colour', 'brewery', 'served_as', 'author', 'timestamp', 'approved')
    search_fields = ['name', 'brewery', 'type', 'colour', 'hops', 'alcohol', 'content']
    actions = ['approve_beer_review', 'disapprove_beer_review']

    summernote_fields = ('content',)

    def approve_beer_review(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_beer_review(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_filter = ('approved', 'timestamp', 'review', 'author')
    list_display = ('review', 'author', 'content', 'timestamp', 'approved')
    search_fields = ['review', 'author', 'approved']
    actions = ['approve_comment', 'disapprove_comment']

    summernote_fields = ('content',)

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_comment(self, request, queryset):
        queryset.update(approved=False)
