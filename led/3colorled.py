#coding: utf-8

#import GPIO, time , sys
import RPi.GPIO as GPIO
import time
import sys

#set pin with Board Mode
R,G,B = 12,16,18
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

#initial pin in/out
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

#set PWM to tuning
pR = GPIO.PWM(R, 60)
pG = GPIO.PWM(G, 60)
pB = GPIO.PWM(B, 60)


#start radio
pR.start(0)
pG.start(0)
pB.start(0)

#Red is On during 2 sec.
pR.ChangeDutyCycle(100)
pG.ChangeDutyCycle(0)
pB.ChangeDutyCycle(0)
time.sleep(2)

# 替换为绿灯亮2秒
pR.ChangeDutyCycle(0)
pG.ChangeDutyCycle(100)
pB.ChangeDutyCycle(0)
time.sleep(2)

# 替换为靛色灯亮2秒
pR.ChangeDutyCycle(0)
pG.ChangeDutyCycle(0)
pB.ChangeDutyCycle(100)
time.sleep(2)

# 定义要闪烁的时间 这里定义为10秒
endtime = 216
currenttime = 0

# 开始进行炫彩闪烁
while True:
    try:
        # 通过占空比控制红色的占比
        for r in range(0, 101, 20):
            pR.ChangeDutyCycle(r)
            # 通过占空比控制绿色的占比
            for g in range(0, 101, 20):
                pG.ChangeDutyCycle(g)
            # 空通过占空比控制蓝色的占比
                for b in range(0, 101, 20):
                    pB.ChangeDutyCycle(b)
                    time.sleep(0.1)
                    currenttime += 1
                    
                    # 结束程序
                    if (currenttime > endtime):
                        pR.stop()
                        pG.stop()
                        pB.stop()
    except KeyboardInterrupt:
        break
GPIO.cleanup()
sys.exit(0)