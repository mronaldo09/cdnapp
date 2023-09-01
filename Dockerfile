# Gunakan image base untuk Python
FROM python:3.8-slim

# Set direktori kerja
WORKDIR /app

# Copy file requirements.txt dan instal dependensi
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy semua file proyek
COPY . .

# Expose port yang akan digunakan oleh Flask
EXPOSE 5000

# Menjalankan aplikasi Flask
CMD ["python", "app.py"]
