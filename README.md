# Şifrelerim
Şifrelerinizi kaydedebileceğiniz bir site.

## Açıklama

Bu proje, Python Flask framework'ü kullanılarak oluşturulmuş basit bir web uygulaması içerir. Projede HTML ve CSS dosyaları da kullanılmıştır.

## Başlangıç

### Gereksinimler

- Python 3.x
- Flask
- SQLAlchemy
- Gerekli diğer bağımlılıklar (örneğin, flask-sqlalchemy)

### Kurulum

1. Proje dizinini bilgisayarınıza klonlayın:

    ```bash
    git clone https://github.com/yanardoner/Sifrelerim.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd Şifrelerim
    ```

3. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install pipenv
    pipenv install SQLAlchemy
    pip install Flask
    pip install SQLAlchemy
    ```

4. Veri tabanını oluşturun:

    ```bash
    python3
    ```

    ```bash
    from main import app, db
    app.app_context().push()
    db.create_all()
    ```

    ```bash
    exit()
    ```

4. Uygulamayı başlatın:

    ```bash
    python main.py
    ```

5. Tarayıcınızda şu adrese gidin:

    ```bash
    http://127.0.0.1:5000
    ```

## Proje Yapısı

- Şifrelerim/
- |-- instance/
- |___|-- (diary.db)
- |-- static/
- |___|-- css/
- |______|-- style.css
- |___|-- img/
- |______|-- çöp.png
- |______|-- kilit.png
- |______|-- login.svg
- |______|-- logo.svg
- |______|-- plus.svg
- |-- templates/
- |___|-- card.html
- |___|-- create_card.html
- |___|-- index.html
- |___|-- login.html
- |___|-- registration.html
- |-- dbCreation.txt
- |-- main.py
- README.md

## Kullanım

- Kayıt sayfasından siteye kayıt olabilirsiniz.
- Giriş sayfasından giriş yapabilirsiniz.
- Kayıtlarınızın bulunacağı sayfada yeni kayıt oluşturabilir ve oluşturduğunuz kayıtlara göz atabilirsiniz.
- Kayıtlarınızı istediğiniz zaman kaydı görüntüleyerek çöp kutusu simgesi sayesinde silebilirsiniz.
- Sayfanın üst kısmında bulunan kitap butonu sayesinde kayıtlarınızın bulunduğu sayfaya gidebilir, giriş butonu sayesinde ise giriş ekranı sayfasına gidebilirsiniz.

## Easter Egg

Her yazılımın önemli bir parçası olan Easter Egg'lere bu web sitesinde de yer veriliyor!
İpucu olarak kayıt sayfasından başlayabilirsiniz.
