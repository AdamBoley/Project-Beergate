from .models import Comment, Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'name',
            'brewery',
            'type',
            'colour',
            'alcohol',
            'hops',
            'image',
            'keywords',
            'content',
            'aroma',
            'appearance',
            'taste',
            'aftertaste',
        )
