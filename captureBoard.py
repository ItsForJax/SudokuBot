import pyautogui as pg

#run until the board's screenshot is perfectly fit (refer to ss_reference.png)
img = pg.screenshot(region=(42,238,500,500))
img.save(r"C:\Users\Dadelos\Desktop\SudokuBot\img\ss.png")



