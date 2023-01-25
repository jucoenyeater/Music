# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:01:05 2023

@author: jucoe
"""

import random
import itertools
from tkinter import *
from tkinter import font

# Create the main Tkinter window
root = Tk()
root.title("Random 3-Word Combination")

# Create list of words to be combined
list1 = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
list2 = ["Root Position", "First Position", "Second Position"]
list3 = ["Root Inversion", "First Inversion", "Second Inversion"]

list1 = ["B"]
list2 = list2
list3 = ["Root Inversion"]

# Creates all possible combination sof the words in the lists
combination = list(itertools.product(list1, list2, list3))

# Shuffle the combinations
random.shuffle(combination)

# Create the label widget to display the words
label = Label(root, text="")
label.pack()

# Create the timer variable and entry widget
timer_var = IntVar()
timer_var.set(30)
timer_entry = Entry(root, textvariable=timer_var)
timer_entry.pack()

# Create a flag to track the state of the timer
is_running = False

# Create an iterator for the word combinations
combination_iter = iter(combination)

# =============================================================================
# # Create a label to hold the image
# image = PhotoImage(file = "image.png")
# image_label = Label(root, image=image)
# =============================================================================

# Create a variable to track if the result image should be visible
result_visible = False

# Create a function to toggle the visibility of the result image
def toggle_result():
    global result_visible
    if result_visible:
        result_button.config(text="Show Result")
        result_visible = False
        result_label.pack_forget()
    else:
        result_button.config("Hide Result")
        result_visible = True
        result_label.pack()
        
# Create the Rsults button to toggle the result image
result_button = Button(root, text="Results", command=toggle_result)
result_button.pack()

# Function to update label with a new word combination
def update_label():
    global is_running
    # Check if the timer is running
    if not is_running:
        return
    # Get the next combination of words
    word1, word2, word3 = next(combination_iter)
    # label.config(text=f"{word1} {word2} {word3}")
    label.config(text="\n".join([word1, word2, word3]))
    root.after(timer_var.get()*1000, update_label)
    
# Function to display result tab for the chord
def show_image():
    image_label.pack()
    root.after(timer_var.get()*1000, show_image)
    
# Function to hide the resulting chord tab
def hide_image():
    image_label.pack_forget()
    update_label()
    
# Function to start / stop the timer
def toggle_timer():
    global is_running
    if is_running:
        start_stop_button.config(text="Start")
        is_running = False
    else:
        start_stop_button.config(text="Stop")
        is_running = True
        timer_var.set(int(timer_entry.get()))
        update_label()
    
# Creat the start / stop button
start_stop_button = Button(root, text="Start", command=toggle_timer)
start_stop_button.pack()


# Set the font and font size for the widgets
font_tuple = ("Arial", 50)
label_font = font.Font(family=font_tuple[0], size=font_tuple[1])
label.config(font=font_tuple)
timer_entry.config(font=font_tuple, width=10)
start_stop_button.config(font=("Arial", 20))

# Find the longest combination of words to be used to size the window
longest_combination = max(combination, key=lambda x: len(" ".join(x)))

# Calculate the width and heigh tof the window based on the longest combination
width = label_font.measure(" ".join(longest_combination)) + timer_entry.winfo_width() + 70
height = label_font.metrics("linespace") * (len(combination[0])+2)
old_height = label.winfo_reqheight()

# Update the geometry of the window
root.update() # Render widget for the correct geometry to populate

# Catch any errors when first creating the window
try:
    root.geometry(f"{width}x{height}")
except TclError as e:
    print(f"Error: {e}")

# root.resizable(False,False)

# Run the loop
root.mainloop()