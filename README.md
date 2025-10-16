# django-test-04

Django REST API Project được tạo tự động bởi **Dev Portal**.

## 📋 Thông tin Project

- **Project Name:** django-test-04
- **App Name:** api
- **Django Version:** 4.2.7
- **DRF Version:** 3.14.0

## 🚀 Models

- **cook**: getcook/

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/quanmbl4255142/django-test-04.git

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## 🐳 Docker

```bash
# Build image
docker build -t django-test-04 .

# Run container
docker run -p 8000:8000 django-test-04
```

## 🔗 API Endpoints

- GET/POST `/api/getcook/` - List/Create cook
- GET/PUT/DELETE `/api/getcook/<id>/` - Detail/Update/Delete cook
- GET `/api/health/` - Health check

## 📝 License

MIT License
