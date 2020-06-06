import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time



def isCollide(data):
    
    for i in range(300, 500):
        for j in range(562, 650):
            if data[i, j] < 100:
                pyautogui.press('up')
                return
    
    # Draw the rectangle for birds
    for i in range(300, 575):
        for j in range(410, 562):
            if data[i, j] < 100:
                pyautogui.press('down')
                return
    return

    

if __name__ == "__main__":
    print(" Dino game about to start in 2 seconds ")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        
       # Draw the rectangle for cactus
        # for i in range(300, 500):     #(width of rect in left direction, width of rect in right direction)
        #     for j in range(562, 650):  #(height of rectangle,space from bottom of floor)
        
        #         data[i, j] = 0
        # # Draw the rectangle for birds
        # for i in range(300, 575):
        #     for j in range(410, 562):
        #         data[i, j] = 171

        # image.show()
        # break
      

