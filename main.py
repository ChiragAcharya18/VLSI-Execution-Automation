import subprocess
import time
import os
from threading import Thread
import pyautogui

def kill(name):
    time.sleep(8)
    im1 = pyautogui.screenshot()
    im1.save(f"C:\\Users\\chirag\\Desktop\\VSCode\\ProjectTemp\\vlsiimgs\\{name}.png")
    subprocess.call(['taskkill','/F','/IM','gtkwave.exe'])
    t1._stop

names = []
names = input('Enter name of the files: ').split(" ")

for name in names:
    o1 = subprocess.check_output(['iverilog',f"{name}.v",f"{name}_t.v"]).decode('utf-8')
    if o1 == "":
        o2 = subprocess.check_output(['vvp','a.out']).decode('utf-8')
        if "vcd opened for output" in o2:
            vcd = o2.split(" ")[3]
            n = str(name)
            t1 = Thread(target=kill, args=(n,))
            t1.start()
            subprocess.call(['gtkwave',vcd], shell=False)
            print("Next program in 2 seconds!")
            time.sleep(1)

 