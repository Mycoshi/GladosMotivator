# Break study machine

from tkinter import *
import time
import math

window = Tk()
window.title('study')
window.config(padx=5, pady=5, bg='white')


def start_timer():
    count_down(5 * 60)


def count_down(count):


    count_min = math.floor(count / 60)
    count_sec = count % 60

    Timer = Label(text=f"{count_min}:{count_sec}", fg="black")
    Timer.grid(column=1, row=2)

    if count > 0:
        print(count)
        window.after(1000, count_down, count - 1)
    #elif count == 0:



canvas = Canvas(width=800, height=850, )
background = PhotoImage(file='background.png')
canvas.create_image(400, 400, image=background)
canvas.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.place(x=25, y=600)

reset_button = Button(text="Reset")
reset_button.place(x=25, y=675)

Marks = Label(text='X', fg='black')
Marks.grid(column=1, row=1)



window.mainloop()
