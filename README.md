# mcp-student-sandbox

Bu repository, öğrenci geliştirme sandbox'ı olarak tasarlanmıştır. Yazılım mühendisliği öğrencilerinin kod iyileştirmesi, hata ayıklama ve GitHub iş akışlarını öğrenmelerini sağlar.

## Repository Bilgileri
- **Repo**: elifKemik/mcp-student-sandbox
- **Repo ID**: 1193751597
- **Dil Kompozisyonu**: Python ağırlıklı (detaylar için GitHub Insights'a bakın).

## İçerik Özeti

- **spaghetti_logic.py**: Temiz kod iyileştirmeleri.
- **failing_calculator.py**: Pull Request ile hata düzeltmeleri.
- **secret_leak.py**: Güvenlik sızıntısı için Issue.
- **mystery_module.py**: İkinci dereceden denklem çözümü.

## Temiz Kod Çalışmaları

`spaghetti_logic.py` dosyasında yapılan iyileştirmeler:

- Fonksiyonları ayrıştırarak modülerlik artırıldı.
- Değişken isimleri açıklayıcı hale getirildi (örneğin, `input_data`, `result_value`).
- Kod tekrarı kaldırıldı ve yardımcı fonksiyonlar eklendi.
- Docstring'ler ve hata yönetimi eklendi.

## Pull Request: failing_calculator.py

| Detay | Açıklama |
|-------|----------|
| **Başlık** | Fix calculator bugs and improve error handling |
| **İyileştirmeler** | Sıfıra bölme hatası kontrolü eklendi; geçersiz giriş doğrulandı; operatör işleme fonksiyonu ayrıldı. |
| **Örnek Değişiklik** | `def calculate(a, b, op): if op == '/' and b == 0: raise ValueError("Cannot divide by zero")` |
| **Durum** | Açık (Open) |

## Issue: secret_leak.py

| Detay | Açıklama |
|-------|----------|
| **Başlık** | Security vulnerability: Hardcoded secrets in secret_leak.py |
| **Sorun** | Hassas verilerin kodda hardcoded edilmesi. |
| **Çözüm Önerisi** | Environment variable'lara taşıma; `.env` dosyası kullanımı. |
| **Örnek** | `API_KEY = os.getenv("API_KEY")` |
| **Durum** | Açık (Open) |

## mystery_module.py

Bu modül, ikinci dereceden denklemleri çözer.

- **Fonksiyon**: `solve_quadratic(a, b, c)`
- **Çıktı**: Kökler (gerçek veya karmaşık).
- **Örnek**: `solve_quadratic(1, -3, 2)` → `(2.0, 1.0)`

## Kurulum ve Kullanım

1. Klone: `git clone https://github.com/elifKemik/mcp-student-sandbox.git`
2. Çalıştır: `python <dosya_adi>.py`
3. Katkıda bulun: PR/Issue açın.
```</body>