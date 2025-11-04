from django import forms


class CourseCreateForm(forms.Form):
    title = forms.CharField()       # hepsi için default required = True
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.SlugField()
