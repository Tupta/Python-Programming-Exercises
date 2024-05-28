import pyautogui, time
print('5 sekund do rozpoczęcia działania')
pyautogui.LOG_SCREENSHOTS = True
pyautogui.LOG_SCREENSHOTS_LIMIT = 100
time.sleep(5)
pyautogui.click()    # Kliknięcie w celu aktywacji programu.
distance = 300
shrink = 20
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)   # Przesunięcie kursora myszy w prawo.
    distance = distance - shrink
    pyautogui.dragRel(0, distance, duration=0.1)   # Przesunięcie kursora myszy w dół.
    pyautogui.dragRel(-distance, 0, duration=0.1)  # Przesunięcie kursora myszy w lewo.
    distance = distance - shrink
    pyautogui.dragRel(0, -distance, duration=0.1)  # Przesunięcie kursora myszy w górę.
