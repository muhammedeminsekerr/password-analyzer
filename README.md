# Password Analyzer

Bir şifrenin ne kadar güçlü olduğunu ölçen araç.

## Ne İşe Yarar?

Hash Cracker'ın tersini yapar: şifre kırmak yerine bir şifrenin ne kadar dayanıklı olduğunu analiz eder. Uzunluk, karakter çeşitliliği ve yaygın zayıf kalıpları kontrol ederek şifreye bir güç puanı verir.

## Özellikler

- Uzunluk kontrolü
- Karakter çeşitliliği (küçük/büyük harf, rakam, özel karakter)
- Yaygın zayıf şifre tespiti
- Güç seviyesi ve iyileştirme önerileri

## Kullanım

    python password_analyzer.py

## Nasıl Çalışır?

Her kriter için puan verir, toplar ve şifreyi zayıf/orta/güçlü olarak sınıflandırır. Uzun ve çeşitli karakterli şifreler yüksek puan alır çünkü deneme yanılma ile kırılmaları katlanarak zorlaşır.

## Yazar

Muhammed Emin Şeker — Bilgisayar Mühendisliği Öğrencisi
GitHub: https://github.com/muhammedeminsekerr
