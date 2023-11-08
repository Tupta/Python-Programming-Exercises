# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys

score == 0

def open_file(file_name, mode):
    """Otwórz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n", e)
        input("\n\nAby zakończyć program, naciśniej klawisz Enter.")
        sys.exit()
    else: 
        return the_file

def next_line(the_file):
        """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
        line = the_file.readline()
        line = line.replace("/", "\n")
        return line

def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz"""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    anserw = []
    for i in range(4):
        anserw.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explantation = next_line(the_file)
    
    return category, question, anserw, correct, explantation

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwe"""
    print("\t\t Witaj w turnieju wiedzy!!!\n")
    print("\t\t", title, "\n")
    
def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

#pobierz pierwszy blok

category, question, anserw, correct, explanatation = next_block(trivia_file)
while category:
    #zadaj pytanie
    print(category)
    print(question)
    for i in range(4):
        print("\t", i + 1, "-" answers[i])
    
    #uzyskaj odpowiedź
    cor_answer = input("jaka jest Twoja odpowiedź?")
    
    #sprawdź odpowiedź
    if cor_answer == correct:
        print("\nTo jest prawidłowa odpowiedź!", end=" ")
        score += 1
    else:
        print("\nTo jest zła odpowiedź", end=" ")
        print(explanatation)
        print("Wynik:", score,"\n\n")
    
    #pobierz kolejny blok
    category, question, anserw, correctc explanatation = next_block(trivia_file)
    
    trivia_file.close()
    print("to było ostatnie pytanie")
    print("twój końcowy wynik:", score)
    
    
    main()
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
    