#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()

clock.title("Lancelott Alarm Clock")
clock.geometry("400x400")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=80,y=300)
addTime = Label(clock,text = "Hr  Min  Sec",font=60).place(x = 145,y=30)
setYourAlarm = Label(clock,text = "  WAKE UP TIME  ",fg="black",relief = "solid",font=("Helevetica",10,"bold")).place(x=140, y=150)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "skyblue",width = 5).place(x=145,y=80)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 5).place(x=185,y=80)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 5).place(x=225,y=80)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="black",width = 25,command = actual_time).place(x =110,y=210)

clock.mainloop()
#Execution of the window.    