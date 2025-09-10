import pyautogui as pag
from time import sleep
import keyboard
# pag.mouseInfo()
# pag.displayMousePosition()

pag.press('win')
pag.write('chome')
pag.press('enter')
sleep(1)
pag.write('https://www.minijogos.com.br/jogo/rpg-idle-clicker')
pag.press('enter')
sleep(1)

keyboard.wait('s')
sleep(1)
while True:
    pag.doubleClick()
    if keyboard.is_pressed('g'):
        break
#---------------------------------------------------------------------------------TENTATIVA2
# pag.press('win')
# pag.write('chome')
# pag.press('enter')
# sleep(1)
# pag.write('tudo gostoso')
# pag.press('enter')
# pag.moveTo(351,307,duration=2)
# pag.click()
# sleep(1)
# pag.moveTo(974,135,duration=2)
# pag.click()
# pag.write('pizza')
# pag.press('enter')
# pag.moveTo(856,812,duration=2)
# pag.click()
# sleep(3)
# pag.scroll(-500)
# pag.moveTo(1079,807,duration=2)
# pag.click()
# sleep(1)
# pag.click()
