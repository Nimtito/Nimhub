# NimHub

## Description
NimHub is a command-line developer control center built with Python. It helps a user manage, track, and launch Python projects from one place. Instead of having projects scattered across folders, NimHub provides a central dashboard for organizing project information, updating project status, viewing project statistics, and opening related tools .

## Problem Statement
As a beginner developer building multiple Python projects, it becomes easy for projects to be scattered across different files and folders. This makes it difficult to:
- keep track of created projects
- know which projects are complete and which are still in progress
- manage project information in one place
- access related tools quickly

# Solution
NimHub solves this problem by providing a single command-line dashboard where the user can:
- add and manage projects
- track project completion status
- view all projects in one place
- launch related tools such as NimTask and Nimfolio
- view simple developer statistics

## Features
### 1. Main Dashboard
A central menu for navigating to:
- Projects Manager
- Tools
- Developer Stats
- Exit

### 2. Projects Manager
Allows the user to:
- add a project
- view all projects
- update project status
- delete a project

Each project contains:
- project name
- description
- status

### 3. Tools Section
Displays available tools such as:
- NimTask
- Nimfolio

### 4. Developer Stats
Shows:
- total number of projects
- number of completed projects
- number of in-progress projects

### 5. Data Storage
Stores project data in a JSON file so that it remains available after the program is closed.

---

## Tech Stack
- Python
- JSON for data storage
- VS Code
- Git
- Virtual environment (venv)

### Python Concepts Used
- Variables
- Input and Output
- Conditional Statements
- Loops
- Functions
- Lists
- Dictionaries
- File Handling
- JSON
- Modules / Imports
- Basic Exception Handling
## Project Structure
```text
nimhub/
│
├── main.py
├── projects.py
├── tools.py
├── stats.py
├── storage.py
├── README.md
├── .gitignore
└── data/
    └── nimhub_data.json