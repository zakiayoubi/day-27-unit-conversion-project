from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=250)

entry = Entry(width=15)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to ")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def calc_function():
    km = round(1.6 * int(entry.get()), 2)
    result_label.config(text=km)


calc_button = Button(text="Calculate", command=calc_function)
calc_button.grid(column=1, row=2)






window.mainloop()





