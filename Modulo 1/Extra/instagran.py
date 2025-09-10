import pyautogui as pag
from time import sleep

#pag.displayMousePosition()

pag.press('win')
pag.write('chrome')
pag.press('enter')
sleep(1)
pag.hotkey('ctrl','shift','n')
sleep(1)
pag.write('www.instagram.com')
pag.press('enter')
pag.moveTo(1210,400,duration=1)
pag.click()
pag.write('souzagabrielwendeldesouza@gmail.com')
pag.press('tab')
pag.write('GabrieleIsaak')

