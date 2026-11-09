import customtkinter as a

a.set_appearance_mode("dark")

app = a.CTk()
app.title("Калькулятор")
app.geometry("500x500")

screen = a.CTkEntry(app, justify="right", font=("Arial", 32))
screen.pack(fill="x", padx=10, pady=10)

app.mainloop()