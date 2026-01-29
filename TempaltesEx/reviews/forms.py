from django import forms

from common.mixins import DisableFormMixin
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'body', 'rating', 'book', 'is_spoiler']


class ReviewCreateForm(ReviewForm):
    pass


class ReviewEditForm(ReviewForm):
    pass


class ReviewDeleteForm(DisableFormMixin,ReviewForm):
    ...
