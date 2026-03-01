# Premium (2026 Update)

Repository ini sudah diperbarui menjadi **tool pengecekan environment** yang aman dan valid untuk Python modern.

## Fungsi utama
- Validasi versi Python minimum `3.10` (rekomendasi `3.12+`).
- Cek ketersediaan command `git` dan `pip`.
- Cek status folder sebagai repository git.
- Cek dependensi Python: `requests`, `rich`, `bs4`.
- Dukungan output human-readable dan JSON.

## Menjalankan
```bash
python run.py
```

## Output JSON
```bash
python run.py --json
```

## Instalasi dependensi jika ada yang missing
```bash
pip install requests rich beautifulsoup4
```

## Catatan
Proyek ini **tidak** lagi menjalankan automasi login/cracking. Fokus sekarang adalah utility diagnostik yang aman untuk kebutuhan setup dan troubleshooting.
