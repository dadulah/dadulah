import time 
import datetime 
import pygame


def alarm(alarm_time):
    music_file = "/storage/emulated/0/Documents/Pydroid3/alarm.mp3"
    print(f"Alarm set for {alarm_time}")
    is_running = True
    
    
    while is_running:
        now = datetime.datetime.now().strftime("%H:%M:%S")
          
        
        if now == alarm_time:
            print("wake up")
            pygame.mixer.init()
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()
    
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
            continue
            
        if now  >  alarm_time:
            print("Set a valid alarm!")
            is_running = False
            continue
             
        print(now)         
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    alarm(alarm_time)
