#!python

# Szyfrator
# Szyfruje twój tekst wybranym szyfrem

from tkinter import *

class Application(Frame):
    """
    Aplikacja z GUI, która szyfruje wiadomość
    wprowadzoną przez użytkownika.
    """
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez
        użytkownika 
        """
        # utwórz etykietę z instrukcją
        Label(self,
              text="\n\nDawno, dawno temu przygotowywałem zabawy na urodziny syna. W związku z tym musiałem przygotować kilka zaszyfrowanych wiadomości.\nA że robiłem to ręcznie, to zajęło mi to mnóstwo czasu. \nI stąd właśnie pomysł na ten program"
              ).grid(row=0, column=0, columnspan=2, sticky=E)

        # utwórz etykietę i pole znakowe służące do wpisania tekstu do zaszyfrowania
        Label(self,
              text="Wprowadź tekst który chcesz zaszyfrować: "
              ).grid(row=4, column=0, columnspan=20, sticky=W)
        self.person_ent = Entry(self, width=95,)
        self.person_ent.grid(row=5, column=0, columnspan=4)

        # utwórz etykietę do pól wyboru szyfru
        Label(self,
              text="Wybierz szyfr:"
              ).grid(row=6, column=0, sticky=W)

        # utwórz pole wyboru szyfru 'GADERYPOLUKI'
        self.GADERYPOLUKI = BooleanVar()
        Checkbutton(self,
                    text="GADERYPOLUKI",
                    variable=self.GADERYPOLUKI
                    ).grid(row=7, column=0, sticky=W)

        # utwórz pole wyboru szyfru 'MALINOWEBUTY'
        self.MALINOWEBUTY = BooleanVar()
        Checkbutton(self,
                    text="MALINOWEBUTY",
                    variable=self.MALINOWEBUTY
                    ).grid(row=8, column=0, sticky=W)

        # utwórz pole wyboru szyfru 'WOJNAOCHMURY'
        self.WOJNAOCHMURY = BooleanVar()
        Checkbutton(self,
                    text="WOJNAOCHMURY",
                    variable=self.WOJNAOCHMURY
                    ).grid(row=9, column=0, sticky=W)

        # utwórz przycisk akceptacji danych
        Button(self,
               text="Kliknij, aby wyświetlić zaszyfrowany tekst",
               command=self.encryptmessage
               ).grid(row=10, column=0, sticky=W)

        # utwórz pole tekstowe do wyświetlenia zaszyfrowanej wiadomości
        self.encrypt_message_text = Text(self, width=75, height=10, wrap=WORD)
        self.encrypt_message_text.grid(row=11, column=0, columnspan=4)

    def custom_replace(self, text):
        replacements = {
            'g': 'a',
            'a': 'g',
            'd': 'e',
            'e': 'd',
            'r': 'y',
            'y': 'r',
            'p': 'o',
            'o': 'p',
            'l': 'u',
            'u': 'l',
            'k': 'i',
            'i': 'k'
        }
        

        result = ""
        for char in text:
            if char in replacements:
                result += replacements[char]
            else:
                result += char
        return result

    def encryptmessage(self):
        # Pobierz tekst wprowadzony przez użytkownika
        input_text = self.person_ent.get()

        # Wykonaj niestandardową zamianę liter
        encrypted_message = self.custom_replace(input_text)

        # Wyświetl zaszyfrowaną wiadomość
        self.encrypt_message_text.delete(1.0, END)  # Wyczyść zawartość pola tekstowego
        self.encrypt_message_text.insert(1.0, encrypted_message)  # Wstaw zaszyfrowaną wiadomość


# Część główna
root = Tk()
root.title("SZYFRATOR")
app = Application(root)
root.mainloop()
