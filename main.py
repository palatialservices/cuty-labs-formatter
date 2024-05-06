# Made by bltondc | discord.gg/botter

import  ctypes,  os

from    os          import system

os.system("cls")

def set_window_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

class stats:
    formatted = 0

set_window_title(f"Palatial Cuty Formatter | Done {stats.formatted}")

with open('tokens.txt', 'r') as file:
    lines = file.readlines()

for line in lines:

    token = line.strip().split('|')[1]
    open('output.txt', 'a').write(token + "\n")