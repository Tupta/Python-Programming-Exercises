
import random, string

x = input("Podaj z ilu znaków ma skłądać się twoje hasło:")
while not x.isnumeric():
    print("Nie podano poprawnej liczby. Spróbuj ponownie.")
    x = input("Podaj z ilu znaków ma skłądać się twoje hasło:")
print(x)
password = "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(int(x))])
print("twoje hasło to:\n"+password)
