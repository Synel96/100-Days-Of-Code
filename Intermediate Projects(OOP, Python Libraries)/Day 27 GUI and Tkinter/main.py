import tkinter
from calculator import Calculator

window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300,height=120)
window.config(padx=50,pady=20)


input =tkinter.Entry(width=5)
input.grid(column=2, row=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=1)

result_label = miles_label = tkinter.Label(text=f"is equal to ")
result_label.grid(column=1, row=2)

result_label_1 = miles_label = tkinter.Label(text="0")
result_label_1.grid(column=2, row=2)

km_label =tkinter.Label(text="Km")
km_label.grid(column=3, row=2)

calculator = Calculator(input,result_label_1)

button = tkinter.Button(text="Calculate", command=calculator.convert)
button.grid(column=2,row=3)




window.mainloop()