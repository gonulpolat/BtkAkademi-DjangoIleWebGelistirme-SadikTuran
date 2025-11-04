from django import forms


class CourseCreateForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': 'Başlık zorunlu bir alandır.'
        },
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    # label'a class özelliği atayabiliyorsun (course-create.html sayfasında)
    # fakat input'a ekleyemiyorsun
    # onu da burda widget üzerinden ekliyorsun. zaten Charfield'in varsayılan widget özelliği TextInput. class özelliği eklemek için yazılıyor.    

    description = forms.CharField(
        error_messages={
            'required': 'Açıklama zorunlu bir alandır.'
        },
        widget=forms.Textarea(attrs={'class':'form-control'})
    )

    imageUrl = forms.CharField(
        error_messages={
            'required': 'Resim zorunlu bir alandır.'
        },
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    slug = forms.SlugField(
        error_messages={
            'required': 'Slug zorunlu bir alandır.'
        },
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
