from graphics import *
import time
import random

def Main():
    win = GraphWin("TBF", 960, 540)
    win.setBackground("black")

    Title_Screen_Image = Image(Point(480, 270), "Title_Screen.png")
    Title_Screen_Image.draw(win)

    while True:
        click_point = win.getMouse()
        if (0 <= click_point.getX() <= 960) and (0 <= click_point.getY() <= 540):
            Title_Screen_Image.undraw()
            break

    Opening_Scene_Image = Image(Point(480, 270), "Opening_Scene.png")
    Opening_Scene_Image.draw(win)

    Opening_Scene_Player_Image = Image(Point(325, 270), "Opening_Scene_Eyes.png")
    Opening_Scene_Player_Image.draw(win)

    Opening_Scene_Count = 0
    while True:
        check_right = win.checkKey()
        if check_right == "Right" or "D" and Opening_Scene_Count <= 11:
            Opening_Scene_Player_Image.move(50, 0)
            time.sleep(1)
            Opening_Scene_Count += 1
        elif check_right == "Right" or "D" and Opening_Scene_Count > 11:
            Opening_Scene_Image.undraw()
            Opening_Scene_Player_Image.undraw()
            break
    
    Opening_Scene_Exit_Image = Image(Point(480, 270), "Opening_Scene_Exit.png")
    Opening_Scene_Exit_Image.draw(win)
    time.sleep(5)
    Opening_Scene_Exit_Image.undraw()

    Base_World_Image = Image(Point(480, 270), "Base_World.png")
    Base_World_Image.draw(win)

    Frame_1_Image = Image(Point(480,270), "Frame_1.png")
    Frame_1_Image.draw(win)

    Player_World = Image(Point(80, 480), "Player_World_Still_Right.png")
    Player_World.draw(win)

    while True:
        match win.checkKey():
            case "W":
                Player_World.move(0, -40)
                time.sleep(0.65)
            case "A":
                Player_World.move(-40, 0)
                time.sleep(0.5)
            case "S":
                Player_World.move(0, 40)
                time.sleep(0.5)
            case "D":
                Player_World.move(40, 0)
                time.sleep(0.5)
            case "Up":
                Player_World.move(0, -40)
                time.sleep(0.65)
            case "Left":
                Player_World.move(-40, 0)
                time.sleep(0.5)
            case "Down":
                Player_World.move(0, 40)
                time.sleep(0.5)
            case "Right":
                Player_World.move(40, 0)
                time.sleep(0.5)

if __name__ == "__main__":
    Main()