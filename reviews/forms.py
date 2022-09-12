from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Review
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'content': _('Your comment')
        }


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
            'served_as',
            'content',
            'aroma',
            'appearance',
            'taste',
            'aftertaste',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'The name of the beer'
            }),
            'brewery': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'The brewery'
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'The type of the beer - ale, stout, lager, etc'
            }),
            'colour': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'The colour of the beer - pale, dark, golden, etc'
            }),
            'alcohol': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'hops': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'The hops of the beer'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'keywords': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Some words to quickly describe the beer - hoppy, malty, etc'
            }),
            'served_as': forms.RadioSelect(),
            'content': SummernoteWidget(),
            'aroma': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'appearance': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'taste': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'aftertaste': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'name': _('Beer'),
            'alcohol': _('Alcohol content (a number)'),
            'image': _('Picture of the beer'),
            'keywords': _('Descriptors'),
            'served_as': _('How was the beer served? Bottled or draught?'),
            'content': _('Your review (note that the editor will not accept images or videos)'),
            'aroma': _("Rank the beer's aroma (a number from 1 to 10)"),
            'appearance': _("Rank the beer's appearance (a number from 1 to 10)"),
            'taste': _("Rank the beer's taste (a number from 1 to 10)"),
            'aftertaste': _("Rank the beer's aftertaste (a number from 1 to 10)"),
        }
