import tkinter as tk
from tkinter import ttk
import numpy as np

#function to convert from degrees celsius to kelvin
def convert(C):
    K = C + 273.15
    return K

#function to convert to the desired time. Comes from Newton's Law of Cooling assuming constant environmental temperature
def Newton(t0, t1, ambient, desired):
    B = t0 - ambient
    k = np.log((t1 - ambient) / (t0 - ambient))
    time = (1 / k) * np.log((desired - ambient) / (t0 - ambient))
    return f"{time:.2f}"

#code for graphical user interface using tkinter
root = tk.Tk()

#set name on window and default size
root.title("Newton's Law of Cooling")
root.geometry("700x400")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

#function to take inputs and either give answer or an error message
def on_click():
    try:
        surrounding = float(e1.get())
        starting = float(e2.get())
        minute = float(e3.get())
        wanted = float(e4.get())

        t0 = convert(starting)
        t1 = convert(minute)
        ambient = convert(surrounding)
        desired = convert(wanted)

        answer.config(text=f"It looks like you'll have to wait {Newton(t0, t1, ambient, desired)} minutes. Enjoy!",
                      style="Normal.TLabel")
    except ValueError:
        answer.config(text="Whoopsies! Looks like at least one of your inputs wasn't a number. Please try again.",
                      style="Error.TLabel")

#text describing what the app does
label1 = ttk.Label(frame, text="Hello! I am Newty, your Newtonian coffee (or tea) guide!").grid(row=0)
label2 = ttk.Label(frame, text="By telling me the temperature of your cup of coffee at two times and the ambient temperature,").grid(row=1, pady=(10, 0))
label3 = ttk.Label(frame, text="I can tell you how long to wait until your coffee reaches your desired temperature!").grid(row=2, pady=(0, 10))

#text and entry boxes for user input
ttk.Label(frame, text="Ambient temperature (in Celsius)").grid(row=3)
ttk.Label(frame, text="Starting temperature (in Celsius)").grid(row=4)
ttk.Label(frame, text="The temperature after 1 minute (in Celsius)").grid(row=5)
ttk.Label(frame,text="Desired temperature (in Celsius). Most people like their temperature between 49°C and 60°C").grid(row=6)
e1 = ttk.Entry(frame)
e2 = ttk.Entry(frame)
e3 = ttk.Entry(frame)
e4 = ttk.Entry(frame)
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)
e3.grid(row=5, column=1)
e4.grid(row=6, column=1)

#button
btn = ttk.Button(frame, text="Calculate!", command=on_click)
btn.grid(row=7, column=0, padx=10, pady=10)

#error message and answer text both use the same box
#this is to convert the error text to red and back to black for a correct user input
style = ttk.Style()
style.configure("Error.TLabel", foreground="red")
style.configure("Normal.TLabel", foreground="black")

#text box for answer or error message
answer = ttk.Label(frame, text="")
answer.grid(row=8)

root.mainloop()
