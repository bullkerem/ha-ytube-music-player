# 🎵 yTube Music Player (Walkman & Linkplay/Fabriq MP3 Proxy Edition)

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

## 📄 Lisans
MIT Lisansı altında açık kaynak olarak sunulmuştur (Orijinal proje: Kolja Windeler `ytube_music_player`, 2026 Walkman & Linkplay/Fabriq geliştirmeleri: `@bullkerem`).
