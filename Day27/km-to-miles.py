from tkinter import *

# Create a window
window = Tk()
window.title("KM to Miles Converter")
# window.minsize(300, 150)
window.config(padx=20, pady=20)

km = Entry(width=10, font="Ariel 16")
km.insert(END, '0')
km.focus()
km.grid(column=1, row=0, padx=3, pady=3)

label1 = Label(text='KM', font=('Ariel', 14, 'normal'))
label1.grid(column=2, row=0, padx=3, pady=3)

label2 = Label(text='is equal to', font=('Ariel', 14, 'normal'))
label2.grid(column=0, row=1, padx=3, pady=3)

miles_label = Label(text=0, font=('Ariel', 14, 'normal'))
miles_label.grid(column=1, row=2, padx=3, pady=3)

label3 = Label(text='Miles', font=('Ariel', 14, 'normal'))
label3.grid(column=2, row=2, padx=3, pady=3)


def btn_clicked():
    km_dis = km.get()
    mile_dis = float(km_dis) * 0.62
    miles_label.config(text=mile_dis)


btn = Button(text='Calculate', font=('Ariel', 12, 'normal'), command=btn_clicked)
btn.grid(column=1, row=3)
btn.config(width=15, padx=3, pady=2)

window.mainloop()
