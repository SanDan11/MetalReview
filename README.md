# 🔥 Metal Review — Full-Stack Metal Album Review App 🤘

> A full-stack web application where I write and showcase my own reviews of legendary metal albums.  
> Built with **React + Vite + TailwindCSS (frontend)** and **FastAPI + SQLite + SQLAlchemy (backend)**, the app combines clean API design, responsive UI, and a dark-metal aesthetic.

---

## 🎯 Overview

Metal Review is a personal review platform designed for **music enthusiasts and developers alike**.  
It allows me to catalog albums, assign ratings, write long-form reviews, and highlight my top 5 records — all powered by a full-stack architecture I coded from scratch.

This project helped me master:
- Building REST APIs with **FastAPI**
- Frontend integration using **React + Axios**
- Styling responsive UIs with **TailwindCSS**
- Managing SQLite databases via **SQLAlchemy ORM**

---

## ⚙️ Features

| Feature | Description |
|:--|:--|
| 🎸 **Album Management** | Add, view, and rate albums in the database |
| 🧠 **Personal Review System** | Write in-depth reviews for each album (Markdown supported) |
| 🔍 **Search & Filters** | Search by album title or artist, filter by genre or rating |
| 🏆 **Top 5 Albums** | Automatically highlights highest-rated albums |
| 💾 **SQLite Database** | Lightweight and portable backend database |
| 🎨 **Tailwind UI** | Metal-themed dark mode styling with glow effects |
| ⚡ **FastAPI Backend** | Fast, async Python backend with REST endpoints |

---

## 🧱 Tech Stack

| Layer | Technology |
|:--|:--|
| **Frontend** | React (Vite), TailwindCSS, Axios, React Router, React Markdown |
| **Backend** | FastAPI, SQLAlchemy, SQLite |
| **Tools** | VS Code, Node.js, Python 3.12, Git |

---

## 🗺️ Roadmap

| Phase | Description | Status |
|:--|:--|:--|
| Phase 0 | Project setup — Vite + Tailwind + GitHub | ✅ |
| Phase 1 | FastAPI backend + SQLite database setup | ✅ |
| Phase 2.1 | React frontend + Album dashboard | ✅ |
| Phase 2.2 | Search + Filter functionality | ✅ |
| Phase 2.3 | Top 5 Albums highlight | ✅ |
| Phase 3 | Review Editor (create / edit reviews via frontend) | ⏳ |
| Phase 4 | Optional user profiles and polish pass | 🔜 |

---

## 🖼️ Screenshots (Coming Soon)

| Home Dashboard | Album Review Page |
|:--:|:--:|
| ![Home Screenshot](docs/home.png) | ![Review Screenshot](docs/review.png) |

---

## 🚀 How to Run

### 🧩 Backend (FastAPI)
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
