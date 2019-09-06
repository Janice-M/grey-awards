from django import forms
from.models import Article

class NewsLetterForm(forms.Form):
    your_name=forms.CharField(label='Preferred  Name',max_length=30)
    email=forms.EmailField(label='Email')


class NewArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        exclude=['profile','pub_date']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }