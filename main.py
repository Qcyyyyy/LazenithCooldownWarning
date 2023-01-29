

import pygame
import keyboard
import tkinter as tk

pygame.init()
pygame.mixer.init()

keybindLockFlag = True
endOfLazenithFlag = True
currentKeybind = "NO KEYBIND SET"
onFlag = False


def on_press(key):
    global currentKeybind
    # Update the label with the pressed key if keybind is set so unlocked.
    if keybindLockFlag == False:
        label.config(text=key)
        currentKeybind = key

    if currentKeybind == key and onFlag == True:
        print("playing")
        pygame.mixer.music.load("24s.mp3")
        pygame.mixer.music.play()


def buttonOnOffClick():
    global onFlag
    if onFlag == False:
        buttonOnOff.config(text="Turn Off")
        onFlag = True
    else:
        buttonOnOff.config(text="Turn On")
        onFlag = False


def buttonKeybindLockClick():
    global keybindLockFlag
    if keybindLockFlag == False:
        buttonKeybindLock.config(text="Unlock Keybind Setting")
        keybindLockFlag = True
    else:
        buttonKeybindLock.config(text="Lock Keybind Setting")
        keybindLockFlag = False



# Create the GUI window
root = tk.Tk()
root.config(bg="black")
root.resizable(False, False)
root.title("Lazenith Cooldown Warning")

canvas = tk.Canvas(root, width=256, height=256)
canvas.pack(padx=50, pady=20)
img = tk.PhotoImage(file="lazenithbg.png")
canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Create a label to display the pressed key
label = tk.Label(root, text="No Keybind Set")
label.pack(pady=10)

buttonKeybindLock = tk.Button(root, text="Unlock Keybind Setting", command=buttonKeybindLockClick)
buttonKeybindLock.pack()

buttonOnOff = tk.Button(root, text="Turn On", command=buttonOnOffClick)
buttonOnOff.pack(padx=10, pady=30)

keyboard.on_press(on_press)

keyboard.add_hotkey("ctrl+alt+delete", keyboard.press_and_release, args=("ctrl+alt+delete",))

root.mainloop()


