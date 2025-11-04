from django import forms


class CourseCreateForm(forms.Form):
    title = forms.CharField(label='Başlık', error_messages={
        'required': 'Başlık zorunlu bir alandır.'
    })     
    description = forms.CharField(widget=forms.Textarea, label='Açıklama', error_messages={
        'required': 'Açıklama zorunlu bir alandır.'
    })
    imageUrl = forms.CharField(label='Resim Url', error_messages={
        'required': 'Resim zorunlu bir alandır.'
    })
    slug = forms.SlugField(error_messages={
        'required': 'Slug zorunlu bir alandır.'
    })
