import customtkinter as ctk
from tkinter import messagebox

from database.database import (
    get_all_projects,
    add_project,
    update_project,
    delete_project,
    search_projects,
    count_projects,
    count_completed_projects,
    count_in_progress_projects
)


class NimTaskPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.configure(fg_color="#1E1E1E")

        self.build_header()

        self.build_statistics()

        self.build_toolbar()

        self.build_projects_area()

        self.load_projects()

    # ==================================================
    # HEADER
    # ==================================================

    def build_header(self):

        header = ctk.CTkFrame(self)

        header.pack(fill="x", padx=20, pady=(20, 10))

        title = ctk.CTkLabel(
            header,
            text="NIMTASK",
            font=("Arial", 28, "bold")
        )

        title.pack(side="left", padx=20, pady=15)

        subtitle = ctk.CTkLabel(
            header,
            text="Project Management Center",
            font=("Arial", 16)
        )

        subtitle.pack(side="left", padx=10)

    # ==================================================
    # STATISTICS
    # ==================================================

    def build_statistics(self):

        frame = ctk.CTkFrame(self)

        frame.pack(fill="x", padx=20, pady=10)

        self.total_projects = ctk.CTkLabel(
            frame,
            text="Projects : 0",
            font=("Arial", 18)
        )

        self.total_projects.pack(side="left", padx=20, pady=15)

        self.completed_projects = ctk.CTkLabel(
            frame,
            text="Completed : 0",
            font=("Arial", 18)
        )

        self.completed_projects.pack(side="left", padx=20)

        self.progress_projects = ctk.CTkLabel(
            frame,
            text="In Progress : 0",
            font=("Arial", 18)
        )

        self.progress_projects.pack(side="left", padx=20)

    # ==================================================
    # TOOLBAR
    # ==================================================

    def build_toolbar(self):

        toolbar = ctk.CTkFrame(self)

        toolbar.pack(fill="x", padx=20, pady=10)

        self.search_entry = ctk.CTkEntry(
            toolbar,
            width=300,
            placeholder_text="Search Project..."
        )

        self.search_entry.pack(side="left", padx=10, pady=10)

        search_btn = ctk.CTkButton(
            toolbar,
            text="Search",
            command=self.search_project
        )

        search_btn.pack(side="left", padx=5)

        refresh_btn = ctk.CTkButton(
            toolbar,
            text="Refresh",
            command=self.load_projects
        )

        refresh_btn.pack(side="left", padx=5)

        add_btn = ctk.CTkButton(
            toolbar,
            text="Add Project",
            command=self.add_project_popup
        )

        add_btn.pack(side="right", padx=10)

    # ==================================================
    # PROJECTS AREA
    # ==================================================

    def build_projects_area(self):

        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            width=900,
            height=500
        )

        self.scroll_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ==================================================
    # UPDATE STATISTICS
    # ==================================================

    def update_statistics(self):

        total = count_projects()

        completed = count_completed_projects()

        progress = count_in_progress_projects()

        self.total_projects.configure(
            text=f"Projects : {total}"
        )

        self.completed_projects.configure(
            text=f"Completed : {completed}"
        )

        self.progress_projects.configure(
            text=f"In Progress : {progress}"
        )

    # ==================================================
    # CLEAR PROJECT CARDS
    # ==================================================

    def clear_projects(self):

        for widget in self.scroll_frame.winfo_children():

            widget.destroy()

    # ==================================================
    # LOAD PROJECTS
    # ==================================================

    def load_projects(self):

        self.clear_projects()

        self.update_statistics()

        projects = get_all_projects()

        if not projects:

            empty = ctk.CTkLabel(

                self.scroll_frame,

                text="No Projects Found",

                font=("Arial",18)

            )

            empty.pack(pady=30)

            return

        for project in projects:

            self.create_project_card(project)

    

# ==================================================
# PROFESSIONAL PROJECT CARD
# ==================================================

