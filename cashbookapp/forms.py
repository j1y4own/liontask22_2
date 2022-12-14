from django import forms
from .models import Cashbook, Comment

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title','content','email','url','created_at','image']

    def __init__(self, *args, **kwargs):
        super(CashbookForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False       
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['email'].widget.attrs['readonly'] = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']