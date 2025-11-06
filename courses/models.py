from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True, max_length=50)


    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default="")
    description = RichTextField()
    image = models.ImageField(upload_to='images', default='')   # default parametresini tanımlamamın sebebi veri tabanında kayıtları olması
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True, null=False, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"


class UploadModel(models.Model):
    image = models.ImageField(upload_to='images')      # uploads klasörü içine images klasörü ekle onun içine dosyaları yaz.
    # uploads klasörünü ben oluşturmadım
    # settings dosyası içine MEDIA_ROOT yazdım ve uploads klasörü bu şekilde oluştu