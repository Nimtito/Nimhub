"""
=========================================================
NIMHUB
pages/statistics.py

PART 1
=========================================================
"""

import customtkinter as ctk

from database.projects import (
    count_projects,
    count_completed_projects,
    count_in_progress_projects
)

from database.tasks import (
    count_tasks,
    count_completed_tasks,
    count_pending_tasks,
    task_completion_percentage,
)


class StatisticsPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(fg_color="#1E1E1E")

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(2, weight=1)

        # =====================================================
        # HEADER
        # =====================================================

        self.header = ctk.CTkFrame(
            self,
            height=90,
            fg_color="#2B2B2B",
            corner_radius=15
        )

        self.header.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=20,
            pady=(20,10)
        )

        self.title = ctk.CTkLabel(
            self.header,
            text="Statistics Dashboard",
            font=("Segoe UI",30,"bold")
        )

        self.title.pack(
            anchor="w",
            padx=20,
            pady=(15,0)
        )

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Overview of Projects and Tasks",
            font=("Segoe UI",15)
        )

        self.subtitle.pack(
            anchor="w",
            padx=20
        )

        # =====================================================
        # STATISTICS CARDS
        # =====================================================

        self.total_projects = self.create_card(
            row=1,
            column=0,
            title="Projects"
        )

        self.total_tasks = self.create_card(
            row=1,
            column=1,
            title="Tasks"
        )

        self.productivity = self.create_card(
            row=1,
            column=2,
            title="Productivity"
        )

                # =====================================================
        # ANALYTICS PANEL
        # =====================================================

        self.analytics_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.analytics_frame.grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="nsew",
            padx=20,
            pady=(10,20)
        )

        self.analytics_frame.grid_columnconfigure((0,1), weight=1)
        self.analytics_frame.grid_rowconfigure(1, weight=1)

        # =====================================================
        # PROJECT STATISTICS
        # =====================================================

        self.project_frame = ctk.CTkFrame(
            self.analytics_frame,
            fg_color="#252525",
            corner_radius=12
        )

        self.project_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(15,8),
            pady=15
        )

        self.project_title = ctk.CTkLabel(
            self.project_frame,
            text="Project Statistics",
            font=("Segoe UI",20,"bold")
        )

        self.project_title.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )

        self.project_box = ctk.CTkTextbox(
            self.project_frame,
            height=260,
            font=("Consolas",15)
        )

        self.project_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        # =====================================================
        # TASK STATISTICS
        # =====================================================

        self.task_frame = ctk.CTkFrame(
            self.analytics_frame,
            fg_color="#252525",
            corner_radius=12
        )

        self.task_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8,15),
            pady=15
        )

        self.task_title = ctk.CTkLabel(
            self.task_frame,
            text="Task Statistics",
            font=("Segoe UI",20,"bold")
        )

        self.task_title.pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )

        self.task_box = ctk.CTkTextbox(
            self.task_frame,
            height=260,
            font=("Consolas",15)
        )

        self.task_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        # =====================================================
        # LOAD STATISTICS
        # =====================================================

        self.refresh_statistics()
            # =====================================================
    # CREATE STAT CARD
    # =====================================================

    def create_card(self, row, column, title):

        card = ctk.CTkFrame(
            self,
            fg_color="#2B2B2B",
            corner_radius=15,
            height=130
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=10,
            pady=(5,10)
        )

        card.grid_propagate(False)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI",18)
        ).pack(
            pady=(20,8)
        )

        value = ctk.CTkLabel(
            card,
            text="0",
            font=("Segoe UI",36,"bold")
        )

        value.pack()

        if title == "Projects":
            self.projects_value = value

        elif title == "Tasks":
            self.tasks_value = value

        elif title == "Productivity":
            self.productivity_value = value

        return card


    # =====================================================
    # REFRESH ALL STATISTICS
    # =====================================================

    def refresh_statistics(self):

        self.projects_value.configure(
            text=str(count_projects())
        )

        self.tasks_value.configure(
            text=str(count_tasks())
        )

        self.productivity_value.configure(
            text=f"{task_completion_percentage()}%"
        )

        self.load_project_statistics()

        self.load_task_statistics()


    # =====================================================
    # LOAD PROJECT STATISTICS
    # =====================================================

    def load_project_statistics(self):

        self.project_box.configure(state="normal")

        self.project_box.delete("1.0", "end")

        total = count_projects()
        completed = count_completed_projects()
        progress = count_in_progress_projects()

        self.project_box.insert(
            "end",
            "PROJECT ANALYTICS\n"
        )

        self.project_box.insert(
            "end",
            "=" * 45 + "\n\n"
        )

        self.project_box.insert(
            "end",
            f"Total Projects      : {total}\n\n"
        )

        self.project_box.insert(
            "end",
            f"Completed Projects  : {completed}\n\n"
        )

        self.project_box.insert(
            "end",
            f"In Progress         : {progress}\n\n"
        )

        if total == 0:

            completion = 0

        else:

            completion = round(
                (completed / total) * 100,
                2
            )

        self.project_box.insert(
            "end",
            f"Completion Rate     : {completion}%\n"
        )

        self.project_box.configure(state="disabled")


    # =====================================================
    # LOAD TASK STATISTICS
    # =====================================================

    def load_task_statistics(self):

        self.task_box.configure(state="normal")

        self.task_box.delete("1.0", "end")

        total = count_tasks()
        completed = count_completed_tasks()
        pending = count_pending_tasks()
        productivity = task_completion_percentage()

        self.task_box.insert(
            "end",
            "TASK ANALYTICS\n"
        )

        self.task_box.insert(
            "end",
            "=" * 45 + "\n\n"
        )

        self.task_box.insert(
            "end",
            f"Total Tasks         : {total}\n\n"
        )

        self.task_box.insert(
            "end",
            f"Completed Tasks     : {completed}\n\n"
        )

        self.task_box.insert(
            "end",
            f"Pending Tasks       : {pending}\n\n"
        )

        self.task_box.insert(
            "end",
            f"Productivity Score  : {productivity}%\n\n"
        )

        if productivity >= 90:

            message = "Outstanding productivity."

        elif productivity >= 70:

            message = "Excellent progress."

        elif productivity >= 50:

            message = "Good progress."

        elif productivity >= 30:

            message = "Needs improvement."

        else:

            message = "Start completing more tasks."

        self.task_box.insert(
            "end",
            f"Assessment:\n{message}"
        )

        self.task_box.configure(state="disabled")