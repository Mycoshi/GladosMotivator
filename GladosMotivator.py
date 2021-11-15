# Break study machine

import tkinter as tk 
import time
import math
import random
import glob
#playsound requires version 1.2.2 new version is broken?
from playsound import playsound
import os

class Core(tk.Tk):
    def __init__(self):
        super().__init__()

# （・ｱ　（・ｱ　（・ｱ　⊂（・）
# （＿） （＿） （＿）　 （＿つ
    
        self.work = True 


# （・ｱ　（・ｱ　（・ｱ　⊂（・）
# （＿） （＿） （＿）　 （＿つ


# UI
        self.title('GladOsMotivator')
        self.geometry('800x530')


        self.canvas =  tk.Canvas(width=800, height=850,)
        self.background =  tk.PhotoImage(file='baseimg.png')
        self.canvas.create_image(470, 270, image=self.background)
        self.canvas.grid(column=1, row=0)

        self.start_button =  tk.Button(text="Start", command=self.start_timer)
        self.start_button.place(x=25, y=380)

        self.reset_button =  tk.Button(text="Reset")
        self.reset_button.place(x=100, y=380)

        # trying to flip switches from red to green to indicate mode
        self.worktimentry = tk.Entry(bg='black',fg='white')
        self.worktimentry.insert(0,'1')
        self.worktimentry.place(x=200,y=380, width = 20)
        self.worktimelabel = tk.Label(text='work',fg='#000000')
        self.worktimelabel.place(x=225,y=380)


        self.breaktimentry = tk.Entry(bg='black',fg='white')
        self.breaktimentry.insert(0,'1')
        self.breaktimentry.place(x=200,y=400, width = 20)
        self.breaktimelabel = tk.Label(text='break')
        self.breaktimelabel.place(x=225,y=400)


        self.worktime = int(self.worktimentry.get())
        self.breaktime = int(self.breaktimentry.get())
#TODO  HERE
    # idk it switches but the label doesnt
    #this isnt right
    def rLightGreenLight(self):
        if self.work == True:
            self.lightlabel = tk.Label(text='work',bg='#2ad60f')
            self.worktimelabel.place(x=225,y=380)
            print('greenlight')
        else:
            self.lightlabel = tk.Label(text='work',bg='#d60f0f')
            self.worktimelabel.place(x=225,y=380)
            print('redlight')


        

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
        self.count_min = math.floor(count / 60)
        self.count_sec = count % 60
        Timer = tk.Label(text=f" {self.count_min} : {self.count_sec} ", fg="white", bg='black')
        Timer.place(x=150,y=380)
        if count > 0:
            print(count)
            self.after(1000, self.count_down, count - 1)
        elif count == 0:
            print('switch!')
            global work 
            if self.work == True:
                self.play_Line()
            else:
                self.play_Line()
            self.work = ~ self.work
            self.rLightGreenLight()
                
            self.start_timer()

    def start_timer(self):
        if self.work == True:
            worktime = int(self.worktimentry.get())
            self.count_down(worktime * 5)
        else:
            breaktime = int(self.breaktimentry.get())
            self.count_down(breaktime*5)




#BOOTSTRAP LOOP
if __name__ == "__main__":
    app = Core()
    #app withdraw removes second window which was root?
    app.mainloop()

        
        #TODO radio buttons for different break timers
        #radio buttons were switched out for customizable entry extra points if we create a lock but seems just aesthetic
        #TODO Noise packs and implentation
        #noise packs exist and are implented with playsound 1.2.2 next to create either a dict or a list of available packs and randomize
        #TODO resize buttons and windows
        # need bolds weights for labels and possible resizing of entry widgets, coloring can be done with hexidecimals 
        # I need to finalize backround image in an editor before placement 
        #im bad at graphic design some i waiting till the backend is up and functional before placement probably place this last
        #TODO add appenable todo list with crossout or checkbox 