def create_project_card(self, project):

    project_id = project[0]
    name = project[1]
    description = project[2]
    status = project[3]
    created = project[4]
    updated = project[5]

    if status == "Completed":
        status_color = "#2ECC71"
    else:
        status_color = "#F39C12"

    card = ctk.CTkFrame(
        self.scroll_frame,
        corner_radius=15,
        border_width=1
    )

    card.pack(
        fill="x",
        padx=15,
        pady=12
    )

    # --------------------------------------------
    # TOP
    # --------------------------------------------

    top = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    top.pack(fill="x", padx=15, pady=(15,5))

    title = ctk.CTkLabel(
        top,
        text=name,
        font=("Arial",22,"bold")
    )

    title.pack(side="left")

    badge = ctk.CTkLabel(
        top,
        text=status,
        fg_color=status_color,
        corner_radius=20,
        width=120,
        height=30
    )

    badge.pack(side="right")

    # --------------------------------------------
    # DESCRIPTION
    # --------------------------------------------

    desc = ctk.CTkLabel(
        card,
        text=description,
        wraplength=700,
        justify="left",
        anchor="w"
    )

    desc.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # --------------------------------------------
    # DATES
    # --------------------------------------------

    dates = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    dates.pack(fill="x", padx=20)

    created_label = ctk.CTkLabel(
        dates,
        text=f"Created : {created}"
    )

    created_label.pack(
        side="left"
    )

    updated_label = ctk.CTkLabel(
        dates,
        text=f"Updated : {updated}"
    )

    updated_label.pack(
        side="right"
    )

    # --------------------------------------------
    # BUTTONS
    # --------------------------------------------

    buttons = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    buttons.pack(
        fill="x",
        padx=15,
        pady=15
    )

    edit_btn = ctk.CTkButton(
        buttons,
        text="✏ Edit",
        width=90,
        command=lambda:self.edit_project(project)
    )

    edit_btn.pack(side="left",padx=5)

    complete_btn = ctk.CTkButton(
        buttons,
        text="✔ Complete",
        width=120,
        fg_color="#2ECC71",
        hover_color="#27AE60",
        command=lambda:self.complete_project(project)
    )

    complete_btn.pack(side="left",padx=5)

    delete_btn = ctk.CTkButton(
        buttons,
        text="🗑 Delete",
        width=100,
        fg_color="#E74C3C",
        hover_color="#C0392B",
        command=lambda:self.remove_project(project)
    )

    delete_btn.pack(side="left",padx=5)

    
        # ==================================================
# ADD PROJECT
# ==================================================

def add_project_popup(self):

    window = ctk.CTkToplevel(self)
    window.title("Add Project")
    window.geometry("500x420")
    window.grab_set()

    ctk.CTkLabel(
        window,
        text="Project Name"
    ).pack(pady=(20,5))

    name_entry = ctk.CTkEntry(window, width=350)
    name_entry.pack()

    ctk.CTkLabel(
        window,
        text="Description"
    ).pack(pady=(20,5))

    description_box = ctk.CTkTextbox(
        window,
        width=350,
        height=120
    )
    description_box.pack()

    ctk.CTkLabel(
        window,
        text="Status"
    ).pack(pady=(20,5))

    status = ctk.CTkOptionMenu(
        window,
        values=[
            "In Progress",
            "Completed"
        ]
    )

    status.pack()

    def save():

        name = name_entry.get().strip()

        description = description_box.get(
            "1.0",
            "end"
        ).strip()

        project_status = status.get()

        if name == "":

            messagebox.showwarning(
                "Warning",
                "Project name is required."
            )

            return

        add_project(
            name,
            description,
            project_status
        )

        window.destroy()

        self.load_projects()

    ctk.CTkButton(
        window,
        text="Save Project",
        command=save
    ).pack(pady=25)

    
        # ==================================================
# SEARCH PROJECT
# ==================================================

def search_project(self):

    keyword = self.search_entry.get().strip()

    self.clear_projects()

    if keyword == "":

        self.load_projects()

        return

    projects = search_projects(keyword)

    if not projects:

        label = ctk.CTkLabel(
            self.scroll_frame,
            text="No matching projects found.",
            font=("Arial",18)
        )

        label.pack(pady=40)

        return

    for project in projects:

        self.create_project_card(project)

    
        # ==================================================
# EDIT PROJECT
# ==================================================

def edit_project(self, project):

    project_id = project[0]

    window = ctk.CTkToplevel(self)
    window.title("Edit Project")
    window.geometry("500x420")
    window.grab_set()

    ctk.CTkLabel(window,text="Project Name").pack(pady=(20,5))

    name_entry = ctk.CTkEntry(
        window,
        width=350
    )

    name_entry.insert(0, project[1])

    name_entry.pack()

    ctk.CTkLabel(
        window,
        text="Description"
    ).pack(pady=(20,5))

    description_box = ctk.CTkTextbox(
        window,
        width=350,
        height=120
    )

    description_box.insert(
        "1.0",
        project[2]
    )

    description_box.pack()

    status = ctk.CTkOptionMenu(
        window,
        values=[
            "In Progress",
            "Completed"
        ]
    )

    status.set(project[3])

    status.pack(pady=20)

    def update():

        update_project(

            project_id,

            name_entry.get(),

            description_box.get(
                "1.0",
                "end"
            ).strip(),

            status.get()

        )

        window.destroy()

        self.load_projects()

    ctk.CTkButton(

        window,

        text="Update",

        command=update

    ).pack(pady=20)

        # ==================================================
# MARK PROJECT COMPLETE
# ==================================================

# ==================================================
# SHOW COMPLETED PROJECTS
# ==================================================

def show_completed(self):

    self.clear_projects()

    projects = get_all_projects()

    for project in projects:

        if project[3] == "Completed":

            self.create_project_card(project)


# ==================================================
# SHOW IN PROGRESS PROJECTS
# ==================================================

def show_progress(self):

    self.clear_projects()

    projects = get_all_projects()

    for project in projects:

        if project[3] == "In Progress":

            self.create_project_card(project)


    # ==================================================
# DELETE PROJECT
# ==================================================

def remove_project(self, project):

    answer = messagebox.askyesno(

        "Delete Project",

        f"Delete '{project[1]}'?"

    )

    if answer:

        delete_project(

            project[0]

        )

        self.load_projects()