flask
scikit-learn
numpy
joblib
pandas
=========================================================================================================================
Kelompok 3:
- Ni Komang Ayu Ratih Asrati_F52124051
- Jonathan_F52124083
- Nur Hafsa_F52124085
- Shendy Kalambe_F52124091
- Citra Ramadani
=========================================================================
Keterangan Sistem Kami tentang: 
SISTEM PREDIKSI DINI BENCANA BANJIR

1. Gambaran Umum Sistem
Sistem ini adalah platform web berbasis AI yang dirancang untuk memprediksi potensi banjir secara real-time dan memberikan peringatan dini kepada masyarakat dan pihak terkait. Sistem menggabungkan data sensor, analisis lingkungan, dan visualisasi interaktif untuk meningkatkan kesiapsiagaan bencana.

2. Komponen Utama Sistem
    a. Dashboard Monitoring Real-Time
       - Live Data Sensor: Menampilkan parameter kunci seperti curah hujan, level air sungai, kelembaban tanah, dan data cuaca
       - Visualisasi Grafik: Tren data waktu-nyata dengan grafik interaktif
       - Status Alert: Indikator warna (hijau/kuning/merah) untuk tingkat bahaya

    b. Modul Prediksi AI/ML
       - Model Prediksi: Menggunakan algoritma machine learning untuk menganalisis pola historis dan data real-time
       - Faktor Prediksi:
         Curah hujan (jam/harian)
         Kapasitas drainase
         Topografi wilayah
         Data historis banjir
       - Output: Probabilitas banjir dengan skala risiko (Rendah-Sedang-Tinggi)

     c. Sistem Peringatan Dini
       - Multi-level Alert:
         Level 1 (Waspada): Monitoring intensif
         Level 2 (Siaga): Persiapan evakuasi
         Level 3 (Awas): Evakuasi segera
       - Channel Notifikasi:
         Notifikasi web dashboard
         SMS blast (opsional)
         Email alert

      d. Peta Interaktif
         GIS Mapping: Pemetaan daerah rawan banjir
         Zonasi Risiko: Pembagian wilayah berdasarkan kerentanan
         Lokasi Sensor: Visualisasi titik-titik sensor

3. Alur Kerja Sistem
Data Input → Proses Analisis → Prediksi → Notifikasi → Tindakan
      ↓           ↓           ↓          ↓           ↓
[Sensor] → [AI Model] → [Risk Level] → [Alert] → [Response]

4. Teknologi yang Digunakan
   a. Frontend (Web Interface)
      HTML5, CSS3, JavaScript
      Chart.js / D3.js untuk visualisasi
      Peta interaktif (Leaflet/OpenLayers)
      Responsive design
   b. Backend & Analisis
      Python (Flask/Django)
      Scikit-learn / TensorFlow untuk model ML
      Database (MySQL/PostgreSQL)
      API untuk integrasi data eksternal

5. Fitur Utama untuk Pengguna
   a. Untuk Masyarakat Umum:
      Informasi status banjir real-time
      Peta zona aman dan evakuasi
      Panduan kesiapsiagaan
   b. Untuk Petugas/Pemerintah:
      Dashboard monitoring lengkap
      Laporan otomatis
      Manajemen sumber daya darurat
      Analisis historis untuk perencanaan

6. Proses Prediksi
   a. Pengumpulan Data:
      Data sensor IoT
      Data cuaca dari BMKG
      Data topografi
   b. Preprocessing:
      Pembersihan data
      Normalisasi
      Feature engineering
   c. Analisis & Prediksi:
      Running model ML
      Perhitungan probabilitas
      Validasi hasil
   d. Visualisasi & Diseminasi:
      Update dashboard
      Generate alert
      Distribusi informasi
