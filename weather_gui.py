import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
win = tk.Tk()
win.geometry('1200x768')
win.title('Real Time Weather Forecasting...')
win.iconbitmap('weather.ico')
# font variables
font_family = 'Roboto'
font_size_regular = 16
font_size_big = 30
text = tk.Text(win)
# label
heading = ttk.Label(win, text='WELCOME TO WEATHER FORECAST')
heading.configure(font=(font_family, font_size_big, 'bold'))
text.config(background='gray', fg='red')
heading.pack(side=tk.TOP)
# entry label
city_label = ttk.Label(win, text='Enter your city : ')
city_label.grid(row=0, column=0)
# entry box
city = tk.StringVar()
city_entry_box = ttk.Entry(win, width=30, textvariable=city)
city_entry_box.focus()
city_entry_box.grid(row=0, column=1)
# mainloop
win.mainloop()