import sys

import pygame
import keyboard
import tkinter as tk

pygame.init()
pygame.mixer.init()

keybindLockFlag = True
endOfLazenithFlag = True
currentKeybind = ""
onFlag = False
counter = 24
currentCount = 0
countingDownFlag = False


def onPress(key):
    global currentKeybind
    global currentCount
    # Update the label with the pressed key if keybind is set so unlocked.
    if not keybindLockFlag:
        label.config(text=key)
        currentKeybind = key
    if currentKeybind == key and onFlag == True and not countingDownFlag:
        if endOfLazenithFlag:
            pygame.mixer.music.load("./24s.mp3")
        else:
            pygame.mixer.music.load("./32s.mp3")
        pygame.mixer.music.play()
        currentCount = 0
        updateCountdown()


def buttonOnOffClick():
    global onFlag
    if not onFlag:
        buttonOnOff.config(text="Turn Off")
        onFlag = True
    else:
        buttonOnOff.config(text="Turn On")
        onFlag = False


def buttonKeybindLockClick():
    global keybindLockFlag
    if not keybindLockFlag:
        buttonKeybindLock.config(text="Unlock Keybind Setting")
        keybindLockFlag = True
    else:
        buttonKeybindLock.config(text="Lock Keybind Setting")
        keybindLockFlag = False


def set24s():
    global endOfLazenithFlag
    global counter
    counter = 24
    timeLeft.config(text=24)
    endOfLazenithFlag = True


def set32s():
    global endOfLazenithFlag
    global counter
    counter = 32
    timeLeft.config(text=32)
    endOfLazenithFlag = False


def updateCountdown():
    global currentCount
    global countingDownFlag
    countingDownFlag = True
    if currentCount < counter and onFlag:
        timeLeft.config(text=counter-currentCount)
        currentCount += 1
        root.after(1000, updateCountdown)
    else:
        timeLeft.config(text=counter)
        countingDownFlag = False


# Create the GUI window
root = tk.Tk()
root.config(bg="#2F3136")
root.resizable(False, False)
root.title("Lazenith CD Warning | By Qcy")

buttonFrame = tk.Frame(root, bd=0)
buttonFrame.pack(pady=10)

button24 = tk.Button(buttonFrame, text="24s", command=set24s)
button24.pack(side="left")
button24.config(font=("Myriad", 13, "bold"))
button32 = tk.Button(buttonFrame, text="32s", command=set32s)
button32.pack(side="left")
button32.config(font=("Myriad", 13, "bold"))

timeLeftLabel = tk.Label(root, text="Time left:")
timeLeftLabel.pack(pady=5)
timeLeftLabel.config(bg="#36393F", fg="#FFFFFF", font=("Myriad", 13, "bold"))

timeLeft = tk.Label(root, text=24)
timeLeft.pack(padx=100)
timeLeft.config(bg="#36393F", fg="#FFFFFF", font=("Myriad", 100, "bold"))

# Create a label to display the pressed key
label = tk.Label(root, text="No Keybind Set")
label.pack(pady=10)
label.config(bg="#36393F", fg="#FFFFFF", font=("Myriad", 13, "bold"))

buttonKeybindLock = tk.Button(root, text="Unlock Keybind Setting", command=buttonKeybindLockClick)
buttonKeybindLock.pack(padx=70)
buttonKeybindLock.config(font=("Myriad", 13, "bold"))

buttonOnOff = tk.Button(root, text="Turn On", command=buttonOnOffClick)
buttonOnOff.pack(padx=10, pady=30)
buttonOnOff.config(font=("Myriad", 13, "bold"))

keyboard.on_press(onPress)

keyboard.add_hotkey("ctrl+alt+delete", keyboard.press_and_release, args=("ctrl+alt+delete",))

root.mainloop()


