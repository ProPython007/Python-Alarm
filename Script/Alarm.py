from pygame import mixer
import time

def sound():
    mixer.init()
    mixer.music.load("pubg.mp3")

def alarm():
    print("\nSet the alarm\n")
    h=int(input("Enter the hour: "))
    m=int(input("Enter the minute: "))
    print("\nSet the alarm time\n")
    z=int(input("Enter time (in sec) of playing: "))

    print("\nAlarm set for "+str(h)+":"+str(m)+"\n\n")
    while True:
        if time.localtime().tm_hour==h and time.localtime().tm_min==m:
            print("Alert!!!")
            break
    sound()
    n=1
    while n>0:
        mixer.music.play(z)
        time.sleep(z)
        n-=1
alarm()
