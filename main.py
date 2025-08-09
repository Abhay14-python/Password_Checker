import tkinter as tk
# from tkinter import ttk 
import ttkbootstrap as ttk
def check():
    if string_var.get() == string_var1.get() == string_var2.get():
        fin_label_text.set("The Password matches ✅✅")
        fin_label.config(foreground="lightgreen") 
    else :
        fin_label_text.set("The Password DOSEN'T match ❌❌")       
        fin_label.config(foreground="red")
    entry["state"] = "disabled"
    entry1["state"] = "disabled"
    entry2["state"] = "disabled"
    button["state"] = "disabled"

def re_try():
    entry["state"] = "normal"
    entry1["state"] = "normal"
    entry2["state"] = "normal"
    button["state"] = "normal"
    fin_label_text.set("")
    fin_label.config(foreground="white")

# window
window = ttk.Window(themename = "superhero")
window.title("Password Checker")
window.geometry("400x300")

# widiget
label = ttk.Label(master = window , text = "Password checker" , font=("Arial", 16, "bold"))
label.pack(pady = 5)

label1 = ttk.Label(master = window , text = "Helps you remember your passwords!")
label1.pack(pady = 5)

string_var = tk.StringVar()
entry = ttk.Entry(master = window , textvariable = string_var , show="•")
entry.pack(pady = 5)

string_var1 = tk.StringVar()
entry1 = ttk.Entry(master = window , textvariable = string_var1 , show="•")
entry1.pack(pady = 5)

string_var2 = tk.StringVar()
entry2 = ttk.Entry(master = window , textvariable = string_var2 , show="•")
entry2.pack(pady = 5)

button = ttk.Button(master = window , text = "Check" , command = check)
button.pack(pady = 5)


fin_label_text = tk.StringVar()
fin_label = ttk.Label(master = window , text = "" , textvariable = fin_label_text)
fin_label.pack(pady = 10)

again = ttk.Button(master = window , text = "Wanna Do Again?" , command = re_try)
again.pack()

window.mainloop()