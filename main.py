# Break study machine

import tkinter
import time
import math
import operator

window = tkinter.Tk()
window.title('GladOsMotivator')
window.geometry('800x500')
worktime = 5
breaktime = 10

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    Timer = tkinter.Label(text=f" {count_min} : {count_sec} ", fg="white", bg='black')
    Timer.place(x=150,y=380)
    if count > 0:
        print(count)
        window.after(1000, count_down, count - 1)
    elif count == 0:

       start_timer()

def start_timer():
    count_down( * 5)





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

worktimentry = tkinter.Entry(text="work")
worktimentry.place(x=200,y=380, width = 20)

breaktimentry = tkinter.Entry(text="break")
breaktimentry.place(x=200,y=400, width = 20)


#timesetbutton = tkinter.Radiobutton(window, text='20on-10off', command = timeset1, value = 1)
#timesetbutton.place(x=200, y=380)

#timesetbutton2 = tkinter.Radiobutton(window, text='10on-10off', command = timeset2, value = 2)
#timesetbutton2.place(x=200, y=360)

window.mainloop()


#TODO radio buttons for different break timers
#TODO Noise packs and implentation
#TODO resize buttons and windows 
#