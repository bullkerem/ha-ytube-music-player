# 🎵 yTube Music Player (Walkman & Linkplay/Fabriq MP3 Proxy Edition)

[![GitHub Release](https://img.shields.io/github/v/release/bullkerem/ha-ytube-music-player?style=for-the-badge&color=brightgreen)](https://github.com/bullkerem/ha-ytube-music-player/releases)
[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge&logo=homeassistantcommunitystore&logoColor=white)](https://github.com/hacs/integration)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.1%2B-18BCF2.svg?style=for-the-badge&logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/bullkerem/ha-ytube-music-player?style=for-the-badge&color=yellow)](https://github.com/bullkerem/ha-ytube-music-player/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/bullkerem/ha-ytube-music-player?style=for-the-badge&color=orange)](https://github.com/bullkerem/ha-ytube-music-player/issues)
[![Last Commit](https://img.shields.io/github/last-commit/bullkerem/ha-ytube-music-player?style=for-the-badge&color=purple)](https://github.com/bullkerem/ha-ytube-music-player/commits/main)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=bullkerem&repository=ha-ytube-music-player&category=integration)

Home Assistant üzerinde **hiçbir Google OAuth / Cookie kurulumuna gerek kalmadan** doğrudan YouTube Music şarkı araması yapabilen ve **Linkplay A31 / Fabriq / Google Cast / VLC** hoparlörlere yerel MP3 dönüştürme (`ffmpeg` proxy) ile kesintisiz ses aktarabilen gelişmiş YouTube Music eklentisi.

---

## 🚀 Bu Sürümdeki Özel Yenilikler

1. **🔓 Oturum Açmadan Anında Arama (`search_query` & `play_query`):**
   - Google'ın Kasım 2024'te kapattığı OAuth / Cookie zorunluluğunu aşarak `ytmusicapi` ve `pytubefix` hibrit motoruyla **0.5 - 2 saniye** içinde şarkı ve sanatçı araması yapar.
2. **🔊 Linkplay A31 / Fabriq Hoparlör Uyumlu Yerel MP3 Proxy (`ytube_proxy.mp3`):**
   - YouTube'un parça parça (`ftypdash` / `iso6`) DASH ses akışlarını Fabriq ve Linkplay A31 donanım çipleri doğrudan çalamaz.
   - Bu sürüm, şarkıyı `Range` paketleriyle yüksek hızda indirip `ffmpeg` (`libmp3lame`) ile standart MP3 formatına (`/local/ytube_proxy.mp3`) dönüştürerek evdeki tüm Wi-Fi hoparlörlerde %100 uyumlu çalar.
3. **📻 Çoklu Hoparlör (Walkman Multi-Room) Seçim Desteği:**
   - Seçili olan birden fazla hoparlöre (`Salon Fabriq`, `Mutfak Fabriq`, `Google Nest Mini`, `VLC`) aynı anda yayın gönderir ve durdurulduğunda tüm seçili hoparlörleri senkronize durdurur.
4. **🛠️ Entegre Fabriq Donanım Köprüsü (`fabriq_cmd`):**
   - Linkplay HTTP API komutlarını (`EQLoad`, `switchmode`, `multiroom`, `timeSync`, `PromptEnable`) doğrudan çalıştırabilir.

---

## 📦 Kurulum

### HACS ile Kurulum
1. **HACS → Entegrasyonlar → Sağ Üst Üç Nokta (`⋮`) → Özel Depolar (Custom Repositories)** menüsünü açın.
2. Bu GitHub deposunun adresini ekleyip kategori olarak **Integration** seçin.
3. İndirdikten sonra Home Assistant'ı yeniden başlatın.

### Manuel Kurulum
1. `custom_components/ytube_music_player` klasörünü Home Assistant'ınızın `/config/custom_components/ytube_music_player` dizinine kopyalayın.
2. Home Assistant'ı yeniden başlatın.

---

## ⚡ Hızlı Arama ve Çaldırma Komutları (`ytube_music_player.call_method`)

- **Şarkı Ara ve Sonuçları Listele (`sensor.ytube_music_player_extra`):**
  ```yaml
  action: ytube_music_player.call_method
  data:
    entity_id: media_player.ytube_music_player
    command: search_query
    parameters:
      - "90lar Türkçe Pop"
  ```
- **Aranan Şarkıyı Doğrudan Çal:**
  ```yaml
  action: ytube_music_player.call_method
  data:
    entity_id: media_player.ytube_music_player
    command: play_query
    parameters:
      - "Tarkan Kuzu Kuzu"
  ```
- **Video ID ile Doğrudan Çal:**
  ```yaml
  action: ytube_music_player.call_method
  data:
    entity_id: media_player.ytube_music_player
    command: play_video_id
    parameters:
      - "dQw4w9WgXcQ"
  ```

---

## 🆕 Sürüm Geçmişi / Changelog

### v20261113.01
- 🚀 Walkman & Linkplay/Fabriq MP3 Proxy Edition için ilk resmi GitHub / HACS sürümü yayınlandı.
- 🏷️ Dinamik GitHub Release, HACS Custom, Home Assistant (`2024.1+`), License MIT, Yıldız, Sorun, Son Commit rozetleri ve tek tıkla **My Home Assistant (HACS)** kurulum butonu eklendi.
- 📦 `manifest.json` sürümü `20261113.01` ve depo bağlantıları `bullkerem/ha-ytube-music-player` olarak güncellendi.

---

## 📄 Lisans
MIT Lisansı altında açık kaynak olarak sunulmuştur (Orijinal proje: Kolja Windeler `ytube_music_player`, 2026 Walkman & Linkplay/Fabriq geliştirmeleri: `@bullkerem`).
