import customtkinter as ctk

# Import Pages
from pages.Dashboard import DashboardPage
from pages.Nimtask import NimtaskPage
from pages.Nimfolio import NimfolioPage
from pages.stats import statsPage


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class NimHubApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("NimHub - Developer Control Center")
        self.geometry("1200x700")

        # ---------------- Sidebar ----------------
        self.sidebar = ctk.CTkFrame(self, width=220)
        self.sidebar.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            self.sidebar,
            text="NIMHUB",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

        ctk.CTkButton(
            self.sidebar,
            text="🏠 Dashboard",
            command=lambda: self.show_page("dashboard")
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="📋 NimTask",
            command=lambda: self.show_page("nimtask")
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="💼 Nimfolio",
            command=lambda: self.show_page("nimfolio")
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="📊 Stats",
            command=lambda: self.show_page("stats")
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="Exit",
            fg_color="red",
            command=self.destroy
        ).pack(side="bottom", fill="x", padx=20, pady=20)

        # ---------------- Content Area ----------------
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="right", fill="both", expand=True)

        self.pages = {
            "dashboard": DashboardPage(self.container),
            "nimtask": NimtaskPage(self.container),
            "nimfolio": NimfolioPage(self.container),
            "stats": statsPage(self.container)
        }

        self.show_page("dashboard")

    def show_page(self, page_name):

        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(fill="both", expand=True)


if __name__ == "__main__":
    app = NimHubApp()
    app.mainloop()