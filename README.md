# NimHub

**NimHub** is a modern desktop application built with Python and CustomTkinter that helps developers manage their projects, tasks, portfolios, and productivity from one centralized dashboard.

---

#  Features

-  Interactive Dashboard
-  Project Management
-  Task Management
-  Portfolio (Nimfolio)
-  Statistics & Analytics
-  Settings
-  Modern Dark UI
-  SQLite Database
-  Search Functionality
-  Task Tracking

---

# Technologies Used

- Python 3
- CustomTkinter
- SQLite3
- Tkinter
- Object-Oriented Programming (OOP)

---

#  Project Structure

```
NimHub/
│
├── assets/
│
├── database/
│   ├── connection.py
│   ├── projects.py
│   ├── tasks.py
│   ├── portfolio.py
│   └── stats.py
│
├── pages/
│   ├── Dashboard.py
│   ├── Projects.py
│   ├── NimTask.py
│   ├── Nimfolio.py
│   ├── Statistics.py
│   └── Settings.py
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

#  Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/NimHub.git
```

### 2. Navigate into the project

```bash
cd NimHub
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the application

```bash
python main.py
```

---

#  Usage

Launch the application and use the sidebar to navigate between:

- Dashboard
- Projects
- NimTask
- Nimfolio
- Statistics
- Settings

---

#  Database

NimHub uses SQLite.

The database is automatically created on first launch.

Database tables include:

- Projects
- Tasks
- Portfolio

---

#  Roadmap

Future updates include:

- User Authentication
- Export Projects to PDF
- Calendar Integration
- Notifications
- Cloud Backup
- Themes
- Charts & Graphs
- Drag-and-Drop Tasks

---

# Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

Please ensure your code follows the project's coding style and includes appropriate documentation where necessary.

---

#  License

This project is licensed under the MIT License.

---

# Author

**Nimrod Kyalo**

Software Developer
