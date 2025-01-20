import tkinter as tk

def button_click(number):
    current_text = display_var.get()
    new_text = current_text + str(number)
    display_var.set(new_text)

def enter_click():
    print("Eingabe: " + display_var.get())
    display_var.set("")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Tastenanzeige")
root.geometry("400x500")

# Abstand oben hinzufügen
top_space = tk.Frame(root, height=100)
top_space.pack()

# Variable für die Anzeigeleiste
display_var = tk.StringVar()

# Rahmen für die Anzeigeleiste und die Enter-Taste erstellen
top_frame = tk.Frame(root)
top_frame.pack()

# Anzeigeleiste erstellen
display_label = tk.Label(top_frame, textvariable=display_var, font=("Helvetica", 16), width=15)
display_label.pack(side=tk.LEFT)

# Rahmen für die Enter-Taste erstellen
enter_frame = tk.Frame(top_frame)
enter_frame.pack(side=tk.RIGHT)

# Enter-Taste erstellen
enter_button = tk.Button(enter_frame, text="Enter", command=enter_click, font=("Helvetica", 16))
enter_button.pack()

# Rahmen für die Tasten erstellen
button_frame = tk.Frame(root)
button_frame.pack()

# Tasten erstellen
button1 = tk.Button(button_frame, text="1", command=lambda: button_click(1), font=("Helvetica", 22), width=5, height=2)
button1.grid(row=0, column=0)

button2 = tk.Button(button_frame, text="2", command=lambda: button_click(2), font=("Helvetica", 22), width=5, height=2)
button2.grid(row=0, column=1)

button3 = tk.Button(button_frame, text="3", command=lambda: button_click(3), font=("Helvetica", 22), width=5, height=2)
button3.grid(row=0, column=2)

button4 = tk.Button(button_frame, text="4", command=lambda: button_click(4), font=("Helvetica", 22), width=5, height=2)
button4.grid(row=1, column=0)

button5 = tk.Button(button_frame, text="5", command=lambda: button_click(5), font=("Helvetica", 22), width=5, height=2)
button5.grid(row=1, column=1)

button6 = tk.Button(button_frame, text="6", command=lambda: button_click(6), font=("Helvetica", 22), width=5, height=2)
button6.grid(row=1, column=2)

button7 = tk.Button(button_frame, text="7", command=lambda: button_click(7), font=("Helvetica", 22), width=5, height=2)
button7.grid(row=2, column=0)

button8 = tk.Button(button_frame, text="8", command=lambda: button_click(8), font=("Helvetica", 22), width=5, height=2)
button8.grid(row=2, column=1)

button9 = tk.Button(button_frame, text="9", command=lambda: button_click(9), font=("Helvetica", 22), width=5, height=2)
button9.grid(row=2, column=2)

# Operator-Tasten erstellen
plus_button = tk.Button(button_frame, text="+", command=lambda: button_click('+'), font=("Helvetica", 20), width=5, height=1)
plus_button.grid(row=0, column=3)

minus_button = tk.Button(button_frame, text="-", command=lambda: button_click('-'), font=("Helvetica", 20), width=5, height=1)
minus_button.grid(row=1, column=3)

multiply_button = tk.Button(button_frame, text="*", command=lambda: button_click('*'), font=("Helvetica", 20), width=5, height=1)
multiply_button.grid(row=2, column=3)

divide_button = tk.Button(button_frame, text="/", command=lambda: button_click('/'), font=("Helvetica", 20), width=5, height=1)
divide_button.grid(row=3, column=3)

# Hauptereignisschleife starten
root.mainloop()
