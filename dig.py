import tkinter as tk
from tkinter import font

def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + symbol)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


root = tk.Tk()
root.title("Fərqli Rəngli Kalkulyator")
root.geometry("400x600")
root.configure(bg='#2C3E50') 


display_font = font.Font(family="Arial", size=24, weight="bold")
display = tk.Entry(root, width=14, font=display_font, justify="right",
                   bg='#34495E', fg='#ECF0F1', bd=10, relief=tk.FLAT)
display.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=15)


button_colors = {
    'numbers': {'bg': '#3498DB', 'fg': 'white', 'active': '#2980B9'},       
    'operators': {'bg': '#E74C3C', 'fg': 'white', 'active': '#C0392B'},     
    'special': {'bg': '#1ABC9C', 'fg': 'white', 'active': '#16A085'},      
    'equals': {'bg': '#9B59B6', 'fg': 'white', 'active': '#8E44AD'}         
}


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, col) in buttons:
    if text.isdigit() or text == '.':
        color_set = button_colors['numbers']
    elif text in '+-*/':
        color_set = button_colors['operators']
    elif text == '=':
        color_set = button_colors['equals']
    else:
        color_set = button_colors['special']
    
    btn = tk.Button(root, text=text, font=("Arial", 18, "bold"),
                    bg=color_set['bg'], fg=color_set['fg'],
                    activebackground=color_set['active'],
                    activeforeground='white',
                    bd=0, relief=tk.RAISED, padx=20, pady=20,
                    command=lambda t=text: button_click(t) if t != '=' else calculate())
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


clear_btn = tk.Button(root, text="C", font=("Arial", 18, "bold"),
                      bg='#E67E22', fg='white',
                      activebackground='#D35400',
                      bd=0, padx=20, pady=20, command=clear)
clear_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")


empty_btn = tk.Button(root, text="⌫", font=("Arial", 18, "bold"),
                      bg='#95A5A6', fg='white',
                      activebackground='#7F8C8D',
                      bd=0, padx=20, pady=20,
                      command=lambda: display.delete(len(display.get())-1, tk.END))
empty_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
