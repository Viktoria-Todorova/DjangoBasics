# from datetime import date
#
from typing import Any

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError

from books.models import Book, Tag
from common.mixins import DisableFormMixin


#
# from books.models import Book
#
#
# class BookFormBasic(forms.Form):
#     title = forms.CharField(max_length=100,
#                             # error_messages= {},
#                            widget=forms.TextInput(attrs={'placeholder': 'e.g Done'}))
#     price = forms.DecimalField(max_digits=6, decimal_places=2, min_value=0,
#                                widget=forms.NumberInput(attrs={'step': '0.1'}),
#                                label='Price (USD)')
#
#     isbn = forms.CharField(max_length=12,
#                            min_length=10,)
#     genre = forms.ChoiceField(
#         choices=Book.GenreChoices.choices,
#         widget=forms.RadioSelect,
#     )
#
#     publishing_date = forms.DateField(
#         initial=date.today(),
#     )
#
#     description = forms.CharField(
#         widget=forms.Textarea,
#     )
#     image_url = forms.URLField()
#     publisher= forms.CharField(max_length=100,)


class BookFormBasic(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    field_order = ['title','pages','price']
    class Meta:
        # fields= "__all__"
        exclude = ["slug"]
        model = Book

        error_messages = {
            'title' :{
                'max_length' : "The title is too long",
                "required" :"Hey you missed the title",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['tags'].queryset = Tag.objects.all()
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))

    #todo exercise it
    def clean_isbn(self):  #todo
        isbn =self.cleaned_data['isbn']
        if isbn.startswith('978'):
            raise ValidationError("The ISBN cannot start with '978'")
        return isbn

    def clean(self) ->dict:
        cleaned= super().clean()
        genre =cleaned.get('genre')
        pages =cleaned.get('pages')
        if pages < 10 and genre == Book.GenreChoices.FICTION:
            raise ValidationError(f"Book of type {Book.GenreChoices.FICTION} cannot have pages less than 10")
        return cleaned

    def save(self,commit =True):
        if self.instance.publisher:
            self.instance.publisher = self.instance.publisher.capitalize()

        # if commit:
        #     self.instance.save()
        return super().save(commit=commit)



class BookCreateForm(BookFormBasic):
    ...
class BookEditForm(BookFormBasic):
    ...
class BookDeleteForm(DisableFormMixin,BookFormBasic):
   ...

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label="",
        required=False,
    )