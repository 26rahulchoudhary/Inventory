# 📦 Inventory Management System

An Inventory Management System built using **Django**, **Django REST Framework**, and **MySQL**. This backend API allows businesses to efficiently manage products, stock levels, suppliers, and purchase orders.

---

## 🚀 Features

- ✅ Product CRUD operations
- ✅ Stock quantity tracking
- ✅ Low-stock alerts
- ✅ Supplier management (optional)
- ✅ RESTful APIs using Django REST Framework
- ✅ Secure authentication (optional)
- ✅ Admin dashboard (Django Admin)

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **API:** RESTful API
- **Optional:** JWT Authentication, Docker

---

## 📂 Project Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/inventory-management.git
cd inventory-management
````

2. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure MySQL Database**

In `settings.py`, update your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Create a superuser (optional for Django Admin)**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

---

## 📡 API Endpoints Overview

| Method | Endpoint                           | Description             |
| ------ | ---------------------------------- | ----------------------- |
| GET    | `/api/products/`                   | List all products       |
| POST   | `/api/products/`                   | Add new product         |
| GET    | `/api/products/{id}/`              | Retrieve single product |
| PUT    | `/api/products/{id}/`              | Update product          |
| DELETE | `/api/products/{id}/`              | Delete product          |
| PATCH  | `/api/products/{id}/adjust-stock/` | Adjust stock quantity   |
| GET    | `/api/low-stock/`                  | List low-stock products |

*Add more based on your project’s structure.*

---

## 📊 Admin Dashboard

Access Django's built-in admin interface at:

```
/admin/
```

---

## 📌 Future Improvements

* Add purchase orders module
* Generate stock reports
* Role-based permissions
* JWT authentication
* API documentation using Swagger/Postman

---

## 📃 License

This project is open-source under the [MIT License](LICENSE).

---

## 👤 Author

**Rahul Choudhary**
[LinkedIn](https://linkedin.com/in/rahulchoudhary2610)
📧 [rahulchoudhary5266@gmail.com](mailto:rahulchoudhary5266@gmail.com)
```
