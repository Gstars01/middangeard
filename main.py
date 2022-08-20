import cmd
from ppadb.client import Client as AdbClient
from time import sleep
import random

deviceport = 5555    #블루스택 번호_정의
target_x = 1469      #몬스터 선택 x,y중간값 좌표
target_y = 624

def random_click(target_x,target_y):                          #매크로 의심을 피하기 위한 랜덤위치 터치
    rand_x = random.randint((target_x-15),(target_x+15))
    rand_y = random.randint((target_y-15),(target_y+15))
    touch = "input touchscreen tap " + str(rand_x) + " " + str(rand_y)
    adbdevice.shell(touch)

def use_skill():
    random_click(target_x, target_y)
    random_click(1354, 700)
    random_click(1183, 696) #스킬
    random_click(1354, 700)
    sleep(0.8)
    random_click(1354, 700)
    sleep(0.8)
    random_click(1354, 700)
    sleep(0.8)
    random_click(1354, 700)
    sleep(1.7)

#adb 설정
client = AdbClient(host="127.0.0.1", port=5037)
client.remote_connect("localhost", int(deviceport))
adbdevice = client.device("localhost:"+str(deviceport))

if adbdevice is not None:
    print("Adb detected")

else:
    print("Adb not detected")
    exit(0)


for i in range(2):
    use_skill()


