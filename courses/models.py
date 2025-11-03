from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True, max_length=50)


    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)  # Admin paneli Add Course'ta date alanı görünmez, tabi Course Change'de de görünmez
    isActive = models.BooleanField()
    """
        blank = True   : admin panelindeki formda slug alanı boş bırakılabilir.
        editable=False : zaten slug alanı save methodu ile kaydediliyor, sen slug alanına herhangi bir değer yazsan da kendi otomatik değer veriyor. bu nedenle slug alanına yazı yazılamasın. kurs ekleme panelinde artık slug alanı görünmez.
    """
    slug = models.SlugField(default="",blank=True, null=False, unique=True, db_index=True)
    """
        CASCADE     : Bir kategori silinirse onunla ilgili kurs da silinir
        SET_NULL    : Bir kategori silinirse kurstaki category_id kolonuna null değeri atanır. bunu kullanmak için null=True demen gerekli, çünkü category kolonu varsayılan olarak null kabul etmiyor
        SET_DEFAULT : Bir kategori silindiğinde kurstaki category_id kolonuna default bir değer atanır. bunun için de default parametresini tanımlaman gerekli.
        * Database'de alanın adı category_id olarak gitse de shell üzerinde işlem yaparken category olarak kullanılır.
    """
    category = models.ForeignKey(Category, default=2, on_delete=models.CASCADE, related_name="kurslar") # default parametresinin sebebi veri tabanında kayıtların olması


    def __str__(self):
        return f"{self.title}"
