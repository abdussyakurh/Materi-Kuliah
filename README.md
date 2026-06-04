📊 Visualisasi Alokasi Dana Bulanan Berbasis Graf Aplikasi berbasis web menggunakan Streamlit dan NetworkX untuk membantu pengguna mengelola serta memvisualisasikan alokasi dana bulanan dalam bentuk struktur graf (jaringan). Aplikasi ini juga dilengkapi dengan fitur Text-to-Speech (TTS) untuk memberikan ringkasan saldo secara audio.

🚀 Fitur Utama

Manajemen Dana Dinamis: Input total dana bulanan dan lacak sisa saldo secara real-time.
Visualisasi Graf Jaringan: Menampilkan hubungan antara total dana, tanggal transaksi, dan kategori pengeluaran menggunakan NetworkX dan Matplotlib.
Kalender Otomatis: Sistem mendeteksi jumlah hari dalam bulan dan tahun yang dipilih (termasuk tahun kabisat).
Output Audio (TTS): Menggunakan gTTS untuk memberikan pembaruan status sisa saldo secara suara setelah data ditambahkan.
Tabel Detail: Menampilkan rincian hubungan antar node dan nominal alokasi dana secara tabular.
🛠️ Teknologi yang Digunakan

Python: Bahasa pemrograman utama.
Streamlit: Framework untuk membangun antarmuka web.
NetworkX: Library untuk manipulasi dan visualisasi struktur graf.
Matplotlib: Rendering visualisasi graf ke dalam format gambar.
gTTS (Google Text-to-Speech): Mengubah teks laporan saldo menjadi suara.
Calendar & Datetime: Pengolahan logika penanggalan.
📂 Struktur File

frontend.py: File utama Streamlit yang menangani antarmuka pengguna (UI) dan logika interaksi.
kodingannya.py: Backend berupa class KebutuhanSehariHari yang mengelola struktur data graf menggunakan NetworkX.
⚙️ Cara Menjalankan

Instalasi Library Pastikan Anda sudah menginstal library yang diperlukan melalui terminal/command prompt: pip install streamlit networkx matplotlib gTTS
Menjalankan Aplikasi Jalankan perintah berikut di folder tempat file berada: streamlit run frontend.py
📖 Cara Penggunaan

Masukkan Total Dana Bulanan pada sidebar.
Pilih Tahun dan Bulan untuk menyesuaikan jumlah hari.
Di panel utama, masukkan Tanggal, Nama Kebutuhan, dan Nominal Dana.
Klik "Tambah ke Graf".
Graf akan terbentuk secara otomatis yang menghubungkan:
Pusat Dana ➔ Tanggal ➔ Kebutuhan.
Dengarkan status saldo melalui fitur audio di bagian bawah halaman.
📝 Catatan Pengembangan Proyek ini memisahkan logika bisnis (Backend) dan tampilan (Frontend) untuk memastikan kode tetap rapi dan mudah dikembangkan di kemudian hari (seperti menambahkan fitur hapus node atau penyimpanan database).
