Para Birimi Dönüştürücü Uygulaması
Bu, bir para biriminden diğerine döviz değeri dönüştürmek için basit bir masaüstü uygulamasıdır. Uygulama, Tkinter kütüphanesini kullanıcı arayüzü için ve döviz kuru bilgilerini almak için ExchangeRate-API'yi kullanır.

Özellikler
Birçok desteklenen para birimi arasında döviz değeri dönüştürme.
Tkinter ile oluşturulmuş kullanıcı dostu grafik arayüz.
Girilen miktar için doğrulama.
Güncel döviz kurları ile dönüştürme sonuçlarını görüntüleme.
Desteklenen para birimleri:
USD (Amerikan Doları)
EUR (Euro)
TRY (Türk Lirası)
GBP (İngiliz Sterlini)
JPY (Japon Yeni)
RUB (Rus Rublesi)
AZN (Azerbaycan Manatı)
AED (Birleşik Arap Emirlikleri Dirhemi)

Gereksinimler
Bu uygulamayı çalıştırmak için sisteminizde aşağıdaki yazılımların yüklü olması gerekir:

Python (3.6 veya daha yüksek)
pip (Python paket yöneticisi)

Ayrıca, gerekli Python kütüphanesini yükleyin:
pip install requests

Kullanım
Depoyu klonlayın veya proje dosyalarını indirin:
git clone https://github.com/kullanıcıadınız/para-birimi-dönüştürücü.git
cd para-birimi-dönüştürücü

Scripti çalıştırın:
python currency_converter.py

Miktar alanına dönüştürmek istediğiniz miktarı girin.
Kaynak Para Birimi açılır menüsünden kaynak para birimini seçin.
Hedef Para Birimi açılır menüsünden hedef para birimini seçin.
Dönüştür butonuna tıklayarak dönüşüm sonucunu alın.

Örnek
Eğer miktar alanına 100 girer, kaynak para birimi olarak USD ve hedef para birimi olarak EUR seçerseniz, uygulama en güncel döviz kuru verisini alacak ve şu formatta sonucu gösterecektir:

Kodu kopyala
100 USD = 90.00 EUR

Hata Yönetimi
Eğer girilen miktar geçersizse, "Geçerli bir miktar girin." hata mesajı gösterilecektir.
API bağlantısı ile ilgili bir sorun varsa, "API bağlantısı başarısız!" hata mesajı gösterilecektir.
Seçilen para birimi için döviz kuru bulunamazsa, "Döviz kuru bulunamadı!" hata mesajı gösterilecektir.

Desteklenen Platformlar
Bu uygulama, Python yüklü olan her işletim sisteminde çalışabilir, bunlar arasında:

Windows
macOS
Linux

Katkıda Bulunma
Katkılarınız beklenmektedir! Uygulamayı geliştirmek veya herhangi bir hatayı düzeltmek isterseniz, depoyu çatallayabilir ve bir pull request gönderebilirsiniz.

Lisans
Bu proje, MIT Lisansı altında lisanslanmıştır.

Teşekkürler
ExchangeRate-API döviz kuru verisi sağladığı için teşekkür ederiz.
Python'un Tkinter kütüphanesi kullanıcı arayüzü için kullanılmıştır.
