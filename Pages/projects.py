"""
=========================================================
NIMHUB
pages/projects.py

PART 1
=========================================================
"""

import customtkinter as ctk
from tkinter import messagebox

from database.projects import (
    add_project,
    get_all_projects,
    update_project,
    delete_project,
    search_projects
)


class ProjectsPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.selected_project = None

        self.configure(fg_color="#1E1E1E")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ==========================================
        # HEADER
        # ==========================================

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
            text="Project Manager",
            font=("Segoe UI",28,"bold")
        )

        self.title.pack(
            anchor="w",
            padx=20,
            pady=(18,0)
        )

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Create, edit and manage your projects",
            font=("Segoe UI",15)
        )

        self.subtitle.pack(
            anchor="w",
            padx=20
        )

        # ==========================================
        # LEFT PANEL
        # ==========================================

        self.form_frame = ctk.CTkFrame(
            self,
            width=360,
            corner_radius=15,
            fg_color="#2B2B2B"
        )

        self.form_frame.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=(20,10),
            pady=(10,20)
        )

        self.form_frame.grid_propagate(False)

        ctk.CTkLabel(
            self.form_frame,
            text="Project Details",
            font=("Segoe UI",22,"bold")
        ).pack(
            pady=(20,15)
        )

        # ==========================================
        # PROJECT NAME
        # ==========================================

        ctk.CTkLabel(
            self.form_frame,
            text="Project Name",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.name_entry = ctk.CTkEntry(
            self.form_frame,
            height=40
        )

        self.name_entry.pack(
            fill="x",
            padx=20,
            pady=(5,15)
        )

        # ==========================================
        # DESCRIPTION
        # ==========================================

        ctk.CTkLabel(
            self.form_frame,
            text="Description",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.description_box = ctk.CTkTextbox(
            self.form_frame,
            height=140
        )

        self.description_box.pack(
            fill="x",
            padx=20,
            pady=(5,15)
        )

        # ==========================================
        # STATUS
        # ==========================================

        ctk.CTkLabel(
            self.form_frame,
            text="Status",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.status_option = ctk.CTkOptionMenu(
            self.form_frame,
            values=[
                "In Progress",
                "Completed"
            ]
        )

        self.status_option.pack(
            fill="x",
            padx=20,
            pady=(5,20)
        )

        self.status_option.set("In Progress")

        # ==========================================
        # BUTTONS
        # ==========================================

        self.add_button = ctk.CTkButton(
            self.form_frame,
            text="Add Project",
            height=42,
            command=self.add_new_project
        )

        self.add_button.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.update_button = ctk.CTkButton(
            self.form_frame,
            text="Update Project",
            height=42,
            command=self.update_selected_project
        )

        self.update_button.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.delete_button = ctk.CTkButton(
            self.form_frame,
            text="Delete Project",
            height=42,
            fg_color="firebrick",
            hover_color="#8B0000",
            command=self.delete_selected_project
        )

        self.delete_button.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.clear_button = ctk.CTkButton(
            self.form_frame,
            text="Clear Form",
            height=42,
            command=self.clear_form
        )

        self.clear_button.pack(
            fill="x",
            padx=20,
            pady=(5,20)
        )


                # ==========================================
        # RIGHT PANEL
        # ==========================================

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

        # ==========================================
        # SEARCH
        # ==========================================

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
            placeholder_text="Search project..."
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
            command=self.search_for_project
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
            command=self.load_projects
        )

        self.show_all_button.grid(
            row=0,
            column=2
        )

        # ==========================================
        # PROJECT LIST TITLE
        # ==========================================

        self.list_title = ctk.CTkLabel(
            self.right_frame,
            text="Saved Projects",
            font=("Segoe UI",22,"bold")
        )

        self.list_title.grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(10,5)
        )

        # ==========================================
        # PROJECTS LISTBOX
        # ==========================================

        self.projects_list = ctk.CTkTextbox(
            self.right_frame,
            font=("Consolas",14)
        )

        self.projects_list.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(5,20)
        )

        # ==========================================
        # PROJECT ID
        # ==========================================

        self.id_label = ctk.CTkLabel(
            self.right_frame,
            text="Selected Project ID : None",
            font=("Segoe UI",15,"bold")
        )

        self.id_label.grid(
            row=3,
            column=0,
            sticky="w",
            padx=20,
            pady=(0,15)
        )

        # ==========================================
        # LOAD DATA
        # ==========================================

        self.load_projects()

        # ==========================================
        # DOUBLE CLICK TO LOAD PROJECT
        # ==========================================

        self.projects_list.bind(
            "<Double-Button-1>",
            self.select_project
        )

            # ==========================================
    # LOAD PROJECTS
    # ==========================================

    def load_projects(self):

        projects = get_all_projects()

        self.display_projects(projects)


    # ==========================================
    # SEARCH PROJECT
    # ==========================================

    def search_for_project(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_projects()

            return

        results = search_projects(keyword)

        self.display_projects(results)


    # ==========================================
    # DISPLAY PROJECTS
    # ==========================================

    def display_projects(self, projects):

        self.projects_list.configure(state="normal")

        self.projects_list.delete("1.0", "end")

        if not projects:

            self.projects_list.insert(
                "end",
                "No projects found."
            )

            self.projects_list.configure(state="disabled")

            return

        for project in projects:

            project_id = project[0]
            name = project[1]
            description = project[2]
            status = project[3]
            date_created = project[4]
            last_updated = project[5]

            self.projects_list.insert(
                "end",
                f"ID: {project_id}\n"
            )

            self.projects_list.insert(
                "end",
                f"Project: {name}\n"
            )

            self.projects_list.insert(
                "end",
                f"Status: {status}\n"
            )

            self.projects_list.insert(
                "end",
                f"Description: {description}\n"
            )

            self.projects_list.insert(
                "end",
                f"Created: {date_created}\n"
            )

            self.projects_list.insert(
                "end",
                f"Updated: {last_updated}\n"
            )

            self.projects_list.insert(
                "end",
                "=" * 70 + "\n"
            )

        self.projects_list.configure(state="disabled")


    # ==========================================
    # SELECT PROJECT
    # ==========================================

    def select_project(self, event=None):

        try:

            index = self.projects_list.index("insert")

            line = self.projects_list.get(
                f"{index} linestart",
                f"{index} lineend"
            )

            if not line.startswith("ID:"):
                return

            project_id = int(
                line.replace("ID:", "").strip()
            )

            projects = get_all_projects()

            for project in projects:

                if project[0] == project_id:

                    self.selected_project = project

                    self.id_label.configure(
                        text=f"Selected Project ID : {project_id}"
                    )

                    self.name_entry.delete(0, "end")
                    self.name_entry.insert(0, project[1])

                    self.description_box.delete("1.0", "end")
                    self.description_box.insert("1.0", project[2])

                    self.status_option.set(project[3])

                    break

        except Exception:

            messagebox.showerror(
                "Selection Error",
                "Please double-click the project's ID line to load it."
            )
                # ==========================================
    # ADD NEW PROJECT
    # ==========================================

    def add_new_project(self):

        name = self.name_entry.get().strip()

        description = self.description_box.get(
            "1.0",
            "end"
        ).strip()

        status = self.status_option.get()

        if not name:

            messagebox.showwarning(
                "Missing Information",
                "Project name is required."
            )

            return

        add_project(
            name,
            description,
            status
        )

        messagebox.showinfo(
            "Success",
            "Project added successfully."
        )

        self.clear_form()

        self.load_projects()


    # ==========================================
    # UPDATE PROJECT
    # ==========================================

    def update_selected_project(self):

        if self.selected_project is None:

            messagebox.showwarning(
                "No Selection",
                "Please select a project first."
            )

            return

        project_id = self.selected_project[0]

        name = self.name_entry.get().strip()

        description = self.description_box.get(
            "1.0",
            "end"
        ).strip()

        status = self.status_option.get()

        if not name:

            messagebox.showwarning(
                "Missing Information",
                "Project name cannot be empty."
            )

            return

        update_project(
            project_id,
            name,
            description,
            status
        )

        messagebox.showinfo(
            "Updated",
            "Project updated successfully."
        )

        self.load_projects()

        self.clear_form()


    # ==========================================
    # DELETE PROJECT
    # ==========================================

    def delete_selected_project(self):

        if self.selected_project is None:

            messagebox.showwarning(
                "No Selection",
                "Please select a project first."
            )

            return

        answer = messagebox.askyesno(
            "Delete Project",
            f"Delete '{self.selected_project[1]}'?"
        )

        if not answer:
            return

        delete_project(
            self.selected_project[0]
        )

        messagebox.showinfo(
            "Deleted",
            "Project deleted successfully."
        )

        self.clear_form()

        self.load_projects()


    # ==========================================
    # CLEAR FORM
    # ==========================================

    def clear_form(self):

        self.selected_project = None

        self.id_label.configure(
            text="Selected Project ID : None"
        )

        self.name_entry.delete(
            0,
            "end"
        )

        self.description_box.delete(
            "1.0",
            "end"
        )

        self.status_option.set(
            "In Progress"
        )

        self.search_entry.delete(
            0,
            "end"
        )