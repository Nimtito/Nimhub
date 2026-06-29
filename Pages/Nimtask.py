"""
=========================================================
NIMHUB
pages/nimtask.py

PART 1
=========================================================
"""

import customtkinter as ctk
from tkinter import messagebox

from database.tasks import (
    add_task,
    get_all_tasks,
    update_task,
    delete_task,
    search_tasks,
    complete_task
)


class NimtaskPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.selected_task = None

        self.configure(fg_color="#1E1E1E")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # =====================================================
        # HEADER
        # =====================================================

        self.header = ctk.CTkFrame(
            self,
            height=80,
            fg_color="#2B2B2B",
            corner_radius=15
        )

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(20,10)
        )

        self.title = ctk.CTkLabel(
            self.header,
            text="NimTask",
            font=("Segoe UI",30,"bold")
        )

        self.title.pack(
            anchor="w",
            padx=20,
            pady=(15,0)
        )

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Task Management System",
            font=("Segoe UI",15)
        )

        self.subtitle.pack(
            anchor="w",
            padx=20
        )

        # =====================================================
        # LEFT PANEL
        # =====================================================

        self.left_frame = ctk.CTkFrame(
            self,
            width=370,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.left_frame.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=(20,10),
            pady=(10,20)
        )

        self.left_frame.grid_propagate(False)

        ctk.CTkLabel(
            self.left_frame,
            text="Task Details",
            font=("Segoe UI",22,"bold")
        ).pack(
            pady=(20,15)
        )

        # =====================================================
        # TITLE
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Task Title",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.title_entry = ctk.CTkEntry(
            self.left_frame,
            height=40
        )

        self.title_entry.pack(
            fill="x",
            padx=20,
            pady=(5,15)
        )

        # =====================================================
        # DESCRIPTION
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Description",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.description_box = ctk.CTkTextbox(
            self.left_frame,
            height=140
        )

        self.description_box.pack(
            fill="x",
            padx=20,
            pady=(5,15)
        )

        # =====================================================
        # PRIORITY
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Priority",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.priority_option = ctk.CTkOptionMenu(
            self.left_frame,
            values=[
                "Low",
                "Medium",
                "High"
            ]
        )

        self.priority_option.pack(
            fill="x",
            padx=20,
            pady=(5,15)
        )

        self.priority_option.set("Medium")

        # =====================================================
        # DUE DATE
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Due Date",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.due_date_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="YYYY-MM-DD"
        )

        self.due_date_entry.pack(
            fill="x",
            padx=20,
            pady=(5,15)
        )

        # =====================================================
        # STATUS
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Status",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.status_option = ctk.CTkOptionMenu(
            self.left_frame,
            values=[
                "Pending",
                "Completed"
            ]
        )

        self.status_option.pack(
            fill="x",
            padx=20,
            pady=(5,20)
        )

        self.status_option.set("Pending")

        # =====================================================
        # BUTTONS
        # =====================================================

        self.add_button = ctk.CTkButton(
            self.left_frame,
            text="Add Task",
            height=42,
            command=self.add_new_task
        )

        self.add_button.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.update_button = ctk.CTkButton(
            self.left_frame,
            text="Update Task",
            height=42,
            command=self.update_selected_task
        )

        self.update_button.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.complete_button = ctk.CTkButton(
            self.left_frame,
            text="Mark Completed",
            height=42,
            command=self.mark_completed
        )

        self.complete_button.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.delete_button = ctk.CTkButton(
            self.left_frame,
            text="Delete Task",
            height=42,
            fg_color="firebrick",
            hover_color="#8B0000",
            command=self.delete_selected_task
        )

        self.delete_button.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.clear_button = ctk.CTkButton(
            self.left_frame,
            text="Clear Form",
            height=42,
            command=self.clear_form
        )

        self.clear_button.pack(
            fill="x",
            padx=20,
            pady=(5,20)
        )

                # =====================================================
        # RIGHT PANEL
        # =====================================================

        self.right_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.right_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10,20),
            pady=(10,20)
        )

        self.right_frame.grid_rowconfigure(2, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # =====================================================
        # SEARCH
        # =====================================================

        self.search_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color="transparent"
        )

        self.search_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20,10)
        )

        self.search_frame.grid_columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            placeholder_text="Search task..."
        )

        self.search_entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0,10)
        )

        self.search_button = ctk.CTkButton(
            self.search_frame,
            text="Search",
            width=120,
            command=self.search_for_task
        )

        self.search_button.grid(
            row=0,
            column=1,
            padx=(0,10)
        )

        self.show_all_button = ctk.CTkButton(
            self.search_frame,
            text="Show All",
            width=120,
            command=self.load_tasks
        )

        self.show_all_button.grid(
            row=0,
            column=2
        )

        # =====================================================
        # TASK LIST TITLE
        # =====================================================

        self.list_title = ctk.CTkLabel(
            self.right_frame,
            text="Task List",
            font=("Segoe UI",22,"bold")
        )

        self.list_title.grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(10,5)
        )

        # =====================================================
        # TASK LIST
        # =====================================================

        self.tasks_list = ctk.CTkTextbox(
            self.right_frame,
            font=("Consolas",14)
        )

        self.tasks_list.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(5,20)
        )

        # =====================================================
        # SELECTED TASK
        # =====================================================

        self.selected_label = ctk.CTkLabel(
            self.right_frame,
            text="Selected Task ID : None",
            font=("Segoe UI",15,"bold")
        )

        self.selected_label.grid(
            row=3,
            column=0,
            sticky="w",
            padx=20,
            pady=(0,15)
        )

        # =====================================================
        # INITIAL LOAD
        # =====================================================

        self.load_tasks()

        self.tasks_list.bind(
            "<Double-Button-1>",
            self.select_task
        )
            # =====================================================
    # LOAD TASKS
    # =====================================================

    def load_tasks(self):

        tasks = get_all_tasks()

        self.display_tasks(tasks)


    # =====================================================
    # SEARCH TASK
    # =====================================================

    def search_for_task(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_tasks()

            return

        tasks = search_tasks(keyword)

        self.display_tasks(tasks)


    # =====================================================
    # DISPLAY TASKS
    # =====================================================

    def display_tasks(self, tasks):

        self.tasks_list.configure(state="normal")

        self.tasks_list.delete("1.0", "end")

        if not tasks:

            self.tasks_list.insert(
                "end",
                "No tasks found."
            )

            self.tasks_list.configure(state="disabled")

            return

        for task in tasks:

            task_id = task[0]
            title = task[1]
            description = task[2]
            priority = task[3]
            due_date = task[4]
            status = task[5]
            date_created = task[6]
            last_updated = task[7]

            self.tasks_list.insert(
                "end",
                f"ID: {task_id}\n"
            )

            self.tasks_list.insert(
                "end",
                f"Title: {title}\n"
            )

            self.tasks_list.insert(
                "end",
                f"Priority: {priority}\n"
            )

            self.tasks_list.insert(
                "end",
                f"Due Date: {due_date}\n"
            )

            self.tasks_list.insert(
                "end",
                f"Status: {status}\n"
            )

            self.tasks_list.insert(
                "end",
                f"Description: {description}\n"
            )

            self.tasks_list.insert(
                "end",
                f"Created: {date_created}\n"
            )

            self.tasks_list.insert(
                "end",
                f"Updated: {last_updated}\n"
            )

            self.tasks_list.insert(
                "end",
                "=" * 70 + "\n"
            )

        self.tasks_list.configure(state="disabled")


    # =====================================================
    # SELECT TASK
    # =====================================================

    def select_task(self, event=None):

        try:

            index = self.tasks_list.index("insert")

            line = self.tasks_list.get(
                f"{index} linestart",
                f"{index} lineend"
            )

            if not line.startswith("ID:"):

                return

            task_id = int(
                line.replace("ID:", "").strip()
            )

            tasks = get_all_tasks()

            for task in tasks:

                if task[0] == task_id:

                    self.selected_task = task

                    self.selected_label.configure(
                        text=f"Selected Task ID : {task_id}"
                    )

                    self.title_entry.delete(0, "end")
                    self.title_entry.insert(0, task[1])

                    self.description_box.delete("1.0", "end")
                    self.description_box.insert("1.0", task[2])

                    self.priority_option.set(task[3])

                    self.due_date_entry.delete(0, "end")
                    self.due_date_entry.insert(0, task[4])

                    self.status_option.set(task[5])

                    break

        except Exception:

            messagebox.showerror(
                "Selection Error",
                "Double-click the task ID line to load a task."
            )

                # =====================================================
    # ADD NEW TASK
    # =====================================================

    def add_new_task(self):

        title = self.title_entry.get().strip()

        description = self.description_box.get(
            "1.0",
            "end"
        ).strip()

        priority = self.priority_option.get()

        due_date = self.due_date_entry.get().strip()

        status = self.status_option.get()

        if title == "":

            messagebox.showwarning(
                "Missing Information",
                "Task title is required."
            )

            return

        add_task(
            title,
            description,
            priority,
            due_date,
            status
        )

        messagebox.showinfo(
            "Success",
            "Task added successfully."
        )

        self.clear_form()

        self.load_tasks()


    # =====================================================
    # UPDATE TASK
    # =====================================================

    def update_selected_task(self):

        if self.selected_task is None:

            messagebox.showwarning(
                "No Task Selected",
                "Please select a task first."
            )

            return

        title = self.title_entry.get().strip()

        description = self.description_box.get(
            "1.0",
            "end"
        ).strip()

        priority = self.priority_option.get()

        due_date = self.due_date_entry.get().strip()

        status = self.status_option.get()

        if title == "":

            messagebox.showwarning(
                "Missing Information",
                "Task title cannot be empty."
            )

            return

        update_task(
            self.selected_task[0],
            title,
            description,
            priority,
            due_date,
            status
        )

        messagebox.showinfo(
            "Updated",
            "Task updated successfully."
        )

        self.load_tasks()

        self.clear_form()


    # =====================================================
    # MARK TASK COMPLETED
    # =====================================================

    def mark_completed(self):

        if self.selected_task is None:

            messagebox.showwarning(
                "No Task Selected",
                "Please select a task first."
            )

            return

        complete_task(
            self.selected_task[0]
        )

        messagebox.showinfo(
            "Completed",
            "Task marked as completed."
        )

        self.load_tasks()

        self.clear_form()


    # =====================================================
    # DELETE TASK
    # =====================================================

    def delete_selected_task(self):

        if self.selected_task is None:

            messagebox.showwarning(
                "No Task Selected",
                "Please select a task first."
            )

            return

        answer = messagebox.askyesno(
            "Delete Task",
            f"Delete '{self.selected_task[1]}'?"
        )

        if not answer:
            return

        delete_task(
            self.selected_task[0]
        )

        messagebox.showinfo(
            "Deleted",
            "Task deleted successfully."
        )

        self.load_tasks()

        self.clear_form()


    # =====================================================
    # CLEAR FORM
    # =====================================================

    def clear_form(self):

        self.selected_task = None

        self.selected_label.configure(
            text="Selected Task ID : None"
        )

        self.title_entry.delete(
            0,
            "end"
        )

        self.description_box.delete(
            "1.0",
            "end"
        )

        self.priority_option.set(
            "Medium"
        )

        self.due_date_entry.delete(
            0,
            "end"
        )

        self.status_option.set(
            "Pending"
        )

        self.search_entry.delete(
            0,
            "end"
        )