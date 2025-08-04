import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from graphics import GraficWifi
from scan import WiFiScanner

text1 = """
Tap to SCAN WIFI 
If you want to get
Wi-fi analytic graphic

"""

class FirstWindow:
    def __init__(self,width, heigh):
        self.win = tk.Tk()
        self.heigh = heigh
        self.width = width


    def command(self):
        self.win.destroy()
        wsc = WiFiScanner()

        gr = GraficWifi(wsc())
        solg = GrLastWindow(gr())
        solg.grphSolution()

    def winSolution(self):
        self.win.geometry(f"{self.heigh}x{self.width}")
        self.win.config(background="black")

        self.wtext = tk.Label(
            self.win,
            text=text1,
            background="black",
            fg="white"
        )
        self.wtext.pack()

        self.button = tk.Button(
            self.win,
            text="SCAN WIFI",
            activebackground="black",
            activeforeground="white",
            anchor="center",
            command=self.command
        )
        
        self.button.pack()
        self.win.mainloop()



class GrLastWindow:
    def __init__(self, graphic):
        self.grpf = graphic
        self.win = tk.Tk()
        

    def grphSolution(self):
        self.canvas = FigureCanvasTkAgg(self.grpf, master=self.win)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.win.mainloop()

        

fw = FirstWindow(230, 400)
fw.winSolution()
