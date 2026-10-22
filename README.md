# Skill Swap Hub (skill_swap_project)

A modern, community-driven skill sharing platform built with Django, Tailwind CSS, and Vanilla JavaScript. Skill Swap Hub allows users to list skills they can offer, request skills they want to learn, connect with other members, and manage their personal skill listings.

---

## Features

- **Skill Listings & Filtering:** Browse community skills with instant filtering between "Offering" and "Requesting" tabs, search queries, and sorting.
- **Skill Management:** Create, edit, and delete personal skills with a responsive confirmation modal.
- **User Authentication:** Registration, login, and profile management with avatar support.
- **Direct Connect:** Connect modal providing contact details (username & email) for skill exchange partners.
- **Fluid UI & Micro-interactions:** Tactile button click animations, smooth modal zooms with backdrop blur, and smooth page transitions.
- **Collapsible Sidebar:** Persistent desktop sidebar state (saved in `localStorage`) and mobile off-canvas drawer.

---

## Tech Stack

- **Backend:** Python, Django 5.2.7
- **Database:** SQLite
- **Frontend:** HTML5, Tailwind CSS, Vanilla CSS & JavaScript, Font Awesome 6.5
- **Image Processing:** Pillow 11.3

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshilp2930/skill_swap_project.git
   cd skill_swap_project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

---

## Default Demo Credentials

- **Username:** `harshil` | **Password:** `1234`
- **Username:** `yash` | **Password:** `1234`
