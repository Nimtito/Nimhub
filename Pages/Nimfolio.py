"""
=========================================================
NIMHUB
pages/nimfolio.py
=========================================================
"""

import customtkinter as ctk
from tkinter import messagebox

from database.portfolio import (
    save_portfolio,
    load_portfolio,
    update_portfolio,
    clear_portfolio
)


class NimfolioPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(fg_color="#1E1E1E")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

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
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

        self.header.grid_propagate(False)

        self.title_label = ctk.CTkLabel(
            self.header,
            text="Nimfolio",
            font=("Segoe UI", 30, "bold")
        )

        self.title_label.pack(
            anchor="w",
            padx=20,
            pady=(15, 0)
        )

        self.subtitle_label = ctk.CTkLabel(
            self.header,
            text="Professional Portfolio Manager",
            font=("Segoe UI", 15)
        )

        self.subtitle_label.pack(
            anchor="w",
            padx=20
        )

        # =====================================================
        # LEFT PANEL
        # =====================================================

        self.left_frame = ctk.CTkFrame(
            self,
            width=430,
            fg_color="#2B2B2B",
            corner_radius=15
        )

        self.left_frame.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=(20, 10),
            pady=(10, 20)
        )

        self.left_frame.grid_propagate(False)

        ctk.CTkLabel(
            self.left_frame,
            text="Portfolio Information",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(20, 15)
        )

        # =====================================================
        # FULL NAME
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Full Name",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.name_entry = ctk.CTkEntry(
            self.left_frame,
            height=40
        )

        self.name_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # PROFESSION
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Profession",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.profession_entry = ctk.CTkEntry(
            self.left_frame,
            height=40
        )

        self.profession_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # LOCATION
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Location",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.location_entry = ctk.CTkEntry(
            self.left_frame,
            height=40
        )

        self.location_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # PHONE
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Phone",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.phone_entry = ctk.CTkEntry(
            self.left_frame,
            height=40
        )

        self.phone_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # EMAIL
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Email",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.email_entry = ctk.CTkEntry(
            self.left_frame,
            height=40
        )

        self.email_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # GITHUB
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="GitHub",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.github_entry = ctk.CTkEntry(
            self.left_frame,
            height=40,
            placeholder_text="https://github.com/username"
        )

        self.github_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # LINKEDIN
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="LinkedIn",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.linkedin_entry = ctk.CTkEntry(
            self.left_frame,
            height=40,
            placeholder_text="https://linkedin.com/in/username"
        )

        self.linkedin_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # WEBSITE
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Website",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.website_entry = ctk.CTkEntry(
            self.left_frame,
            height=40,
            placeholder_text="https://yourwebsite.com"
        )

        self.website_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # =====================================================
        # ABOUT
        # =====================================================

        ctk.CTkLabel(
            self.left_frame,
            text="About",
            anchor="w"
        ).pack(
            fill="x",
            padx=20
        )

        self.about_box = ctk.CTkTextbox(
            self.left_frame,
            height=180
        )

        self.about_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 20)
        )
                # =====================================================
        # RIGHT PANEL
        # =====================================================

        self.right_frame = ctk.CTkFrame(
            self,
            fg_color="#2B2B2B",
            corner_radius=15
        )

        self.right_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(10, 20)
        )

        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=1)

        # =====================================================
        # PREVIEW TITLE
        # =====================================================

        self.preview_title = ctk.CTkLabel(
            self.right_frame,
            text="Portfolio Preview",
            font=("Segoe UI", 24, "bold")
        )

        self.preview_title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=25,
            pady=(20, 10)
        )

        # =====================================================
        # PREVIEW BOX
        # =====================================================

        self.preview = ctk.CTkTextbox(
            self.right_frame,
            font=("Consolas", 15),
            wrap="word"
        )

        self.preview.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=25,
            pady=(0, 20)
        )

        self.preview.configure(state="disabled")

        # =====================================================
        # BUTTON BAR
        # =====================================================

        self.button_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color="transparent"
        )

        self.button_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 20)
        )

        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        # =====================================================
        # SAVE BUTTON
        # =====================================================

        self.save_button = ctk.CTkButton(
            self.button_frame,
            text="💾 Save",
            height=42,
            command=self.save_profile
        )

        self.save_button.grid(
            row=0,
            column=0,
            padx=(0, 10),
            pady=5,
            sticky="ew"
        )

        # =====================================================
        # UPDATE BUTTON
        # =====================================================

        self.update_button = ctk.CTkButton(
            self.button_frame,
            text="✏ Update",
            height=42,
            command=self.update_profile
        )

        self.update_button.grid(
            row=0,
            column=1,
            padx=(10, 0),
            pady=5,
            sticky="ew"
        )

        # =====================================================
        # SECOND BUTTON ROW
        # =====================================================

        self.button_frame2 = ctk.CTkFrame(
            self.right_frame,
            fg_color="transparent"
        )

        self.button_frame2.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 20)
        )

        self.button_frame2.grid_columnconfigure((0, 1), weight=1)

        # =====================================================
        # CLEAR BUTTON
        # =====================================================

        self.clear_button = ctk.CTkButton(
            self.button_frame2,
            text="🧹 Clear",
            height=42,
            command=self.clear_form
        )

        self.clear_button.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="ew"
        )

        # =====================================================
        # DELETE BUTTON
        # =====================================================

        self.delete_button = ctk.CTkButton(
            self.button_frame2,
            text="🗑 Delete",
            height=42,
            fg_color="firebrick",
            hover_color="#8B0000",
            command=self.delete_profile
        )

        self.delete_button.grid(
            row=0,
            column=1,
            padx=(10, 0),
            sticky="ew"
        )

        # =====================================================
        # LOAD SAVED PROFILE
        # =====================================================

        self.load_profile()

            # =====================================================
    # LOAD PROFILE
    # =====================================================

    def load_profile(self):

        profile = load_portfolio()

        self.clear_form(clear_preview=False)

        self.preview.configure(state="normal")
        self.preview.delete("1.0", "end")

        if profile is None:

            self.preview.insert(
                "end",
                "No portfolio found.\n\nCreate your portfolio to see the preview."
            )

            self.preview.configure(state="disabled")
            return

        (
            profile_id,
            full_name,
            profession,
            location,
            about,
            phone,
            email,
            github,
            linkedin,
            website
        ) = profile

        self.name_entry.insert(0, full_name)
        self.profession_entry.insert(0, profession)
        self.location_entry.insert(0, location)
        self.phone_entry.insert(0, phone)
        self.email_entry.insert(0, email)
        self.github_entry.insert(0, github)
        self.linkedin_entry.insert(0, linkedin)
        self.website_entry.insert(0, website)
        self.about_box.insert("1.0", about)

        preview = f"""
============================================================

{full_name}

{profession}

============================================================

📍 Location
{location}

📞 Phone
{phone}

📧 Email
{email}

💻 GitHub
{github}

🔗 LinkedIn
{linkedin}

🌐 Website
{website}

============================================================

ABOUT

{about}

============================================================
"""

        self.preview.insert("1.0", preview)
        self.preview.configure(state="disabled")

    # =====================================================
    # SAVE PROFILE
    # =====================================================

    def save_profile(self):

        save_portfolio(
            self.name_entry.get().strip(),
            self.profession_entry.get().strip(),
            self.location_entry.get().strip(),
            self.about_box.get("1.0", "end").strip(),
            self.phone_entry.get().strip(),
            self.email_entry.get().strip(),
            self.github_entry.get().strip(),
            self.linkedin_entry.get().strip(),
            self.website_entry.get().strip()
        )

        messagebox.showinfo(
            "Success",
            "Portfolio saved successfully."
        )

        self.load_profile()

    # =====================================================
    # UPDATE PROFILE
    # =====================================================

    def update_profile(self):

        update_portfolio(
            self.name_entry.get().strip(),
            self.profession_entry.get().strip(),
            self.location_entry.get().strip(),
            self.about_box.get("1.0", "end").strip(),
            self.phone_entry.get().strip(),
            self.email_entry.get().strip(),
            self.github_entry.get().strip(),
            self.linkedin_entry.get().strip(),
            self.website_entry.get().strip()
        )

        messagebox.showinfo(
            "Updated",
            "Portfolio updated successfully."
        )

        self.load_profile()

    # =====================================================
    # DELETE PROFILE
    # =====================================================

    def delete_profile(self):

        answer = messagebox.askyesno(
            "Delete Portfolio",
            "Are you sure you want to delete your portfolio?"
        )

        if not answer:
            return

        clear_portfolio()

        self.clear_form()

        messagebox.showinfo(
            "Deleted",
            "Portfolio deleted successfully."
        )

    # =====================================================
    # CLEAR FORM
    # =====================================================

    def clear_form(self, clear_preview=True):

        self.name_entry.delete(0, "end")
        self.profession_entry.delete(0, "end")
        self.location_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.github_entry.delete(0, "end")
        self.linkedin_entry.delete(0, "end")
        self.website_entry.delete(0, "end")

        self.about_box.delete("1.0", "end")

        if clear_preview:

            self.preview.configure(state="normal")

            self.preview.delete("1.0", "end")

            self.preview.insert(
                "1.0",
                "Portfolio preview will appear here."
            )

            self.preview.configure(state="disabled")