from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):
    """
        This is a form for adding a post by a user.
        Fields: title - title of the blog
                content - content of the blog
    """

    error_messages = {
        'title_length': "Title should be between 1 and 50 characters long.",
        'content_length': "Content should be of maximum length 1000."
    }

    title = forms.CharField(label='Title', max_length=50, help_text='Enter title of the post')
    content = forms.CharField(label='Content', max_length=1000, help_text='Enter Content of the post', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title)<1 and len(title)>50:
            raise ValidationError(
                self.error_messages['title_length'],
                code = 'title_length'
            )
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content and len(content)<1 and len(content)>1000:
            raise ValidationError(
                self.error_messages['content_length'],
                code = 'content_length'
            )
        return content

    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     post.set_title(self.cleaned_data["title"])
    #     post.set_content(self.cleaned_data["content"])
    #     if commit:
    #         post.save()
    #     return post