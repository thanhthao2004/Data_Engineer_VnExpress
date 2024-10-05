# Sử dụng hình ảnh Python 3.10
FROM python:3.10

# Thiết lập thư mục làm việc
WORKDIR /usr/src/app

# Sao chép tệp requirements.txt vào container
COPY requirements.txt ./

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
RUN pip install scrapy selenium webdriver-manager pymongo

# Cài đặt Chromium và các thư viện hỗ trợ
RUN apt-get update && apt-get install -y \
    chromium \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    && apt-get clean

# Tải xuống và cài đặt ChromeDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Sao chép mã nguồn ứng dụng vào container
COPY . .

# Đặt biến môi trường cho Python
ENV PYTHONUNBUFFERED=1

# Lệnh để chạy ứng dụng
CMD ["sh", "-c", "sleep 60 && python -m scrapy runspider vnexpress_data_warehouse/spiders/feature_TTTThao.py"]
