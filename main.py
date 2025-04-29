from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.insert(END, string=0)
miles_input.focus()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)


def miles_to_km():
    answer = float(miles_input.get()) * 1.609
    kilometer_result_label["text"] = f"{answer:.2f}"


calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

window.mainloop()
