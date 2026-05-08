# The VIP Path: Predictive Decision Tree for E-sports Arena

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Project-Finished-success.svg)]()

## Project Overview

Project ini bertujuan untuk mengidentifikasi profil pelanggan di sebuah arena e-sports yang memiliki potensi tinggi untuk beralih ke layanan **VIP Membership**. Dengan menggunakan pendekatan **Decision Tree Learning** secara manual, project ini menganalisis variabel mana yang paling berpengaruh terhadap keputusan pelanggan.

## Dataset Description

Dataset dihasilkan secara sintetis menggunakan `generator.py` dengan korelasi yang disesuaikan dengan perilaku nyata di industri gaming/warnet. Variabel meliputi:

- **Genre Favorit:** FPS, MOBA, RPG, Casual.
- **Jam Main Mingguan:** Durasi bermain dalam satu minggu.
- **Pengeluaran Snack:** Total belanja makanan/minuman.
- **Waktu Main Utama:** Pagi, Siang, Sore, Malam, Subuh.
- **Target:** `target_membership` (1 = Member, 0 = Reguler).

## Key Technical Features

1. **Entropy & Information Gain:** Menentukan variabel pemisah (Root Node) terbaik untuk meminimalkan ketidakpastian data.
2. **Leakage Audit:** Mengidentifikasi dan menghapus variabel yang menyebabkan bias (Data Leakage).
3. **Laplace Smoothing:** Menangani probabilitas pada grup dengan sampel kecil (Small Sample Size) agar prediksi tetap realistis.
4. **Rules Extraction:** Mengonversi struktur pohon keputusan menjadi strategi bisnis "IF-THEN" yang siap pakai.

## Quick Results

- **Top Predictor:** `jam_main_mingguan` dengan threshold optimal di angka **34 Jam**.
- **Top Synergy:** Kombinasi Jam Main (>34) dan Pengeluaran Snack (>70rb) meningkatkan akurasi prediksi secara signifikan.
- **Laplace Correction:** Mengoreksi probabilitas segmen langka dari 0% menjadi **6.67%**.

## How to Run

1. Jalankan `dataset-generator.py` untuk mendapatkan `dataset-pelanggan.csv`.
2. Buka `analysis.ipynb` menggunakan Jupyter Notebook atau VS Code.
3. Jalankan semua cell untuk melihat proses hitung Entropy dan visualisasi Gain.

---

_Project ini adalah bagian dari pembelajaran mandiri Data Science - Bab 3: Decision Tree Foundations._

## Author

Ryan
