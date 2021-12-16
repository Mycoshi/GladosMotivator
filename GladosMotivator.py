# Break study machine

import tkinter as tk 
import time
import math
import random
import glob
#playsound requires version 1.2.2 new version is broken?
from playsound import playsound
import os
from tkinter.ttk import Label, Style
from tkinter import Tk

# Play with this whe ready for async voicelines
#import asyncio




class Core(tk.Tk):
    def __init__(self):
        super().__init__()

# （・ｱ　（・ｱ　（・ｱ　⊂（・）
# （＿） （＿） （＿）　 （＿つ
    
        self.work = True 


# （・ｱ　（・ｱ　（・ｱ　⊂（・）
# （＿） （＿） （＿）　 （＿つ


# UI
#BUILD TIMER STANDING 0:00 LABEL
#font fixd with stupid easy font= must explore aperture fonts,
        self.title('GladOsMotivator')
        self.geometry('800x530')

        self.style = Style(self.master)
        self.style.configure("My.TLabel", font=('Arial', 25))

        self.canvas =  tk.Canvas(width=800, height=850,)
        self.background =  tk.PhotoImage(file='baseimg.png')
        self.canvas.create_image(470, 270, image=self.background)
        self.canvas.grid(column=1, row=0)

        self.start_button =  tk.Button(text="Start", command=self.start_timer)
        self.start_button.place(x=100, y=450)

        self.stop_button =  tk.Button(text="Stop", command=self.stop_timer)
        self.stop_button.place(x=175, y=450)

        # trying to flip switches from red to green to indicate mode
        self.worktimentry = tk.Entry(bg='black',fg='white')
        self.worktimentry.insert(0,'1')
        self.worktimentry.place(x=120,y=380, width = 20)
        self.worktimelabel = tk.Label(text='work',fg='#000000', font=('Helvatical bold',20))
        self.worktimelabel.place(x=120,y=280)


        #making signal light
        self.signallabel = tk.Label(text='I',bg='green', height=5, width=10, justify='center', relief='sunken')
        self.signallabel.place(x=100,y=300)
        self.signallabel2 = tk.Label(text='O',bg='red', height=5, width=10, justify='center', relief='raised')
        self.signallabel2.place(x=175,y=300)


        self.breaktimentry = tk.Entry(bg='black',fg='white')
        self.breaktimentry.insert(0,'1')
        self.breaktimentry.place(x=205,y=380, width = 20)
        self.breaktimelabel = tk.Label(text='break')
        self.breaktimelabel.place(x=200,y=280)


        self.worktime = int(self.worktimentry.get())
        self.breaktime = int(self.breaktimentry.get())


        #button color switch working 
    def rLightGreenLight(self):
        if self.work == True:
            self.signallabel.config (relief='sunken')
            self.signallabel2.config (relief='raised')
            print("greenlight")
        else:
            self.signallabel.config (relief='raised')
            self.signallabel2.config (relief='sunken')
            print("redlight")


        

# 1- here a combination of os.path.dirname(os.path.abspath(__file__)) & Glob work to retrieve the place we are in and then cycle down into the folders we have knowledge of

#fixed praise glob
    def play_Line(self):
        path = os.path.dirname(os.path.abspath(__file__))
        Break_glines = glob.glob(path + "/sounds/Break_time/*")
        Work_glines = glob.glob(path + "/sounds/Work_time/*")
        if self.work == True:
            playsound(Break_glines[random.randint(0,23)])
        else:
            playsound(Work_glines[random.randint(0,23)])


#TODO CHECK IF TIMER BUG STILL EXISTS 
    def count_down(self, count):
        if self.running == True:
            self.count_min = math.floor(count / 60)
            self.count_sec = count % 60
            Timer = tk.Label(text=f" {self.count_min} : {self.count_sec} ", fg="white", bg='#4b5d69', font=('Helvatical bold',20))
            Timer.place(x=150,y=50)
            if count > 0:
                print(count)
                self.after(1000, self.count_down, count - 1)
            elif count == 0:
                print('switch!')
                global work 
                self.play_Line()
                self.work = ~ self.work
                self.rLightGreenLight()
                self.start_timer()
        else:
            return

    def start_timer(self):
        self.running = True
        if self.work == True:
            worktime = int(self.worktimentry.get())
            self.count_down(worktime * 5)
        else:
            breaktime = int(self.breaktimentry.get())
            self.count_down(breaktime*5)
    def stop_timer(self):
        self.running = False
        




#BOOTSTRAP LOOP
if __name__ == "__main__":
    app = Core()
    #app withdraw removes second window which was root?
    app.mainloop()

        
     #noise packs exist and are implented with playsound 1.2.2 next to create either a dict or a list of available packs and randomize
    # need bolds weights for labels and possible resizing of entry widgets, coloring can be done with hexidecimals 
    #TODO add appenable todo list with crossout or checkbox 
    # Timer functional but start button does not start at previous position 