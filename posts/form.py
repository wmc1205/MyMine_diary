
from posts.models import Post
from django import forms

class PostForm(forms.ModelForm):
    post_content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-start'}))
    class Meta:
        model = Post
        fields = ['post_title','post_image','post_content']



