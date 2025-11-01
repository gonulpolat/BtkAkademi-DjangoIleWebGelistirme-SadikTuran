from django.contrib import admin
from django.urls import include, path

# http://127.0.0.1:8000/                                   => Anasayfa
# http://127.0.0.1:8000/anasayfa                           => Anasayfa
# http://127.0.0.1:8000/iletisim                           => İletişim Sayfası
# http://127.0.0.1:8000/hakkimizda                         => Hakkımızda Sayfası
# http://127.0.0.1:8000/kurs                               => Kurs listesi
# http://127.0.0.1:8000/kurs/liste                         => Kurs listesi
# http://127.0.0.1:8000/kurs/<>                            => <> Detay Sayfası
# http://127.0.0.1:8000/kurs/kategori/programlama          => Programlama Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/web-gelistirme       => Web Geliştirme Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/mobil-uygulamalar    => Mobil Uygulamalar Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/<1>                  => Programlama Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/<2>                  => Web Geliştirme Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/<3>                  => Mobil Uygulamalar Kategorisine Ait Kurslar
# http://127.0.0.1:8000/kurs/kategori/<str:>               => Yanlış Kategori Seçimi
# http://127.0.0.1:8000/kurs/kategori/<int:>               => Programlama Kategorisine Ait Kurslar

urlpatterns = [
    path('', include('pages.urls')),
    path('kurs/', include('courses.urls')),
    path('admin/', admin.site.urls),
]
