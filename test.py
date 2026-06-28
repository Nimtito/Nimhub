import customtkinter as ctk

app = ctk.CTk()
app.title("NimHub Test")
app.geometry("400x200")

label = ctk.CTkLabel(app, text="CustomTkinter is working!")
label.pack(pady=40)

app.mainloop()