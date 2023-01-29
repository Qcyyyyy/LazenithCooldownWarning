

#import pygame
#import keyboard

#pygame.init()
#pygame.mixer.init()

#while True:
#    if keyboard.read_key() == "left":
#        pygame.mixer.music.load("24s.mp3")
#        pygame.mixer.music.play

import keyboard
import tkinter as tk

def on_press(key):
    # Update the label with the pressed key
    label.config(text=key)

# Create the GUI window
root = tk.Tk()
root.title("Keyboard Input")

# Create a label to display the pressed key
label = tk.Label(root, text="")
label.pack()

keyboard.on_press(on_press)

keyboard.add_hotkey("ctrl+alt+delete", keyboard.press_and_release, args=("ctrl+alt+delete",))

root.mainloop()


