from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class BeerReviewAdmin(SummernoteModelAdmin):
    """
    Controls properties of beer review table in admin panel
    Allows filtering by fields in list_filter
    Sets what fields are visible in the table in list_display
    Controls what fields are included in searches
    Determines what actions are allowed in actions
    Sets the content field to be a Summernote Rich Text Editor
    """

    list_filter = ('approved', 'timestamp', 'brewery', 'type', 'author', 'served_as')
    list_display = ('name', 'pk', 'type', 'colour', 'brewery', 'served_as', 'author', 'timestamp', 'approved')
    search_fields = ['name', 'brewery', 'type', 'colour', 'hops', 'alcohol', 'content']
    actions = ['approve_beer_review', 'disapprove_beer_review']

    summernote_fields = ('content',)

    def approve_beer_review(self, request, queryset):
        """
        Allows mass approval of beer reviews
        I.e, the approved field of all selected reviews is set to True
        Useful for approving several reviews at once
        """
        queryset.update(approved=True)

    def disapprove_beer_review(self, request, queryset):
        """
        Allows mass disapproval of beer reviews
        I.e, the approved field of all selected reviews is set to False
        Useful for removing several reviews at once
        """
        queryset.update(approved=False)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Controls properties of comments table in admin panel
    Allows filtering by fields in list_filter
    Sets what fields are visible in the table in list_display
    Controls what fields are included in searches
    Determines what actions are allowed in actions
    Sets the content field to be a Summernote Rich Text Editor
    """
    list_filter = ('approved', 'timestamp', 'review', 'author')
    list_display = ('review', 'author', 'content', 'timestamp', 'approved')
    search_fields = ['review', 'author', 'approved']
    actions = ['approve_comment', 'disapprove_comment']

    summernote_fields = ('content',)

    def approve_comment(self, request, queryset):
        """
        Allows mass approval of comments
        I.e, the approved field of all selected comments is set to True
        Useful for approving several comments at once
        """
        queryset.update(approved=True)

    def disapprove_comment(self, request, queryset):
        """
        Allows mass disapproval of comments
        I.e, the approved field of all selected comments is set to False
        Useful for removing several comments at once
        """
        queryset.update(approved=False)
