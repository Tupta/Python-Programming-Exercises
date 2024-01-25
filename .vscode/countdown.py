#! python3

#countdown.py - skrypt odliczający czas

import time, subprocess

timeLeft = 60

while timeLeft > 0 :
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
    
#Todo - odtworzenie dzwięku po skończeniu odliczania

subprocess.Popen(['start', 'alarm.wav'], shell=True)

    