from django import forms

from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug')
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'image': 'Resim Url',
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
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
            'image' : {
                'required': 'Resim Url alanı zorunludur.',
                'max_length': 'En fazla 50 karakter girilebilir',
            },
        }


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug', 'categories', 'isActive', 'isHome')
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'image': 'Resim Url',
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'slug' : forms.TextInput(attrs={'class':'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class':'form-control'}),
        }
        error_messages = {
            'title' : {
                'required': 'Başlık alanı zorunludur.',
                'max_length': 'En fazla 50 karakter girilebilir',
            },
            'description' : {
                'required': 'Açıklama alanı zorunludur.',
            },
            'image' : {
                'required': 'Resim Url alanı zorunludur.',
                'max_length': 'En fazla 50 karakter girilebilir',
            },
        }


class UploadForm(forms.Form):
    image = forms.ImageField()