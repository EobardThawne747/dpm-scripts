import pyautogui
import time

serv_location = pyautogui.locateCenterOnScreen(r'C:\Users\admin.erinm\Desktop\samples\server.png', confidence = 0.5)
pyautogui.click(serv_location) #klikon tek ikona e server manager 

while True: #pret derisa te gjeje file location
    if pyautogui.locateCenterOnScreen(r'C:\Users\admin.erinm\Desktop\samples\files.png') != None:
        files_location = pyautogui.locateCenterOnScreen(r'C:\Users\admin.erinm\Desktop\samples\files.png', confidence = 0.5)
        break
pyautogui.click(files_location) 

time.sleep(1)

pyautogui.click(103,145) #(103,145) volume click

time.sleep(17) #per tu bere load volumet

pyautogui.click(1254,198) #klikimi tek pjesa gri qe te behet scroll



while True: #scroll derisa te gjeje C:
    if pyautogui.locateCenterOnScreen(r'C:\Users\admin.erinm\Desktop\samples\c.png') != None:
        c_location = pyautogui.locateCenterOnScreen(r'C:\Users\admin.erinm\Desktop\samples\c.png')
        break
    pyautogui.scroll(-100)
    pyautogui.scroll(-100)
    pyautogui.scroll(-100)
    pyautogui.scroll(-100)
    time.sleep(0.1)

pyautogui.click(c_location)

pyautogui.screenshot(r'C:\Users\admin.erinm\Desktop\DPMSRV-HC250\VolumeC.png')

pyautogui.click(1889,6) #close server manager
