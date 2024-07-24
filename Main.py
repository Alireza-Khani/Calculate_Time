from tkinter import *
from tkinter.ttk import *

master = Tk()

# setting the windows size
master.geometry("600x400")

# declaring string variable
# for storing name and password
firstTime = StringVar()
secondTime = StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    resultLabel = Label(master, text="", font=('calibre', 10, 'bold'))
    resultLabel.grid(row=3, column=3)
    hour = 0
    minute = 0
    text = ""
    try:
        first = firstTime.get().split(':')
        second = secondTime.get().split(':')
        radioValue = radio.get()

        if radioValue == '+':
            hour = int(first[0]) + int(second[0])
            minute = int(first[1]) + int(second[1])
            extraHour = int(minute / 60)
            hour += extraHour
            minute -= (extraHour * 60)
            text = f"{hour}:{minute}"

        elif radioValue == '-':
            hour = int(first[0]) - int(second[0])
            minute = int(first[1]) - int(second[1])
            if minute < 0:
                hour -= 1
                minute += 60

            text = f"{hour}:{minute}"

        firstTime.set("")
        secondTime.set("")

    except:
        text = "Enter correct time"
    finally:
        resultLabel = Label(master, text=text, font=('calibre', 10, 'bold'))
        resultLabel.grid(row=3, column=3)


name_label = Label(master, text='First Time', font=('calibre', 10, 'bold'))

name_entry = Entry(master, textvariable=firstTime, font=('calibre', 10, 'normal'))

passw_label = Label(master, text='Second Time', font=('calibre', 10, 'bold'))

passw_entry = Entry(master, textvariable=secondTime, font=('calibre', 10, 'normal'))

sub_btn = Button(master, text='Submit', command=submit)

radio = StringVar(master, "1")

addRadio = Radiobutton(master, text="Add", variable=radio, value="+")
subRadio = Radiobutton(master, text="Sub", variable=radio, value="-")

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)
addRadio.grid(row=3, column=0)
subRadio.grid(row=3, column=1)

mainloop()
