# Break study machine

import tkinter
import time
import math
import pydub
from playsound import playsound
window = tkinter.Tk()
window.title('GladOsMotivator')
window.geometry('800x500')
work = True







def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    Timer = tkinter.Label(text=f" {count_min} : {count_sec} ", fg="white", bg='black')
    Timer.place(x=150,y=380)
    if count > 0:
        print(count)
        window.after(1000, count_down, count - 1)
    elif count == 0:
        print(count)
        global work 
        if work == True:
            playsound('hey-moron.mp3')
        else:
            playsound('hey-moron.mp3')    
        work = ~ work
        
        start_timer()

def start_timer():
    if work == True:
        worktime = int(worktimentry.get())
        count_down(worktime * 5)
    else:
        breaktime = int(breaktimentry.get())
        count_down(breaktime*5)




#background Placement
canvas =  tkinter.Canvas(width=800, height=850, )
background =  tkinter.PhotoImage(file='baseimg.png')
canvas.create_image(470, 270, image=background)
canvas.grid(column=1, row=0)
#ui

start_button =  tkinter.Button(text="Start", command=start_timer)
start_button.place(x=25, y=380)

reset_button =  tkinter.Button(text="Reset")
reset_button.place(x=100, y=380)

worktimentry = tkinter.Entry()
worktimentry.insert(0,'15')
worktimentry.place(x=200,y=380, width = 20)
worktimelabel = tkinter.Label(text='work')
worktimelabel.place(x=225,y=380)

breaktimentry = tkinter.Entry()
breaktimentry.insert(0,'15')
breaktimentry.place(x=200,y=400, width = 20)
breaktimelabel = tkinter.Label(text='break')
breaktimelabel.place(x=225,y=400)


worktime = int(worktimentry.get())
breaktime = int(breaktimentry.get())






window.mainloop()


#TODO radio buttons for different break timers
#TODO Noise packs and implentation
#TODO resize buttons and windows 
#