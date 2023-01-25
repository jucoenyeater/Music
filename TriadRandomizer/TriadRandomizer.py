# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:01:05 2023

@author: jucoe
"""

import random
import itertools
from tkinter import *
from tkinter import font


root = Tk()
root.title("Random 3-Word Combination")


list1 = ["A","A#","B","B#","C","C#","D","D#","E","F","F#","G","G#"]
list2 = ["Root Position", "First Position", "Second Position"]
list3 = ["Root Inversion", "First Inversion", "Second Inversion"]
combination = list(itertools.product(list1, list2, list3))
random.shuffle(combination)

label = Label(root, text="")
label.pack()

timer_var = IntVar()
timer_var.set(5)
timer_entry = Entry(root, textvariable=timer_var)
timer_entry.pack()

# Initiate is_running state
is_running = False

combination_iter = iter(combination)

# Create a label to hold the image
image = PhotoImage(file = "image.png")
image_label = Label(root, image=image)

def update_label():
    global is_running
    if not is_running:
        return
    word1, word2, word3 = next(combination_iter)
    # label.config(text=f"{word1} {word2} {word3}")
    label.config(text="\n".join([word1, word2, word3]))
    root.after(timer_var.get()*1000, update_label)
    
def toggle_timer():
    global is_running
    if is_running:
        start_stop_button.config(text="Start")
        is_running = False
    else:
        start_stop_button.config(text="Stop")
        is_running = True
        update_label()
    

start_stop_button = Button(root, text="Start", command=toggle_timer)
start_stop_button.pack()



font_tuple = ("Arial", 50)
label_font = font.Font(family=font_tuple[0], size=font_tuple[1])
label.config(font=font_tuple)
timer_entry.config(font=font_tuple, width=10)
start_stop_button.config(font=("Arial", 20))

longest_combination = max(combination, key=lambda x: len(" ".join(x)))
width = label_font.measure(" ".join(longest_combination)) + timer_entry.winfo_width() + 70
height = label_font.metrics("linespace") * (len(combination[0])+2)
old_height = label.winfo_reqheight()

root.update() # Render widget to for the correct geometry to populate

try:
    root.geometry(f"{width}x{height}")
except TclError as e:
    print(f"Error: {e}")

# root.resizable(False,False)


root.mainloop()