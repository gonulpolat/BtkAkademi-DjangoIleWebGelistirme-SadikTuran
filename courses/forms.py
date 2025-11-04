from django import forms

from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = '__all__'   (az önce yanlış yazmışım parantez olmayacak sorry)
        fields = ('title', 'description', 'imageUrl', 'slug')
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'imageUrl': 'Resim Url',
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'imageUrl' : forms.TextInput(attrs={'class':'form-control'}),
            'slug' : forms.TextInput(attrs={'class':'form-control'}),
        }
        # widgets eklenme sebebi class özelliği eklemek
