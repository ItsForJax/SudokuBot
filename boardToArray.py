import pyautogui as pg
import easyocr
import numpy as np
from matplotlib import pyplot as plt
import time

reader = easyocr.Reader(['en'],gpu = False)
pth = 'img/tiles/t20.jpg'
res = reader.readtext(pth)
res
#for x in range(9):
#    for y in range(9):
#        img = pg.screenshot(region=(42+(x * (500/9)),238+(y * (500/9)),500/9,500/9))
#        img.save(fr"C:\Users\Dadelos\Desktop\SudokuBot\img\tiles\t{x}{y}.jpg")