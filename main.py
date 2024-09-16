from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = ("Courier", 10)
FONT_BOLD = ("Courier", 35, "bold")
reps = 0
timer = None

# ---------------------------- TIMER RESET --------------------------------------- # 

def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    title_lbl.config(text="Timer",fg=GREEN)
    check_lbl.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    reps = 0  # Reset reps to 0


# ---------------------------- TIMER MECHANISM ----------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*20
    long_break_sec = LONG_BREAK_MIN*20
    short_break_sec = SHORT_BREAK_MIN*10

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lbl.config(text="Break",font=("Courier",45, "bold"),fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lbl.config(text="Break",font=("Courier",45, "bold"),fg=PINK)
    else:
        count_down(work_sec)
        title_lbl.config(text="Work",font=("Courier",45, "bold"),fg=RED)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer  
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000, count_down, count-1) #timer variable
    else:
        start_timer()

        mark = ""
        work_sess = math.floor(reps/2)
        for _ in range(work_sess):
            mark+="✔"
        check_lbl.config(text=mark)
# ---------------------------- UI SETUP ------------------------------------------ #

#window setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)
window.eval('tk::PlaceWindow . center')

#create a canvas & an image
canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(102,113, image=tomato_pic)
timer_text = canvas.create_text(103,124, text="00:00", fill="white", font=FONT_BOLD)

#Label
title_lbl = Label(text="Timer", fg=GREEN, font=("Courier",45, "bold"),bg=YELLOW)
check_lbl = Label(fg=GREEN, font=FONT_BOLD, bg=YELLOW)

#Buttons
start_btn = Button(text="Start", padx=10,pady=5, font=FONT, command=start_timer)
reset_btn = Button(text="Reset", padx=10,pady=5, font=FONT, command=reset_timer)

#Grid Layout
title_lbl.grid(column=1,row=0)
canvas.grid(column=1, row=1)
start_btn.grid(column=0,row=2)
reset_btn.grid(column=2, row=2)
check_lbl.grid(column=1, row=3)

window.mainloop()