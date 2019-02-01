import tkinter as tk
import tkinter as ttk
import webbrowser

app=tk.Tk()

app.title('App')

search_label=ttk.Label(app, text='Search:')
search_label.grid(row=0, column=0)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=0, column=1)

app.mainloop()