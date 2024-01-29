import tkinter

def calculate():
    km = float(input.get()) * 1.609
    kilo['text'] = str(km)

window = tkinter.Tk()
window.title("miles to kilometers conveter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

# Label
is_equal = tkinter.Label(text="is equal to")
is_equal.grid(column=0, row=1)

kilo = tkinter.Label(text="0")
kilo.grid(column=1, row=1)

km = tkinter.Label(text="km")
km.grid(column=2, row=1)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)


# Entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

# button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()