from django.contrib import admin
from .models import Review, Comment

@admin.register(Review)
class BeerReviewAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'timestamp', 'brewery', 'type', 'author')
    list_display = ('name', 'type', 'brewery', 'timestamp', 'approved', 'author')
    search_fields = ['name', 'brewery', 'type', 'colour', 'hops', 'alcohol', 'content']
    actions = ['approve_beer_review']

    def approve_beer_review(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'timestamp', 'review', 'author')
    list_display = ('review', 'author', 'content', 'timestamp', 'approved')
    search_fields = ['review', 'author', 'approved']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
