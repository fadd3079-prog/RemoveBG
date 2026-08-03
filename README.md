# RemoveBG

## Cara Pakai

1. Buat virtual environment
```powershell
python -m venv .venv
```

2. Aktifkan virtual environment
```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependensi
Pakai CPU:
```powershell
pip install "rembg[CPU]" pillow
```

Jika ingin GPU:
```powershell
pip install "rembg[GPU]" pillow
```

4. Jalankan program
```powershell
python main.py
```

5. Keluar dari virtual environment
```powershell
deactivate
```

