from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField()
    isActive = models.BooleanField()
    #slug = models.SlugField(null=True)  # Zaten veri tabanı oluşturuldu. slug alanı sonradan eklendiği ve null değer kabul etmeyecği için null parametresine True geçiyorsun ya da 
    slug = models.SlugField(default="", null=False)  # Bu durumda da zaten var olan kayıtlar default değeri alacağı için null=False diyebilirsin

    
    def save(self, *args, **kwargs):
        #save methodu çalıştığında slug alanları otomatik yazdırılır
        self.slug = slugify(self.title)
        super().save(args, kwargs)


    def __str__(self):
        return f"{self.title}"
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"
