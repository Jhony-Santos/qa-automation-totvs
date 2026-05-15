# QA Automation Challenge - TOTVS

## Overview

This project was developed as part of the QA Automation Technical Challenge.

The objective is to validate the ability to design and implement a resilient and scalable automation framework using:

- Python 3.12
- Playwright
- Pytest
- Page Object Model (POM)
- Clean Code principles

---

## Technologies

- Python 3.12
- Playwright
- Pytest
- Requests
- Faker
- Pytest HTML Report

---

## Architecture

The project follows the Page Object Model (POM) pattern.

### Project Structure

```txt
qa-automation-totvs/
│
├── api/
│   └── products_api.py
│
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── home_page.py
│   ├── products_page.py
│   └── signup_page.py
│
├── tests/
│   ├── test_inventory_cart.py
│   ├── test_products_api.py
│   └── test_register_user.py
│
├── utils/
│   └── data_factory.py
│
├── reports/
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Implemented Scenarios

### Web Automation

#### User Registration E2E

- Access website
- Navigate to signup page
- Fill registration form using dynamic data
- Create account
- Validate success message

#### Inventory / Cart Validation

- Access products page
- Open product details
- Add 4 units to cart
- Validate quantity
- Validate total price

---

## API Automation

### GET /api/productsList

Validations:
- Status Code 200
- Response body is not null
- Products list exists
- Products list is not empty
- Product fields contain valid values

---

## Features

- Dynamic test data generation
- Screenshot capture on failure
- HTML report generation
- Reusable methods
- Stable locators
- No fixed waits

---

## Installation

### Clone repository

```bash
git clone https://github.com/Jhony-Santos/qa-automation-totvs.git
```

### Access project

```bash
cd qa-automation-totvs
```

### Create virtual environment

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright browsers

```bash
playwright install
```

---

## Running Tests

### Run all tests

```bash
pytest
```

### Run web tests

```bash
pytest tests/test_register_user.py
```

```bash
pytest tests/test_inventory_cart.py
```

### Run API tests

```bash
pytest tests/test_products_api.py
```

---

## Reports

HTML reports are generated inside:

```txt
reports/
```

Screenshots on failure are generated inside:

```txt
screenshots/
```

---

## Author

Jhonatan Santos