import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Losowy wybór dwór cyfr.
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        # Odpowiedź prawidłowa jest obsługiwana przez argument allowRegexes.
        # Odpowiedź nieprawidłowa jest obsługiwana przez argument blockRegexes
        # i odpowiedni komunikat.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Źle!')],
                              timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Czas minął!')
    except pyip.RetryLimitException:
        print('Zbyt wiele prób!')
    else:
        # Ten blok będzie wykonany, jeśli w bloku try nie zostanie zgłoszony żaden wyjątek.
        print('Dobrze!')
        correctAnswers += 1
    time.sleep(1)  # Krótka przerwa pozwalająca użytkownikowi na przeczytanie komunikatu.
print('Wynik: %s / %s' % (correctAnswers, numberOfQuestions))
