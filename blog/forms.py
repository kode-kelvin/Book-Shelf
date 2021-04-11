from django import forms
from .models import Comment, Category, Post


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


# defing the list
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


# for status

choice = [('Draft', 'Draft'), ('Published', 'Published')]


class BookForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'slug', 'publish', 'category', 'author', 'book_author', 'cover', 'pdf', 'content', 'status')

        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'status': forms.Select(choices=choice, attrs={'class': 'form-control'}),
        }
