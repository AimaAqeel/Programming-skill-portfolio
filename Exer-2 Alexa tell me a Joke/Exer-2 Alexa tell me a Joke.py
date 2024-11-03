# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 04:09:46 2024

@author: pc
"""

from tkinter import *
import random

# Load jokes from file
def load_jokes(filename="randomJokes.txt"):
    jokes = []
    with open(filename, 'r') as file:
        for line in file:
            setup, punchline = line.strip().split('?')
            jokes.append((setup + '?', punchline))
    return jokes

# Display setup and wait for the user to reveal the punchline
def tell_joke():
    global current_joke
    current_joke = random.choice(jokes)
    setup_label.config(text=current_joke[0])
    punchline_button.config(state=NORMAL)
    punchline_label.config(text="")

# Display the punchline when button is clicked
def show_punchline():
    punchline_label.config(text=current_joke[1])
    punchline_button.config(state=DISABLED)

# Load jokes and initialize Tkinter app
jokes = load_jokes()
current_joke = None

# Setup Tkinter window
root = Tk()
root.geometry("300x300")
root.title("Alexa, tell me a Joke")

# Display Setup Label
setup_label = Label(root, text="Click 'Tell me a joke' to start!", font=("Arial", 14), wraplength=400)
setup_label.pack(pady=10)

# Button to get a new joke setup
joke_button = Button(root, text="Alexa, tell me a joke", command=tell_joke, font=("Arial", 12))
joke_button.pack(pady=5)

# Button to show punchline
punchline_button = Button(root, text="Show Punchline", command=show_punchline, state=DISABLED, font=("Arial", 12))
punchline_button.pack(pady=5)

# Label to display punchline
punchline_label = Label(root, text="", font=("Arial", 14), fg="blue", wraplength=400)
punchline_label.pack(pady=10)

root.mainloop()
