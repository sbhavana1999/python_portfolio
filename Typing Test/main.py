from tkinter import *
import random
from data import data

para_list = []

def start_timer():
    global para_list
    start_button.config(state='disabled')
    para = random.choice(data)
    para_list = para.split(' ')
    countdown(59)


def countdown(count):
    if count >=0 :
        if count <= 9 :
            count = '0'+str(count)
            timer.config(text=f"00:{count}")
            count = int(count)
        else:    
            timer.config(text=f"00:{count}")
        window.after(1000, countdown, count-1)
    else:
        timer.config(text='Times UP')
        start_button.config(state='normal')


def content():
    pass












window = Tk()
window.title('Speed Typing Test')
window.geometry("700x550")
window.config(background='black', height=550, width=700, padx=80, pady=50)

label = Label(text='Speed Typing Test', fg='white', background='Black', font=('Courier', 40, 'bold') )
label.grid(row=0, column=1)

canvas = Canvas(height=150, width=200,highlightthickness=0)
typing_img = PhotoImage(file='images.png')
canvas.create_image(100,75, image=typing_img)
canvas.grid(row=1,column=1)

timer = Label(text='1:00', fg='white', background='black', font=('Arial',30))
timer.grid(row=2,column=1)

passage = Label(text='This is where paragraph will be displayed', font=('Courier', 18, 'bold'), 
                fg='white', background='black')
passage.grid(row=3, column=1)

entry = Entry(width=42, font=('Courier', 18, 'bold') )
entry.grid(row=4, column=1, pady=3)

start_button = Button(text='Start', width=10, command=start_timer)
start_button.grid(row=5, column=1, pady=7)

window.mainloop()
