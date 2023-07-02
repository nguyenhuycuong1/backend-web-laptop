# Sử dụng base image có sẵn chứa Python và PostgreSQL
FROM python:3.10

# Cài đặt các dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Sao chép mã nguồn vào container
COPY . /app
WORKDIR /app

# Cài đặt dependencies từ file requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Chạy lệnh migrate để tạo các bảng trong PostgreSQL
CMD ["python", "manage.py", "migrate"]

# Mở cổng 8000 để truy cập vào FastAPI
EXPOSE 8000

# Chạy ứng dụng FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
