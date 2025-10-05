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
- [License](#-license)
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
