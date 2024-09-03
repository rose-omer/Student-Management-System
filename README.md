# Öğrenci Yönetim Sistemi

Bu proje, Python ve Tkinter kullanarak geliştirilmiş bir Öğrenci Yönetim Sistemi uygulamasıdır. Uygulama, kullanıcıların öğrenci bilgilerini ekleyebileceği, güncelleyebileceği, silebileceği, arayabileceği ve bu bilgileri bir CSV dosyasına aktarabileceği bir masaüstü uygulamasıdır. Ayrıca, uygulamaya erişim için bir giriş (login) ekranı bulunmaktadır. Veriler, MySQL veritabanında saklanmaktadır.

## Özellikler

- **Öğrenci Ekleme:** Kullanıcılar, yeni öğrenci bilgilerini (Ad, Soyad, TC Kimlik No, Doğum Tarihi, Telefon Numarası, E-posta) ekleyebilir.
- **Öğrenci Bilgilerini Güncelleme:** Mevcut öğrenci bilgileri güncellenebilir.
- **Öğrenci Silme:** Öğrenci bilgileri veritabanından silinebilir.
- **Öğrenci Arama:** Belirli bir öğrenciyi ad veya TC Kimlik No ile arama imkanı.
- **Veri Dışa Aktarma:** Öğrenci bilgilerini bir CSV dosyasına aktarabilir.
- **Kullanıcı Girişi:** Uygulamaya erişim için kullanıcı adı ve şifre ile giriş yapılması gerekmektedir.

## Giriş (Login) Ekranı

Uygulamaya erişim sağlamak için kullanıcıların önce giriş yapması gerekmektedir. Giriş ekranında kullanıcı adı ve şifre alanları bulunur. Doğru kullanıcı adı ve şifre girildikten sonra uygulama ana ekranına yönlendirilirsiniz. Yanlış bilgi girilmesi durumunda hata mesajı görüntülenir.

Giriş ekranı, kullanıcıların uygulamaya yetkisiz erişimini engellemek amacıyla geliştirilmiştir.

## Kullanılan Teknolojiler

- **Python:** Uygulamanın genel programlama dili.
- **Tkinter:** Kullanıcı arayüzü (UI) oluşturmak için kullanılan Python kütüphanesi.
- **MySQL:** Öğrenci verilerinin saklandığı veritabanı.
- **Pandas:** Veri işlemleri ve CSV dosyası dışa aktarma işlemleri için kullanıldı.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımların bilgisayarınızda kurulu olması gerekmektedir:

- Python 3.x
- MySQL Veritabanı
- Aşağıdaki Python kütüphaneleri:
  - Tkinter (Python ile birlikte gelir)
  - MySQL Connector (`pip install mysql-connector-python`)
  - Pandas (`pip install pandas`)

## Kurulum ve Çalıştırma

1. **Depoyu Klonlayın:**
    ```bash
    git clone https://github.com/kullaniciadi/ogrenci-yonetim-sistemi.git
    cd ogrenci-yonetim-sistemi
    ```

2. **Gerekli Python Kütüphanelerini Yükleyin:**
    ```bash
    pip install mysql-connector-python pandas
    ```

3. **MySQL Veritabanını Ayarlayın:**

   MySQL'de aşağıdaki komutları kullanarak bir veritabanı oluşturun ve öğrenci bilgilerini saklayacak tabloları ekleyin:

    ```sql
    CREATE DATABASE ogrenci_yonetim;
    USE ogrenci_yonetim;

    CREATE TABLE ogrenciler (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ad VARCHAR(100),
        soyad VARCHAR(100),
        tc_no VARCHAR(11) UNIQUE,
        dogum_tarihi DATE,
        telefon_no VARCHAR(15),
        eposta VARCHAR(100)
    );
    ```

4. **Veritabanı Bağlantı Ayarlarını Yapılandırın:**

   `database.py` dosyasında, MySQL veritabanı bağlantı ayarlarınızı güncelleyin:

    ```python
    mydb = mysql.connector.connect(
        host="localhost",
        user="kullanici_adiniz",
        password="sifreniz",
        database="ogrenci_yonetim"
    )
    ```

5. **Uygulamayı Başlatın:**
    ```bash
    python main.py
    ```

## Ekran Görüntüleri

### Giriş (Login) Ekranı

Giriş ekranı üzerinden kullanıcı adı ve şifrenizi girerek sisteme erişim sağlayabilirsiniz.

![Giriş Ekranı](screenshots/login_screen.png)

### Öğrenci Yönetim Ekranı

Öğrencileri ekleyebilir, güncelleyebilir, silebilir ve arayabilirsiniz.

![Öğrenci Yönetim Ekranı](screenshots/student_management.png)

## Katkıda Bulunanlar

- **[İsim Soyisim](https://github.com/kullaniciadi)** - Proje Sahibi

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

Bu dosya, projenin temel özelliklerini ve kurulum adımlarını açıklamaktadır. Daha fazla bilgi için proje dosyalarını inceleyebilir veya [wiki](https://github.com/kullaniciadi/ogrenci-yonetim-sistemi/wiki) sayfasına göz atabilirsiniz.
