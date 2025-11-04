from django import forms

from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
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
        error_messages = {
            'title' : {
                'required': 'Başlık alanı zorunludur.',
                'max_length': 'En fazla 50 karakter girilebilir',
            },
            'description' : {
                'required': 'Açıklama alanı zorunludur.',
            },
            'imageUrl' : {
                'required': 'Resim Url alanı zorunludur.',
                'max_length': 'En fazla 50 karakter girilebilir',
            },
        }
