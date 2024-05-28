#! python3
# Automatycznie wypełnia formularz internetowy.
import pyautogui, time

formData = [{'name': 'Alicja', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Powiedz Bartkowi, że mówię mu cześć.'},
            {'name': 'Bartek', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Karol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Proszę zabrać kukiełki z pokoju.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Chronić niewinnych. Służyć społeczeństwu. Stać na straży prawa.'},
            ]

pyautogui.PAUSE = 0.5
print('Upewnij się, że okno przeglądarki WWW jest aktywne, a formularz został wczytany!')

for person in formData:
    # Umożliwienie użytkownikowi zakończenia działania skryptu.
    print('>>> 5-SEKUNDOWA PRZERWA POZWALAJĄCA UŻYTKOWNIKOWI NACISNĄĆ CTRL-C <<<')
    time.sleep(5)

    print('Wprowadzenie informacji o osobie %s...' % (person['name']))
    pyautogui.write(['\t', '\t'])

    # Wypełnienie pola Name.
    pyautogui.write(person['name'] + '\t')

    # Wypełnienie pola Greatest Fear(s).
    pyautogui.write(person['fear'] + '\t')

    # Wypełnienie pola Source of Wizard Powers.
    if person['source'] == 'wand':
        pyautogui.write(['down', '\n', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', '\n', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', '\n', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', '\n', '\t'], 0.5)

    # Wypełnienie pola RoboCop.
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t'], 0.5)

    # Wypełnienie pola Additional Comments.
    pyautogui.write(person['comments'] + '\t')

    # Kliknięcie przycisku Prześlij przez symulację naciśnięcia klawisza Enter.
    time.sleep(0.5) # Oczekiwanie na aktywowanie przycisku.
    pyautogui.press('enter')

    # Zaczekanie na wczytanie strony.
    print('Submitted form.')
    time.sleep(5)

    # Kliknięcie łącza "Submit another response".
    pyautogui.write(['\t', '\n'])
