import inflect
import pyautogui as pg
import pydirectinput as pd
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def do_gj(num, starting, num_starting):
    if starting == False:
        time.sleep(5)
        p = inflect.engine()
        for x in range (1, num):
            c = p.number_to_words(x)
            pd.press('/')
            pg.typewrite(c.capitalize()+("."))
            pd.press('enter')
            pd.press('space')
            time.sleep(0.25)
    else:
        time.sleep(5)
        p = inflect.engine()
        for x in range (num_starting, num):
            c = p.number_to_words(x)
            pd.press('/')
            pg.typewrite(c.capitalize()+("."))
            pd.press('enter')
            pd.press('space')
            time.sleep(0.25)
def do_hj(num, starting, num_starting):
    time.sleep(5)
    p = inflect.engine()
    if starting == "False":
        for x in range (1, num):
            time.sleep(.5)
            c = p.number_to_words(x)
            for element in c.capitalize()+("."):  
                pd.press('/')
                pg.typewrite(element)
                pd.press('enter')
                pd.press('space')
                time.sleep(0.25)
            time.sleep(0.5) 
            pd.press('/')
            pg.typewrite(c.capitalize()+("."))
            pd.press('enter')
            pd.press('space')
    else:
        for x in range (num_starting, num):
            time.sleep(.5)
            c = p.number_to_words(x)
            for element in c.capitalize()+("."):  
                pd.press('/')
                pg.typewrite(element)
                pd.press('enter')
                pd.press('space')
                time.sleep(0.25)
            time.sleep(0.5) 
            pd.press('/')
            pg.typewrite(c.capitalize()+("."))
            pd.press('enter')
            pd.press('space')
def do_dj(num, starting, num_starting):
    if starting == False:
        time.sleep(5)
        p = inflect.engine()
        for x in range (1, num):
            time.sleep(.5)
            c = p.number_to_words(x)
            word = c.capitalize()+(".")
            for element in word[::-1]:  
                pd.press('/')
                pg.typewrite(element)
                pd.press('enter')
                pd.press('space')
                time.sleep(0.25)
            time.sleep(0.5) 
            pd.press('/')
            pg.typewrite(word[::-1])
            pd.press('enter')
            pd.press('space')
    else:
        time.sleep(5)
        p = inflect.engine()
        for x in range (num_starting, num):
            time.sleep(.5)
            c = p.number_to_words(x)
            word = c.capitalize()+(".")
            for element in word[::-1]:  
                pd.press('/')
                pg.typewrite(element)
                pd.press('enter')
                pd.press('space')
                time.sleep(0.25)
            time.sleep(0.5) 
            pd.press('/')
            pg.typewrite(word[::-1])
            pd.press('enter')
            pd.press('space')


