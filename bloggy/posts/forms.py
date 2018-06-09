from django import forms

class CommentForm(forms.Form):
    body =  forms.CharField(widget=forms.Textarea, label='Your comment', max_length=1000)