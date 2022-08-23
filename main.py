import cmd
from ppadb.client import Client as AdbClient
from time import sleep
import random
import pyautogui
#ld player adb 0 = 5555 1 =5557 2 =5559
deviceport = 5555    #블루스택 번호_정의
target_x = 1469      #몬스터 선택 x,y중간값 좌표
target_y = 624
common_x = 1354
common_y = 702
common_time = 1
skill_x = 1180
skill_y = 697
def random_click(target_x,target_y,time):                          #매크로 의심을 피하기 위한 랜덤위치 터치
    sleep(int(time))
    rand_x = random.randint((target_x-10),(target_x+10))
    rand_y = random.randint((target_y-10),(target_y+10))
    touch = "input touchscreen tap " + str(rand_x) + " " + str(rand_y)
    adbdevice.shell(touch)

def input_swipe(x,y,xx,yy):
    touch = "input touchscreen swipe " + str(x) + " " + str(y) + " " + str(xx) + " " + str(yy)
    adbdevice.shell(touch)
def combo1():
    for i in range(4):
        random_click(common_x, common_y, common_time)
    check_monster()
def combo2():
    for i in range(4):
        random_click(common_x,common_y,common_time)
    check_monster()
def combo3():
    random_click(skill_x,skill_y,0)
    random_click(skill_x,skill_y,0)
    random_click(common_x,common_y,common_time)
    random_click(common_x, common_y,common_time)
    random_click(common_x,common_y,common_time)
    check_monster()

def combo4():
    random_click(common_x,common_y,0)
    random_click(skill_x,skill_y,0)
    random_click(common_x,common_y,common_time)
    random_click(common_x,common_y,common_time)
    random_click(common_x,common_y,common_time)
    check_monster()
def avoid():
    for i in range(4):
        input_swipe(970, 330, 620, 330)
    for j in range(10):
        input_swipe(223, 728, 234, 185)
def check_monster():
    sleep(0.1)
    save_img = pyautogui.screenshot()
    coyote_img1 = pyautogui.locate("coyotelv1.png",save_img,confidence=0.8)
    coyote_img2 = pyautogui.locate("coyote_last.png",save_img,confidence=0.7)
    bear_img3 = pyautogui.locate("bearlv3.png",save_img,confidence=0.8)
    bear_img4 = pyautogui.locate("bearlv4.png",save_img,confidence=0.8)
    dont_att = pyautogui.locate("avoid.png",save_img,confidence=0.8)
    check_coyote = pyautogui.locate("target.png",save_img,confidence=0.5)
    if dont_att is not None:
        avoid()
    elif coyote_img1 is not None:
        if check_coyote is not None:
            for i in range(10):
                input_swipe(223, 728, 234, 185)
                check_monster()
        else :
            combo1()

    elif coyote_img2 is not None:
        combo2()

    elif bear_img3 is not None:
        combo3()

    elif bear_img4 is not None:
        combo4()

#adb 설정
client = AdbClient(host="127.0.0.1", port=5037)
client.remote_connect("localhost", int(deviceport))
adbdevice = client.device("localhost:"+str(deviceport))
client.remote_connect("localhost", int(5557))
adbdevice = client.device("localhost:"+str(5557))

if adbdevice is not None:
    print("Adb detected")

else:
    print("Adb not detected")
    exit(0)


while True:
    end = int(input("프로그램 계속 진행\n1.진행 \n2.종료"))
    if end==1:
        for i in range(5):
            for i in range(20):
                input_swipe(223,728,234,185)

            random_click(target_x, target_y, 0)
            check_monster()
            input_swipe(970, 330, 620, 330)

    elif end==2:
        exit(0)
    else :
        print("재입력 필요")


