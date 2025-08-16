# 🎙️ Sentiric Coqui TTS Service - Görev Listesi

Bu belge, `coqui-tts-service`'in geliştirme yol haritasını ve önceliklerini tanımlar.

---

### Faz 1: Temel Sentezleme Yeteneği (Mevcut Durum)

Bu faz, servisin temel ses üretme ve klonlama görevini yerine getirmesini hedefler.

-   [x] **FastAPI Sunucusu:** `/api/v1/synthesize` endpoint'ini içeren temel sunucu.
-   [x] **Coqui XTTS Entegrasyonu:** `TTS.api` kütüphanesi ile `xtts_v2` modelini yükleme ve kullanma.
-   [x] **Varsayılan Ses:** `speaker_wav_url` belirtilmediğinde varsayılan bir referans sesi kullanma.
-   [x] **Dinamik Ses Klonlama:** Harici bir URL'den referans `.wav` indirip sesi klonlama yeteneği.
-   [x] **Gözlemlenebilirlik:** Sağlık kontrolü (`/health`) endpoint'i ve yapılandırılmış loglama.

---

### Faz 2: Performans ve Optimizasyon (Sıradaki Öncelik)

Bu faz, servisin kaynak kullanımını ve hızını iyileştirmeyi hedefler.

-   [ ] **Görev ID: TTS-COQUI-001 - Model Önbellekleme**
    -   **Açıklama:** Sık kullanılan `speaker_wav_url`'lerinden indirilen ses dosyalarını ve üretilen sesleri Redis'te önbelleğe alarak tekrar eden istekleri hızlandır. (Bu görev `tts-gateway`'e taşınabilir).
    -   **Durum:** ⬜ Planlandı.

-   [ ] **Görev ID: TTS-COQUI-002 - GPU Optimizasyonu**
    -   **Açıklama:** Eğer CUDA destekli bir ortamda çalışıyorsa, modelin GPU üzerinde daha verimli çalışması için `torch` ayarlarını ve `Dockerfile`'ı optimize et.
    -   **Durum:** ⬜ Planlandı.

---

### Faz 3: Gelişmiş Özellikler

-   [ ] **Görev ID: TTS-COQUI-003 - Duygu Desteği (Emotion)**
    -   **Açıklama:** Coqui XTTS modelinin desteklediği duygu (`emotion`) parametresini API'ye ekleyerek, "kızgın", "mutlu" gibi farklı tonlarda ses üretmeyi sağla.
    -   **Durum:** ⬜ Planlandı.