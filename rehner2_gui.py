import tkinter as tk

def on_button_click(button_text):
    current_text = display_var.get()
    new_text = current_text + button_text
    display_var.set(new_text)

def on_operator_click(operator, button):
    current_text = display_var.get()
    new_text = current_text + operator
    display_var.set(new_text)
    reset_button_colors()
    button.config(bg="blue")

def on_enter_click():
    expression = display_var.get()
    try:
        result = eval(expression)
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")
    reset_button_colors()

def on_clear_click():
    display_var.set('')
    reset_button_colors()

def on_button_press(event):
    event.widget.config(bg="lightblue")

def on_button_release(event):
    event.widget.config(bg="SystemButtonFace")

def reset_button_colors():
    for button in buttons_list:
        if button['text'] in operators:
            button.config(bg="lightgrey")
        else:
            button.config(bg="SystemButtonFace")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# StringVar für den Anzeigetext erstellen
display_var = tk.StringVar()

# Anzeige-Entry erstellen
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Tasten definieren
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    'C', '0'
]

operators = ['+', '-', '*', '/']

# Liste zum Speichern der Tasten
buttons_list = []

# Tasten erstellen und im Grid platzieren
row_val = 1
col_val = 0
for button_text in buttons:
    if button_text == 'C':
        btn = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 18), relief="flat", command=on_clear_click)
    else:
        btn = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 18), relief="flat", command=lambda b=button_text: on_button_click(b))
    
    btn.grid(row=row_val, column=col_val)
    
    # Ereignisse binden
    btn.bind("<ButtonPress>", on_button_press)
    btn.bind("<ButtonRelease>", on_button_release)
    
    buttons_list.append(btn)
    
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Operatoren-Tasten erstellen und rechts platzieren
for i, operator in enumerate(operators):
    btn = tk.Button(root, text=operator, width=5, height=2, font=("Arial", 18), bg="lightgrey", relief="flat", command=lambda b=operator, btn=btn: on_operator_click(b, btn))
    
    btn.grid(row=i+1, column=4)
    
    # Ereignisse binden
    btn.bind("<ButtonPress>", on_button_press)
    btn.bind("<ButtonRelease>", on_button_release)
    
    buttons_list.append(btn)

# '=' Taste erstellen und rechts neben der Anzeige platzieren
enter_btn = tk.Button(root, text='=', width=5, height=2, font=("Arial", 18), relief="flat", command=on_enter_click)
enter_btn.grid(row=0, column=4)

# Hauptschleife starten
root.mainloop()
