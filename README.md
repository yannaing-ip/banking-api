# Banking API

A PayPal-style banking API built with Django and Django REST Framework. Supports user authentication, account management, and money transfers between users.

## Live Demo

Base URL: `https://banking-api-production-9407.up.railway.app`

Swagger UI: `https://banking-api-production-9407.up.railway.app/swagger/`

## Tech Stack

- Python 3.13
- Django 6.0
- Django REST Framework
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)
- Railway (deployment)
- drf-yasg (Swagger UI)

## Features

- JWT authentication (register, login, token refresh)
- One account per user
- Secure money transfers using atomic transactions and row-level locking
- Double spending prevention with `select_for_update()`
- Transaction history with filtering by date and status
- Swagger UI for API documentation

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login and get JWT tokens |
| POST | `/api/auth/refresh/` | Refresh access token |
| GET | `/api/auth/me/` | Get current user profile |
| PUT | `/api/auth/me/` | Update profile |

### Accounts
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/accounts/create/` | Create account |
| GET | `/api/accounts/` | List my accounts |
| GET | `/api/accounts/<id>/` | Account detail |
| DELETE | `/api/accounts/<id>/` | Deactivate account |

### Transactions
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/transactions/transfer/` | Transfer money by email |
| GET | `/api/transactions/` | List transactions |
| GET | `/api/transactions/<id>/` | Transaction detail |

#### Transaction Filtering
```
GET /api/transactions/?date_from=2024-01-01&date_to=2024-12-31&status=completed
```

## Local Setup

```bash
git clone https://github.com/yannaing-ip/banking-api.git
cd banking-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:
```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/banking_db
```

```bash
python manage.py migrate
python manage.py runserver
```

## Security

- Passwords are hashed using Django's built-in password hashers
- JWT tokens expire after 1 hour
- Refresh tokens expire after 7 days
- All money operations use database-level locking to prevent race conditions
- Balances can never go negative

