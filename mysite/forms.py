from django import forms
from django.forms import DateInput

from mysite.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content')


class DateHistoryForm(forms.Form):
    history_date = forms.DateTimeField(label='Point of date', widget=DateInput(attrs={'type': 'date'}))
