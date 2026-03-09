# Flask Invoice Generator

A lightweight billing and invoice generation web application built with **Flask**.
The application collects billing details through a form and generates a printable invoice with automatic GST calculation and amount-in-words conversion.

---

## Features

* Clean billing form with validation
* Automatic invoice number generation
* GST calculation
* Dynamic quantity calculation
* Amount-in-words conversion
* Printable invoice
* Export invoice as PDF
* Address auto-fill from pincode API
* International phone number validation

---

## Tech Stack

Backend

* Python
* Flask

Frontend

* HTML
* Bootstrap 5
* JavaScript

Libraries

* html2pdf.js
* intl-tel-input

---

## Project Structure

```
receiptprojectflask/
│
├── backend.py
├── requirements.txt
│
├── templates/
│   ├── billing_form.html
│   └── receipt.html
│
└── static/
    └── logo.png
```

### File Overview

`backend.py`
Flask application containing routes, invoice generation logic, and form handling.

`templates/billing_form.html`
Form interface where users enter billing and receiver details.

`templates/receipt.html`
Invoice template rendered after form submission.

`static/logo.png`
Company logo used in the invoice header.

---

## How It Works

1. User opens the billing form.
2. Form collects receiver and owner details.
3. Data is sent to the Flask backend.
4. Backend generates:

   * Invoice number
   * Invoice date
5. The receipt template is rendered with the submitted data.
6. The user can print the invoice or export it as PDF.

---

## Local Setup

### 1. Clone the repository

```
git clone https://github.com/yourusername/receipt-project-flask.git
cd receipt-project-flask
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python backend.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## Deployment

This project can be deployed on platforms such as **Render**.

Start command used during deployment:

```
gunicorn backend:app
```

---

## Notes

* Invoice numbers are generated sequentially during runtime.
* Data is not stored in a database in the current implementation.
* This project is intended as a lightweight demonstration of a Flask-based billing workflow.

---

## Author

Delwin
