#Nothing important here, just a bit of tkinter crash course drafts 

import tkinter as tk

#interface for downloader to make software more user-friendly

root = tk.Tk()
root.geometry('500x320')
root.title('YTDownloader')

label = tk.Label(root, text="Hello World", font=("Arial",15))
label.pack(padx=10, pady=10)

textbox = tk.Text(root, font=("Arial", 10), height=3)
textbox.pack(pady=10, padx=30)

# myentry = tk.Entry(root)
# myentry.pack()

button = tk.Button(root, text='Download', font=('Arial', 9))
button.pack(pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
btn1 = tk.Button(buttonframe, text= 'btn 1')
btn1.grid(row=0, column=0, sticky='news')
btn2 = tk.Button(buttonframe, text= 'btn 2')
btn2.grid(row=0, column=1, sticky='news')
btn3 = tk.Button(buttonframe, text= 'btn 3')
btn3.grid(row=0, column=2, sticky='news')
buttonframe.pack(fill='x')


root.mainloop()
