from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Currency convertor')
root.geometry("280x500")
root.config(bg="white")


import requests


my_notebook = ttk.Notebook(root)
my_notebook.place(x=20, y=20)

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']

currency_frame = Frame(my_notebook, width=480, height=480, bg="grey")
convertor_frame = Frame(my_notebook, width=480, height=480, bg="grey")

currency_frame.pack(fill="both", expand=1)
convertor_frame.pack(fill="both", expand=1)

my_notebook.add(currency_frame, text='currencies')
my_notebook.add(convertor_frame, text='conversions')

home = LabelFrame(currency_frame, text="Conversion from USD", bg="grey")
home.pack(pady=20)

home_entry = Entry(home, font=(24))
home_entry.pack(padx=10, pady=10)

conversion = LabelFrame(currency_frame, text='conversion currency', bg="grey")
conversion.pack(pady=20)

convert = Label(conversion, text="Convert To:", font=("Arial", 20))
convert.config(bg="grey")
convert.pack()

convert_list = Listbox(conversion, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.pack()

convert_label = Label(convertor_frame, text="Converted to: ", font=("Arial", 20))
convert_label.config(bg="grey")
convert_label.pack()


def convert_curr():
    try:
        num = float(home_entry.get())
        print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
        ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
        convert_label['text'] = ans
        my_notebook.select(1)
    except ValueError:
        messagebox.showerror("error", "PLease enter a number")
    except requests.exceptions.ConnectionError as x:
        messagebox.showerror("error", "No internet connection")




convert_btn = Button(currency_frame, command=convert_curr, text="Convert", font=("Arial", 20), width=10)
convert_btn.config(bg="grey")
convert_btn.pack()


root.mainloop()
