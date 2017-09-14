from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields 列表你可以明确的告诉框架你想在你的表单中包含哪些字段，或者使用exclude 列表定义你想排除在外的那些字段。
        fields = ('name','email','body')