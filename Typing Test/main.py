from tkinter import *
import random
from data import data


para_list = []
index = 0
count = 7
entered_text = ''

'''
This function is the first step when the start button is pressed.It randomly picks a paragraph from list
and calls content to start displaying the lines on screen and also starts the timer.

It also reset the values when the start button is pressed again to take the test again.
'''
def start_timer():
    global para_list,index
    index = 0
    entry.config(state=NORMAL)
    entry.delete(0,END)
    nwpm_label.config(text='')
    start_button.config(state='disabled')
    para = random.choice(data)
    para_list = para.split(' ')
    content()
    countdown(59)

'''
The countdown function is responsible for the timer and the steps to be taken once time is up.
'''
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
        entry.config(state=DISABLED)
        calculate_nwpm()

'''
The content function is display next line when entry key is pressed.
'''
def content():
    global index
    text = para_list[index:index+7]
    passage.config(text=" ".join(text))
    index += 7

'''
The enter function listens to the entry key and calls the content function to display next line.
'''
def enter(e):
    global entered_text, count
    data = entry.get()
    count = len(data.split(' ')) 
    entered_text = entered_text + ' ' + data
    
    if count >=7:
        entry.delete(0, END)
        content()

'''
This function is use to calculate net word per minute after the timer goes off.
To calculate nwpm we calculate words per minute which include spaces and puncuation and divide them by 5.
After calculating wpm we see how many mistakes we made and we detect them from wpm for accurate calculation.
'''
def calculate_nwpm():
    global entered_text
    entered_text = entered_text + ' ' + entry.get()
    passage.config(text='Score is displayed below!!')
    entered_text_list = (entered_text.split(' '))[1:]
    wpm = round(len(entered_text[1:])/5)
    mistake = 0
    print(para_list)
    print(entered_text_list)
    for i in range(0,len(entered_text_list)):
        if entered_text_list[i] != '' and para_list[i] != entered_text_list[i]:
            mistake += 1
    nwpm = wpm-mistake  

    nwpm_label.config(text=f'Your Score is : {nwpm} nwpm')





window = Tk()
window.title('Speed Typing Test')
window.geometry("700x550")
window.config(background='black', height=550, width=700, padx=70, pady=50)

label = Label(text='Speed Typing Test', fg='white', background='Black', font=('Courier', 40, 'bold') )
label.grid(row=0, column=1, pady=3)

canvas = Canvas(height=150, width=200,highlightthickness=0)
typing_img = PhotoImage(file='images.png')
canvas.create_image(100,75, image=typing_img)
canvas.grid(row=1,column=1)

timer = Label(text='1:00', fg='white', background='black', font=('Arial',30))
timer.grid(row=2,column=1, pady=10)

passage = Label(text='This is where paragraph will be displayed', font=('Courier', 18, 'bold'), 
                fg='white', background='black')
passage.grid(row=3, column=1)

entry = Entry(width=42, font=('Courier', 18, 'bold'))
entry.grid(row=4, column=1, pady=3)
entry.focus()

start_button = Button(text='Start', width=20, font=('Arial',15), command=start_timer)
start_button.grid(row=5, column=1, pady=7)

nwpm_label = Label(text='', bg='black', fg='white', font=('Courier', 18, 'bold'))
nwpm_label.grid(row=6,column=1)

window.bind('<Return>',enter)

window.mainloop()
