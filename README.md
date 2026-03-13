# 🍔 Mini Food - Modern Landing Page

A sleek, premium-designed food delivery landing page built with **Django 6**, **django-tailwind**, and **daisyUI**. This project showcases modern web design principles and core Django fundamentals.

![Project Preview](https://via.placeholder.com/1200x600?text=Mini+Food+Project+Preview)

## 🎯 Project Overview

Mini Food is a responsive landing page designed to "wow" users with vibrant aesthetics, smooth interactions, and a seamless user experience. It serves as a practical application of Django core concepts, integrating a Python backend with a modern utility-first CSS framework via `django-tailwind`.

### ✨ Key Features

- **🚀 High Performance**: Built with Django 6 and optimized static assets.
- **🎨 Premium UI/UX**: Uses a curated HSL color palette and **daisyUI** components for a professional look.
- **📱 Fully Responsive**: Seamless experience across mobile, tablet, and desktop.
- **🍕 Dynamic Menu**: Renders menu items, features, and testimonials dynamically via Django templates.
- **⚡ Hot Reload**: Integrated with `django-browser-reload` for a faster development workflow.
- **✨ Micro-animations**: Interactive hover effects and smooth transitions using Tailwind CSS.

## 🛠️ Tech Stack

- **Backend**: Python 3.x, [Django 6.0](https://www.djangoproject.com/)
- **Frontend**: [Tailwind CSS](https://tailwindcss.com/) via `django-tailwind`, [daisyUI](https://daisyui.com/)
- **Database**: SQLite (Development)
- **Tools**: `django-tailwind`, `django-browser-reload`

## 📖 What I Learned

This project was a journey into mastering the Django ecosystem. Key concepts implemented include:

- **Django Core**: Understanding the `MVT` (Model-View-Template) architecture.
- **Views & URLs**: Handling requests and routing with `path()` and `include()`.
- **Templates**: Mastering Template Inheritance (`extends`, `block`), Partials (`include`), and Loops (`for`).
- **Static Files**: Managing and serving CSS and images using `{% static %}`.
- **Django-Tailwind**: Integrating Tailwind CSS into a Django project as a dedicated theme app.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js & npm (Required for `django-tailwind`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abubakkar-js-dev/mini_food.git
   cd mini_food
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   # Or manually:
   # pip install django django-tailwind django-browser-reload
   ```

4. **Install Tailwind CSS dependencies**:
   ```bash
   python manage.py tailwind install
   ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Start Tailwind in watch mode** (in a separate terminal):
   ```bash
   python manage.py tailwind start
   ```

Go to `http://127.0.0.1:8000` to see the site!

## 📸 Screenshots

| Hero Section | Menu Section |
| :---: | :---: |
| ![Hero](https://via.placeholder.com/400x250) | ![Menu](https://via.placeholder.com/400x250) |

## 🏗️ Future Improvements

- [ ] Add a full-fledged ordering system with a database.
- [ ] Implement user authentication (Sign up / Login).
- [ ] Add a search & filter functionality for menu items.
- [ ] Integrate a payment gateway.

---
Made with ❤️ by Abu Bakkar Siddik
