from tkinter import Tk, Button, Label, Entry, Listbox, Toplevel
from tkinter.font import Font

# Define constants
BG = "#2D2D2D"
FG = "white"

def load_expenses():
    expenses.delete(0, "end")
    with open("expenses.txt", "r", encoding="utf-8") as file:
        for line in file:
            expenses.insert("end", line.strip())

def load_balance():
    amount = open("./balance.txt", "r").read()
    title_label["text"] = f"Your Balance: {float(amount):.2f}€"

    if float(amount) <= 0: title_label["fg"] = "red"
    else: title_label["fg"] = FG

def add_expense(amount: float, desti: str):
    if amount == "" or desti == "": return

    with open("./expenses.txt", "a", encoding="utf-8") as file:
        file.write(f"{amount}€ | {desti}\n")
    load_expenses()

    add_income(-float(amount))


def get_expense_toadd():
    window = Toplevel(app)
    window.geometry("300x200")
    window.configure(bg=BG)
    window.title("Add Expense")

    title_label = Label(window, text="Add Expense", bg=BG, fg=FG, font=title_font)
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    amount_entry = Entry(window, bg=BG, fg=FG, font=label_font)
    amount_entry.place(relx=0.5, rely=0.3, anchor="center")

    desti_entry = Entry(window, bg=BG, fg=FG, font=label_font)
    desti_entry.place(relx=0.5, rely=0.5, anchor="center")

    add_button = Button(window, text="Add", bg=BG, fg=FG, font=label_font, command=lambda: add_expense(amount_entry.get(), desti_entry.get()))
    add_button.place(relx=0.5, rely=0.7, anchor="center")    


def add_income(amount: float):
    newamount = float(title_label["text"].split(" ")[2][:-1]) + float(amount)
    open("./balance.txt", "w").write(str(newamount))

    load_balance()

def get_income_toadd():
    window = Toplevel(app)
    window.geometry("300x200")
    window.configure(bg=BG)
    window.title("Add Income")

    title_label = Label(window, text="Add Income", bg=BG, fg=FG, font=title_font)
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    amount_entry = Entry(window, bg=BG, fg=FG, font=label_font)
    amount_entry.place(relx=0.5, rely=0.3, anchor="center")

    add_button = Button(window, text="Add", bg=BG, fg=FG, font=label_font, command=lambda: add_income(amount_entry.get()))
    add_button.place(relx=0.5, rely=0.5, anchor="center")

# Create the window
app = Tk()
app.geometry("500x500")
app.configure(bg=BG)
app.title("Expense Tracker")

# Create the fonts
title_font = Font(family="Arial", size=26)
label_font = Font(family="Arial", size=15)

# Create the widgets
title_label = Label(app, text="Your Balance: 470.01€", bg=BG, fg=FG, font=title_font)
title_label.place(relx=0.5, rely=0.1, anchor="center")

expense_label = Label(app, text="Expenses", bg=BG, fg=FG, font=label_font)
expense_label.place(relx=0.7, rely=0.35, anchor="center")

expenses = Listbox(app, bg=BG, fg=FG, font=label_font, height=8, width=25)
expenses.place(relx=0.7, rely=0.6, anchor="center")

add_expense_btn = Button(app, text="Add Expense", bg=BG, fg=FG, font=label_font, command=get_expense_toadd)
add_expense_btn.place(relx=0.2, rely=0.45, anchor="center")

add_income_btn = Button(app, text="Add Income", bg=BG, fg=FG, font=label_font, command=get_income_toadd)
add_income_btn.place(relx=0.2, rely=0.55, anchor="center")


# Load the data
load_expenses()
load_balance()

app.mainloop()