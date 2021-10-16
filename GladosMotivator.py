# Break study machine

import tkinter
import time
import math
import random
#playsound requires version 1.2.2 new version is broken?
from playsound import playsound 

window = tkinter.Tk()
window.title('GladOsMotivator')
window.geometry('800x530')
work = True 

def play_Line():
    Break_glines = ['brb.wav','didwell.wav']
    Work_glines = ['imbecile.wav','justdoit.wav']
    if work == True:
        playsound(Break_glines[random.randint(0,2)])
    else:
        playsound(Work_glines[random.randrange(2)])




def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    Timer = tkinter.Label(text=f" {count_min} : {count_sec} ", fg="white", bg='black')
    Timer.place(x=150,y=380)
    if count > 0:
        print(count)
        window.after(1000, count_down, count - 1)
    elif count == 0:
        print('switch!')
        global work 
        if work == True:
            play_Line()
        else:
            play_Line()
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

worktimentry = tkinter.Entry(bg='black',fg='white')
worktimentry.insert(0,'15')
worktimentry.place(x=200,y=380, width = 20)
worktimelabel = tkinter.Label(text='work',fg='#000000')
worktimelabel.place(x=225,y=380)

breaktimentry = tkinter.Entry(bg='black',fg='white')
breaktimentry.insert(0,'15')
breaktimentry.place(x=200,y=400, width = 20)
breaktimelabel = tkinter.Label(text='break')
breaktimelabel.place(x=225,y=400)


worktime = int(worktimentry.get())
breaktime = int(breaktimentry.get())






window.mainloop()


#TODO radio buttons for different break timers
#radio buttons were switched out for customizable entry extra points if we create a lock but seems just aesthetic
#TODO Noise packs and implentation
#noise packs exist and are implented with playsound 1.2.2 next to create either a dict or a list of available packs and randomize
#TODO resize buttons and windows
# need bolds weights for labels and possible resizing of entry widgets, coloring can be done with hexidecimals 
# I need to finalize backround mage in an editor before placement 
#im bad at graphic design some i waiting till the backend is up and functional before placement probably place this last
#TODO add appenable todo list with crossout or checkbox 
