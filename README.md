# Django Stripe Checkout Demo

This project is a simple Django application demonstrating Stripe Checkout (test mode) with a minimal product purchase flow.

---

## Features

- Three fixed products displayed on a single page
- Quantity selection and Stripe Checkout payment
- Paid orders shown on the same page ("My Orders")
- Protection against double charge / refresh issues

---

## Tech Stack

- Django
- Stripe (Checkout – Test Mode)
- PostgreSQL
- HTML (Django Templates)

---

## Assumptions

- Single-page UX for simplicity
- No user authentication 
- Prices stored in the smallest currency unit (paise)

---

## Payment Flow

Stripe Checkout was chosen over Payment Intents because:

- It handles most edge cases (validation, retries, UI)
- Reduces backend complexity
- More secure for a small demo

### Flow

1. User selects product and quantity
2. Backend creates a Stripe Checkout Session
3. User completes payment on Stripe-hosted page
4. On success, order is marked as paid and shown on home page

---

## Preventing Double Charge / Inconsistent State

- Each payment creates a unique Stripe Checkout Session ID
- Session ID is stored before redirecting the user
- Order is marked as paid only once
- Refreshing the success page does not create duplicate charges

---

# Setup Instructions

# 1. Clone the repository
```bash
git clone <repo-url>
cd payment_project
```
# 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
# 3. Install dependencies
```bash
pip install -r requirements.txt
```
# 4. Environment variables
# Create a .env file and add:
```bash
STRIPE_SECRET_KEY=
STRIPE_PUBLIC_KEY=
DB_NAME=stripe_db
DB_USER=stripe_user
DB_PASSWORD=strongpassword
DB_HOST=localhost
DB_PORT=5432
```
# 6. Run development server
```bash
python manage.py runserver
```

## Add Sample Products Using Django Shell
Open Django shell:
```bash
python manage.py shell
```
Run the following commands:
```bash
from shop.models import Product

Product.objects.create(name="T-Shirt", price=50000)
Product.objects.create(name="Shoes", price=120000)
Product.objects.create(name="Cap", price=30000)

exit()
```
## Stripe Test Card

Use the following Stripe test card:

Card Number: 4242 4242 4242 4242

Expiry Date: Any future date

CVC: Any