# Gamepad Frontend

Kivy ve KivyMD kütüphaneleri kullanılarak oluşturulmuş bir gamepad arayüzünün kodlarını içermektedir. Uygulama, bir oyun veya simülasyonu kontrol etmek için etkileşimli bir kullanıcı arayüzü sağlar. Arayüz, çeşitli düğmeler ve yönlendirme kontrolleri ile görsel olarak çekici ve kullanıcı dostu bir düzen sunar.

## Özellikler

- **Düğme Kontrolleri**: "Touch", "Enlarge", "STOP" ve yön düğmeleri gibi farklı eylemler için birden fazla düğme içerir.
- **Görsel Göstergeler**: Düğme eylemleri için görsel geri bildirim sağlamak amacıyla ikonlar kullanır.
- **Duyarlı Düzen**: Farklı ekran boyutlarına uyum sağlar, böylece çeşitli cihazlarda kullanılabilirlik sağlar.

## Gereksinimler

Bu uygulamayı çalıştırmadan önce aşağıdakilerin kurulu olduğundan emin olun:

- Python 3.6 veya üzeri
- Kivy
- KivyMD

Gerekli paketleri pip kullanarak yükleyebilirsiniz:

```bash
pip install kivy kivymd
```

## Dosya Yapısı

- `main.py`: Uygulamayı çalıştıran ana Python dosyası.
- `main.kv`: Uygulamanın düzenini tanımlayan Kivy dili dosyası.
- `image/image1.png`: Düzen içinde kullanılan görüntü kaynağı.

## Uygulamayı Çalıştırma

1. Bu depoyu yerel makinenize klonlayın.
2. Proje dizinine gidin.
3. Aşağıdaki komutu kullanarak uygulamayı çalıştırın:

```bash
python main.py
```
![gamepaf_frontend](https://github.com/Deryaglmz/GamepadFrontend/assets/129391768/98e032f1-c376-4a5f-935a-d2237b4230c7)
