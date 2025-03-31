# Base image olarak Python 3.9 kullanalım
FROM python:3.9-slim

# Çalışma dizini oluşturalım
WORKDIR /app

# requirements.txt dosyasını kopyalayıp bağımlılıkları yükleyelim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalayalım
COPY . .

# 5000 portunu dışarıya açalım
EXPOSE 5000

# Uygulamayı çalıştıralım
CMD ["python", "app.py"]