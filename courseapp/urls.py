from django.contrib import admin
from django.urls import include, path

# http://127.0.0.1:8000/                          => Anasayfa
# http://127.0.0.1:8000/anasayfa                  => Anasayfa
# http://127.0.0.1:8000/iletisim                  => İletişim Sayfası
# http://127.0.0.1:8000/hakkimizda                => Hakkımızda Sayfası
# http://127.0.0.1:8000/kurs                      => Kurs listesi
# http://127.0.0.1:8000/kurs/liste                => Kurs listesi
# http://127.0.0.1:8000/kurs/detay                => Kurs Detay Sayfası
# http://127.0.0.1:8000/kurs/programlama          => Programlama Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/web-gelistirme       => Web Geliştirme Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/mobil-uygulamalar    => Mobil Uygulamalar Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/<>                   => Yanlış Kategori Seçimi

urlpatterns = [
    path('', include('pages.urls')),
    path('kurs/', include('courses.urls')),
    path('admin/', admin.site.urls),
]
