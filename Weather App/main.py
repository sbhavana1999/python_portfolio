from tkinter import *
from api import tempertaure

sun = None
moon = None

def on_enter():
    global sun,moon
    city = entry.get()


    time, temps = tempertaure(city)

    if len(temps) != 0:
        canvas = Canvas(height=400, width=600, background="#36454F")
        city_label = canvas.create_text(50,35, text=f"{city.title()}", font=('Courier', 20, "normal"), fill='White')
        curr_temp = canvas.create_text(50,58, text=f"{temps[0]}°C", font=('Courier', 17, "normal"), fill='White')
        canvas.create_line(2, 80, 600, 80 , fill='white', width=2)
        sun = PhotoImage(file='sun1.png')
        moon = PhotoImage(file='moon2.png')
        dis = 0
        for i in range(1,len(temps)):
            _time = str((time+i)%24)
            if len(_time) != 2:
                _time = '0'+_time  
            canvas.create_text(50+dis, 150 , text=f"{_time}:00", font=('Courier', 15, "normal"), fill='White' )
            
            if int(_time) >= 6 and int(_time) <= 18:
                canvas.create_image(50+dis,200, image=sun) 
            else:
                canvas.create_image(50+dis,200, image=moon)    

            canvas.create_text(50+dis, 260 , text=f"{temps[i]}°C", font=('Courier', 15, "normal"), fill='White' )     
            dis += 95
        
        canvas.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    else:
        label_city = Label(text="The Entered city is not present.", background='Beige', 
                           font=('Courier', 10, 'normal'))  
        label_city.grid(row=2, column=0, columnspan=3, padx=10, pady=10)  



window = Tk()
window.title('Weather App')
window.geometry("640x500")
window.config(background='Beige')

label = Label(text="Today's Weather", background='Beige', font=('Courier', 25, 'bold'))
label.grid(row=0, column=1, pady=3)

label_city = Label(text="Enter City Name : ", background='Beige', font=('Courier', 15))
label_city.grid(row=1, column=0, pady=3)
entry = Entry(width=20, font=('Courier', 18))
entry.grid(row=1, column=1)
entry.focus()
enter = Button(text="Enter", command=on_enter)
enter.grid(row=1, column=2)

window.mainloop()