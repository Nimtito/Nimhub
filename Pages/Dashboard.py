"""
=========================================================
NIMHUB
pages/Dashboard.py
=========================================================
"""

import random
import customtkinter as ctk

from database.projects import (
    count_projects,
    count_completed_projects,
    count_in_progress_projects,
    get_all_projects
)

from database.tasks import (
    count_tasks,
    get_all_tasks
)


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(fg_color="#1E1E1E")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.quotes = [

            "Success is built one commit at a time.",

            "Discipline beats motivation.",

            "Build today what others dream about tomorrow.",

            "Small improvements every day become massive success.",

            "Code. Learn. Build. Repeat."

        ]
                # =====================================================
        # HEADER
        # =====================================================

        self.header = ctk.CTkFrame(
            self,
            height=100,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20,10)
        )

        self.header.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self.header,
            text="Welcome Back, Nimrod 👋",
            font=("Segoe UI", 30, "bold")
        )

        self.title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=25,
            pady=(18,0)
        )

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Developer Control Center",
            font=("Segoe UI",15)
        )

        self.subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=25
        )

        self.refresh_button = ctk.CTkButton(
            self.header,
            text="🔄 Refresh",
            width=140,
            command=self.refresh_dashboard
        )

        self.refresh_button.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=20
        )

        # =====================================================
        # STATISTICS CARDS
        # =====================================================

        self.stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.stats_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        for i in range(4):
            self.stats_frame.grid_columnconfigure(i, weight=1)

        self.project_card = self.create_card(
            "Projects",
            "0"
        )

        self.project_card.grid(
            row=0,
            column=0,
            padx=10,
            sticky="ew"
        )

        self.task_card = self.create_card(
            "Tasks",
            "0"
        )

        self.task_card.grid(
            row=0,
            column=1,
            padx=10,
            sticky="ew"
        )

        self.completed_card = self.create_card(
            "Completed",
            "0"
        )

        self.completed_card.grid(
            row=0,
            column=2,
            padx=10,
            sticky="ew"
        )

        self.progress_card = self.create_card(
            "In Progress",
            "0"
        )

        self.progress_card.grid(
            row=0,
            column=3,
            padx=10,
            sticky="ew"
        )

                # =====================================================
        # QUICK ACTIONS
        # =====================================================

        self.quick_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.quick_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        self.quick_title = ctk.CTkLabel(
            self.quick_frame,
            text="Quick Actions",
            font=("Segoe UI", 20, "bold")
        )

        self.quick_title.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )

        self.button_frame = ctk.CTkFrame(
            self.quick_frame,
            fg_color="transparent"
        )

        self.button_frame.pack(
            pady=(0,15)
        )

        self.new_project_btn = ctk.CTkButton(
            self.button_frame,
            text="➕ New Project",
            width=180
        )

        self.new_project_btn.grid(
            row=0,
            column=0,
            padx=10
        )

        self.new_task_btn = ctk.CTkButton(
            self.button_frame,
            text="✅ New Task",
            width=180
        )

        self.new_task_btn.grid(
            row=0,
            column=1,
            padx=10
        )

        self.portfolio_btn = ctk.CTkButton(
            self.button_frame,
            text="💼 Nimfolio",
            width=180
        )

        self.portfolio_btn.grid(
            row=0,
            column=2,
            padx=10
        )

        self.statistics_btn = ctk.CTkButton(
            self.button_frame,
            text="📊 Statistics",
            width=180
        )

        self.statistics_btn.grid(
            row=0,
            column=3,
            padx=10
        )

        # =====================================================
        # LOWER SECTION
        # =====================================================

        self.bottom_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.bottom_frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(10,20)
        )

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

                # =====================================================
        # RECENT PROJECTS PANEL
        # =====================================================

        self.projects_frame = ctk.CTkFrame(
            self.bottom_frame,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.projects_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0,10)
        )

        self.projects_label = ctk.CTkLabel(
            self.projects_frame,
            text="Recent Projects",
            font=("Segoe UI",20,"bold")
        )

        self.projects_label.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )

        self.projects_box = ctk.CTkTextbox(
            self.projects_frame,
            font=("Consolas",14),
            height=320
        )

        self.projects_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        self.projects_box.configure(
            state="disabled"
        )

        # =====================================================
        # RIGHT PANEL
        # =====================================================

        self.right_panel = ctk.CTkFrame(
            self.bottom_frame,
            fg_color="transparent"
        )

        self.right_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10,0)
        )

        self.right_panel.grid_rowconfigure(
            0,
            weight=3
        )

        self.right_panel.grid_rowconfigure(
            1,
            weight=1
        )

        self.right_panel.grid_columnconfigure(
            0,
            weight=1
        )

        # =====================================================
        # RECENT TASKS
        # =====================================================

        self.tasks_frame = ctk.CTkFrame(
            self.right_panel,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.tasks_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.tasks_label = ctk.CTkLabel(
            self.tasks_frame,
            text="Recent Tasks",
            font=("Segoe UI",20,"bold")
        )

        self.tasks_label.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )

        self.tasks_box = ctk.CTkTextbox(
            self.tasks_frame,
            font=("Consolas",14),
            height=180
        )

        self.tasks_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        self.tasks_box.configure(
            state="disabled"
        )

        # =====================================================
        # DEVELOPER QUOTE
        # =====================================================

        self.quote_frame = ctk.CTkFrame(
            self.right_panel,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.quote_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(10,0)
        )

        self.quote_title = ctk.CTkLabel(
            self.quote_frame,
            text="Developer Quote",
            font=("Segoe UI",18,"bold")
        )

        self.quote_title.pack(
            anchor="w",
            padx=20,
            pady=(15,5)
        )

        self.quote_label = ctk.CTkLabel(
            self.quote_frame,
            text=random.choice(self.quotes),
            wraplength=450,
            justify="left",
            font=("Segoe UI",15)
        )

        self.quote_label.pack(
            anchor="w",
            padx=20,
            pady=(0,15)
        )

        # =====================================================
        # INITIAL LOAD
        # =====================================================

        self.refresh_dashboard()
            # =====================================================
    # CREATE STAT CARD
    # =====================================================

    def create_card(self, title, value):

        card = ctk.CTkFrame(
            self.stats_frame,
            corner_radius=15,
            fg_color="#2B2B2B",
            height=130
        )

        card.grid_propagate(False)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 18)
        ).pack(pady=(20, 5))

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 34, "bold")
        )

        value_label.pack()

        if title == "Projects":
            self.project_value = value_label

        elif title == "Tasks":
            self.task_value = value_label

        elif title == "Completed":
            self.completed_value = value_label

        elif title == "In Progress":
            self.progress_value = value_label

        return card


    # =====================================================
    # LOAD STATISTICS
    # =====================================================

    def load_dashboard_stats(self):

        self.project_value.configure(
            text=str(count_projects())
        )

        self.task_value.configure(
            text=str(count_tasks())
        )

        self.completed_value.configure(
            text=str(count_completed_projects())
        )

        self.progress_value.configure(
            text=str(count_in_progress_projects())
        )


    # =====================================================
    # LOAD RECENT PROJECTS
    # =====================================================

    def load_recent_projects(self):

        self.projects_box.configure(state="normal")
        self.projects_box.delete("1.0", "end")

        projects = get_all_projects()

        if not projects:

            self.projects_box.insert(
                "end",
                "No projects available."
            )

        else:

            for project in projects[:5]:

                self.projects_box.insert(
                    "end",
                    f"📁 {project[1]}\n"
                )

                self.projects_box.insert(
                    "end",
                    f"Status : {project[3]}\n"
                )

                self.projects_box.insert(
                    "end",
                    "-" * 40 + "\n"
                )

        self.projects_box.configure(state="disabled")


    # =====================================================
    # LOAD RECENT TASKS
    # =====================================================

    def load_recent_tasks(self):

        self.tasks_box.configure(state="normal")
        self.tasks_box.delete("1.0", "end")

        tasks = get_all_tasks()

        if not tasks:

            self.tasks_box.insert(
                "end",
                "No tasks available."
            )

        else:

            for task in tasks[:5]:

                self.tasks_box.insert(
                    "end",
                    f"✅ {task[1]}\n"
                )

                self.tasks_box.insert(
                    "end",
                    f"Priority : {task[3]}\n"
                )

                self.tasks_box.insert(
                    "end",
                    f"Status   : {task[4]}\n"
                )

                self.tasks_box.insert(
                    "end",
                    "-" * 40 + "\n"
                )

        self.tasks_box.configure(state="disabled")


    # =====================================================
    # REFRESH DASHBOARD
    # =====================================================

    def refresh_dashboard(self):

        self.load_dashboard_stats()

        self.load_recent_projects()

        self.load_recent_tasks()

        self.quote_label.configure(
            text=random.choice(self.quotes)
        )