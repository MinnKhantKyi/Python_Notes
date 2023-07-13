# Need to pip install playground==1.2.2 
from playsound import playsound
import time

SOUND : str = "Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3"
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):

    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        second_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm sound in {minute_left:02d}:{second_left:02d} ")

    playsound(SOUND)

if __name__ == "__main__":
    
    while True:
        print("Enter -1 to exit")
        minutes = int(input("Minutes to wait > "))
        
        if minutes == -1:
            break
        else:
            seconds = int(input("Seconds to wait > "))
            total_timer = minutes * 60 + seconds
            alarm(total_timer)
