from django import forms

from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = ('__all__')
        fields = ('title', 'description', 'imageUrl', 'slug')
