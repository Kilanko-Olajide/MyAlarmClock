import time
import datetime
import pygame

def set_alarm(alarmtime):
    print(f"The alarm is set for {alarmtime}")
    sound_file = "Ayra-Starr-Ft-Anitta-and-Coco-Jones-Woman-Commando-(TrendyBeatz.com).mp3"
    starter = True 

    while starter:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currenttime)
        if currenttime == alarmtime:
            print("WAKE UP!!! 😉😉")

            starter = False
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)
        
if __name__ == "__main__":
    alarmtime = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarmtime) 
