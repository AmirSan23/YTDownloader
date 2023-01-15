import tkinter as tk
from tkinter import filedialog
import main

class DownloaderGUI:

    def __init__(self):
        #initial settings of an app window
        self.root = tk.Tk()
        self.root.geometry('500x300')

        #App lable/title
        self.lable = tk.Label(self.root, text="Downloader Test Interface", font=("Arial", 15))
        self.lable.pack(padx=10, pady=10)

        #input field
        self.textbox = tk.Text(self.root, height=1, font=("Arial", 10))
        self.textbox.pack(padx=30, pady=10)

        #button collection
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        #Get audio only button
        self.button1 = tk.Button(self.buttonframe, text="Get audio only", font=("Arial",10),
                                 command=self.download_audio_only)
        #self.button.pack(padx=10, pady=10)
        self.button1.grid(row=0, column=0,
                          sticky="news",
                          padx=5,
                          pady=5)

        #Get a playlist (Video format)
        self.button2 = tk.Button(self.buttonframe, text="Get a playlist (Video format)", font=("Arial",10))
        self.button2.grid(row=1, column=0,
                          sticky="news",
                          padx=5,
                          pady=5)

        #Download video button
        self.button3 = tk.Button(self.buttonframe, text="Download video", font=("Arial",10))
        self.button3.grid(row=0,
                          column=1,
                          sticky="news",
                          padx=5,
                          pady=5)

        #Get Playlist(Audio button)
        self.button4 = tk.Button(self.buttonframe, text="Get a playlist (Audio format)", font=("Arial",10))
        self.button4.grid(row=1,
                          column=1,
                          sticky="news",
                          padx=5,
                          pady=5)

        self.buttonframe.pack(fill='y', pady = 20)
        self.root.mainloop()

    def download_audio_only(self):
        outputpath = filedialog.askdirectory() #ask user for path where they want their file to be stored
        main.get_audio_only(self.textbox.get('1.0', tk.END), outputpath)

DownloaderGUI()