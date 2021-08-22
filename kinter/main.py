import tkinter


def button_clicked():
    message = mile_entry.get()
    kilo = float(message) * 1.6
    kilo_result["text"] = kilo


window = tkinter.Tk()
window.title("Genshin Impact")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)
equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)
mile_entry = tkinter.Entry(width=10)
mile_entry.grid(column=1, row=0)
kilo_result = tkinter.Label(text="0")
kilo_result.grid(column=1, row=2)
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
kilo_label = tkinter.Label(text="KM")
kilo_label.grid(column=2, row=2)
calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=3)

window.mainloop()
