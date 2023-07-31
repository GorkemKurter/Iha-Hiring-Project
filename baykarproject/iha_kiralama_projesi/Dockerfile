# Resmi Python 3 imajını kullanarak Django uygulamasını çalıştırmak için Dockerfile
FROM python:3

# Çıktı ve hataları tamponlamadan doğrudan yazdırmak için çevre değişkeni ayarı
ENV PYTHONUNBUFFERED 1

# Django uygulamasının çalışacağı /code dizinini oluşturur
RUN mkdir /code
WORKDIR /code

# Gerekli Python kütüphanelerini yüklemek için requirements.txt dosyasını kopyala ve yükleyin
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Proje dosyalarını Docker konteynerine kopyala
ADD . /code/
