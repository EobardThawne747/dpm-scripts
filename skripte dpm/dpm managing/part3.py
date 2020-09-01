import pyautogui
import time
import pyperclip

folder_location = ''

def image_recognition(image, error_message, conf): #kthen kordinatat e qendres se imazhit
    error_counter = 0
    while True: #loop cdo sekonde derisa te gjeje image
        if pyautogui.locateCenterOnScreen(image, confidence = conf) != None:
           location = pyautogui.locateCenterOnScreen(image, confidence = conf)
           time.sleep(1)
           break
        error_counter +=1 #shfaq mesazhin e errorit pas 20 sekondash per te kerkuar inputin e userit
        if error_counter > 20:
            pyautogui.alert(error_message)
            error_counter = 0
    return location

def explorer_reports(): #handle pjesen e explorerit

    
    image = r'C:\Users\admin.erinm\Desktop\DPMIMage\pdf_format.PNG'  
    error_message = "Programi eshte duke kerkuar per ikonen blu qe ti beje save raportin ne pdf"
    
    pdf_format = image_recognition(image, error_message, 0.99)
    pyautogui.moveTo(pdf_format, duration = 0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('enter')

    image = r'C:\Users\admin.erinm\Desktop\DPMIMage\save.PNG'
    error_message = "Programi eshte duke kerkuar per ikonen save"
    
    save_button = image_recognition(image, error_message, 0.99)
    pyautogui.moveTo(save_button, duration = 0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('enter')

    global folder_location #variabel global pasi pathi na duhet vetem njehere
    if folder_location == '':
        image = r'C:\Users\admin.erinm\Desktop\DPMIMage\path.PNG'
        error_message = "Programi eshte duke kerkuar per te ruajtur pathin"

        path_location = image_recognition(image, error_message, 0.8)
        pyautogui.moveTo(path_location.x - 100, path_location.y, duration = 0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
    
        folder_location = pyperclip.paste()


    image = r'C:\Users\admin.erinm\Desktop\DPMIMage\save2.PNG'
    error_message = "Programi eshte duke kerkuar per butoni qe te beje save raportin"

    save2 = image_recognition(image, error_message, 0.8)
    pyautogui.moveTo(save2, duration = 0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('left')
    time.sleep(0.2)
    pyautogui.press('enter')
   
#fundi i funksioneve

image = r'C:\Users\admin.erinm\Desktop\DPMIMage\dpm_icon.PNG'
error_message = "Programi eshte duke kerkuar per ikonen DPM"
dpm_location = image_recognition(image, error_message, 0.9)
pyautogui.doubleClick(dpm_location)

image = r'C:\Users\admin.erinm\Desktop\DPMIMage\reporting.PNG'
error_message = "Programi eshte duke kerkuar per butonin Reporting te DPM"
rep_location = image_recognition(image, error_message, 0.5)

#mund te shtosh dhe nje opsion per timeout
pyautogui.moveTo(rep_location, duration = 1)   
pyautogui.click()

imglist = [r'C:\Users\admin.erinm\Desktop\DPMIMage\disk.PNG',
           r'C:\Users\admin.erinm\Desktop\DPMIMage\Recovery.PNG',
           r'C:\Users\admin.erinm\Desktop\DPMIMage\recovery_point.PNG',
           r'C:\Users\admin.erinm\Desktop\DPMIMage\status.PNG',
           r'C:\Users\admin.erinm\Desktop\DPMIMage\tape_manage.PNG',
           r'C:\Users\admin.erinm\Desktop\DPMIMage\tape_util.PNG'
    ]
# blloku qe ketu e poshte do futet ne nje cikel for 6 here per raportet
for i in range(6):
    image = imglist[i]
    error_message = "Nuk po gjendet imazhi " + imglist[i]
    gjashte_icons = image_recognition(image, error_message, 0.8)

    pyautogui.moveTo(gjashte_icons, duration = 1)
    pyautogui.click()
    time.sleep(0.5)# per te qene me konsistent
    pyautogui.doubleClick()

    image = r'C:\Users\admin.erinm\Desktop\DPMIMage\content.PNG'
    error_message = "Programi eshte duke kerkuar content te " + imglist[i]
    content_location = image_recognition(image, error_message, 0.9)
    # pjesa poshte nuk do ekzekutohet 1 here
    if i == 4: #tek tape management skemi select
        time.sleep(0.5)
        pyautogui.press('enter')
    else:
        x = content_location.x
        y = content_location.y

        pyautogui.moveTo(x +100,y, duration = 0.8)
        pyautogui.click(x +100,y)

        pyautogui.moveTo(x+100 ,y+30, duration = 0.3)
        pyautogui.click(x+100,y+30)

        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter') #per rastin e e fundit qe del tabele, ne rastet e tjera enter ska funksion


    explorer_reports()
    time.sleep(0.5) #smooth transition nga explorer te dpm
    pyautogui.getActiveWindow().close()
pyautogui.alert(folder_location, 'folder location')
