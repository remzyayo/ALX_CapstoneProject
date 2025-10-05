# 💰 Expense Tracker API

A Django Rest Framework (DRF) project that allows users to *track their expenses* by category, date, and budget.  
Each user can register, log in, and manage their own expenses securely.  

This API is built as part of my *ALX Capstone Project, demonstrating skills in **backend development, database modeling, and RESTful API design*.

---

## 📚 Table of Contents

- [Project Overview](#-project-overview)
- [Week-by-Week Progress](#-week-by-week-progress)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [API Endpoints](#-api-endpoints)
- [Example Payloads](#-example-payloads)
- [Author](#-author)
- [Future Plans](#-future-plans)

---

## 🚀 Project Overview

The *Expense Tracker API* helps users manage their finances by logging and categorizing expenses.  
Each user has private access to their data and can set budgets, compare them with actual spending, and monitor their difference.

---

## 🗓 Week-by-Week Progress

### ✅ Week 1 (Current)
- Setup Django and Django REST Framework
- Configured project settings and virtual environment
- Implemented user authentication (register, login, logout)
- Connected local repo to GitHub

### ⏳ Week 2 (Upcoming)
- Implement Expense CRUD functionality
- Add attributes (Category, Amount, Budget, Difference)
- Create user-based relationships (each user manages their own expenses)

### 🚀 Week 3 (Upcoming)
- Add filtering and pagination
- Deploy to Heroku or PythonAnywhere
- Finalize README and API documentation

---

## ✨ Features

- User Registration & Authentication  
- Add, Edit, Delete, View Expenses (CRUD)  
- Expense Date and Time Tracking  
- Budget vs Actual Difference Calculation  
- Filtering & Pagination (Week 3)  
- JWT Token Authentication  

---

## 🧱 Tech Stack

- *Python 3.12*
- *Django 5.x*
- *Django REST Framework (DRF)*
- *SQLite* (Development)
- *JWT Authentication* (via SimpleJWT)
- *Postman* for API testing

---

## 🔑 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /api/register/ | Register a new user |
| POST | /api/login/ | Login and get authentication token |
| POST | /api/logout/ | Logout user |
| GET | /api/expenses/ | List all expenses |
| POST | /api/expenses/ | Create a new expense |
| PUT | /api/expenses/<id>/ | Update expense |
| DELETE | /api/expenses/<id>/ | Delete expense |

---

## 🧪 Example Payloads

### 🧍‍♂ User Registration
```json
{
  "username": "francis",
  "email": "francis@example.com",
  "password": "password123"
}

---

## Author
*Francis Oluremi*  
Founder/CEO – CAROMA FARM ENTERPRISES 
📍 Ondo State, Nigeria  

[LinkedIn](https://www.linkedin.com/in/francis-oluremi-aa927a355/)

---

## 🚀 Future Plans

Here are some features and improvements planned for future versions of this project:

1. *Expense Filtering & Pagination*
   - Allow users to filter expenses by category or date range.
   - Add pagination for large expense lists.

2. *Budget Alerts*
   - Notify users when their spending approaches or exceeds their set budget.

3. *Data Visualization*
   - Display monthly or category-based expense summaries using charts.

4. *Reports & Export*
   - Generate downloadable expense reports (PDF or Excel).

5. *JWT Authentication*
   - Upgrade authentication to use JSON Web Tokens for better security.

6. *Frontend Integration*
   - Build a React or Vue.js frontend to consume this API for better user experience.

7. *Cloud Deployment*
   - Host the API on platforms like Heroku or PythonAnywhere for live access.

8. *Multi-Currency Support*
   - Support different currencies and automatic conversion for international users.


The goal is to make this Expense Tracker API a complete personal finance management solution.



