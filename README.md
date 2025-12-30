# Gym Management System (Python OOP)

Bu proje, **Nesne Tabanlı Programlama (OOP)** prensiplerini uygulamalı olarak hayata geçirmek amacıyla geliştirilmiş bir spor salonu üye ve ödeme takip sistemidir. OOP mantığını pekiştirmek için tasarlanmıştır.

## Proje Özellikleri
* **Üye Yönetimi:** Yeni üye kaydı, üye silme ve ID tabanlı sorgulama.
* **Otomatik Tarih Hesaplama:** Seçilen pakete göre (1, 3, 6, 12 ay) bitiş tarihinin `datetime` kütüphanesi ile otomatik belirlenmesi.
* **Kasa Raporu:** Yapılan tüm işlemlerin loglanması ve toplam cironun anlık takibi.
* **Esnek Süre Uzatma:** Mevcut üyelerin paket yenileme işlemlerinin yönetilmesi.
* **Encapsulation:** Veri güvenliği için değişkenler `_` (protected) erişim belirleyicisi ile tanımlanmış, verilere erişim `getter` ve `setter` metodları ile sağlanmıştır.
* **Composition:** `SporSalonu` sınıfı, `Uye` ve `OdemeIslemi` nesnelerini kendi bünyesinde barındırarak nesneler arası hiyerarşik bir ilişki kurar.
* **Validation:** Telefon numarası ve e-posta formatları için özel kontrol döngüleri eklenmiştir.
