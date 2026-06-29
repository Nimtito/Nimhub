"""
=========================================================
NIMHUB
Developer Control Center

main.py
=========================================================
"""

import customtkinter as ctk

from pages.Dashboard import DashboardPage
from pages.projects import ProjectsPage
from pages.Nimtask import NimtaskPage
from pages.Nimfolio import NimfolioPage
from pages.stats import StatisticsPage


# =========================================================
# APP SETTINGS
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================================================
# MAIN APPLICATION
# =========================================================

class NimHub(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("NimHub - Developer Control Center")

        self.geometry("1400x800")

        self.minsize(1200, 700)

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.sidebar.grid_propagate(False)

        # =====================================================
        # CONTENT
        # =====================================================

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.content.grid_rowconfigure(0, weight=1)

        self.content.grid_columnconfigure(0, weight=1)

        # =====================================================
        # LOGO
        # =====================================================

        logo = ctk.CTkLabel(
            self.sidebar,
            text="NIMHUB",
            font=("Segoe UI", 30, "bold")
        )

        logo.pack(pady=(30, 5))

        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Developer Control Center",
            font=("Segoe UI", 14)
        )

        subtitle.pack(pady=(0, 30))

        # =====================================================
        # CREATE PAGES
        # =====================================================

        self.pages = {

            "dashboard": DashboardPage(self.content),

            "projects": ProjectsPage(self.content),

            "nimtask": NimtaskPage(self.content),

            "nimfolio": NimfolioPage(self.content),

            "statistics": StatisticsPage(self.content),

        

        }

        # =====================================================
        # NAVIGATION BUTTONS
        # =====================================================

        self.create_button(
            "🏠 Dashboard",
            "dashboard"
        )

        self.create_button(
            "📁 Projects",
            "projects"
        )

        self.create_button(
            "✅ NimTask",
            "nimtask"
        )

        self.create_button(
            "💼 Nimfolio",
            "nimfolio"
        )

        self.create_button(
            "📊 Statistics",
            "statistics"
        )

        self.create_button(
            "⚙ Settings",
            "settings"
        )

        exit_btn = ctk.CTkButton(

            self.sidebar,

            text="🚪 Exit",

            height=45,

            fg_color="firebrick",

            hover_color="#8B0000",

            command=self.destroy

        )

        exit_btn.pack(

            side="bottom",

            fill="x",

            padx=15,

            pady=20

        )

        # =====================================================
        # START PAGE
        # =====================================================

        self.show_page("dashboard")

    # =========================================================
    # CREATE SIDEBAR BUTTON
    # =========================================================

    def create_button(self, text, page):

        button = ctk.CTkButton(

            self.sidebar,

            text=text,

            height=45,

            command=lambda: self.show_page(page)

        )

        button.pack(

            fill="x",

            padx=15,

            pady=5

        )

    # =========================================================
    # SHOW PAGE
    # =========================================================

    def show_page(self, page_name):

        for page in self.pages.values():

            page.grid_forget()

        page = self.pages[page_name]

        page.grid(

            row=0,

            column=0,

            sticky="nsew"

        )

        # Refresh page automatically

        if hasattr(page, "refresh_statistics"):
            page.refresh_statistics()

        if hasattr(page, "load_projects"):
            page.load_projects()

        if hasattr(page, "load_tasks"):
            page.load_tasks()

        if hasattr(page, "load_profile"):
            page.load_profile()

        if hasattr(page, "load_dashboard_stats"):
            page.load_dashboard_stats()


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app = NimHub()

    app.mainloop()