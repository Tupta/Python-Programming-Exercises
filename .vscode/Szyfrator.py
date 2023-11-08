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
        użytkownika i wyświetlenia opowiadania.
        """
        # utwórz etykietę z instrukcją
        Label(self,
              text = "\n\nDawno, dawno temu przygotowywałem zabawy na urodziny syna. W związku z tym musiałem przygotować kilka zaszyfrowanych wiadomości.\nA że robiłem to ręcznie, to zajęło mi to mnóstwo czasu. \nI stąd właśnie pomysł na ten program"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = E)

        # utwórz etykietę i pole znakowe służące do wpisania tekstu do zaszyfrowania
        Label(self,
              text = "Wprowadź tekst który chcesz zaszyfrować: "
              ).grid(row = 4, column = 0, sticky = W)
        self.person_ent =  Entry(self)
        self.person_ent.grid(row = 4, column = 1, sticky = W)
          
        # utwórz etykietę do pól wyboru szyfru
        Label(self,
              text = "Wybierz szyfr:"
              ).grid(row = 5, column = 0, sticky = W)

        # utwórz pole wyboru szyfru 'GADERYPOLUKI'
        self.GADERYPOLUKI = BooleanVar()
        Checkbutton(self,
                    text = "GADERYPOLUKI",
                    variable = self.GADERYPOLUKI
                    ).grid(row = 6, column = 1, sticky = W)

        # utwórz pole wyboru szyfru 'MALINOWEBUTY'
        self.MALINOWEBUTY = BooleanVar()
        Checkbutton(self,
                    text = "MALINOWEBUTY",
                    variable = self.MALINOWEBUTY
                    ).grid(row = 7, column = 1, sticky = W)

        # utwórz pole wyboru szyfru 'WOJNAOCHMURY'
        self.WOJNAOCHMURY = BooleanVar()
        Checkbutton(self,
                    text = "WOJNAOCHMURY",
                    variable = self.WOJNAOCHMURY
                    ).grid(row = 8, column = 1, sticky = W)

          # utwórz przycisk akceptacji danych
        Button(self,
               text = "Kliknij, aby wyświetlić zaszyfrowany tekst",
               command = self.encryptmessage
               ).grid(row = 9, column = 0, sticky = W)

        encryptmessage = Text(self, width = 75, height = 10, wrap = WORD)
        encryptmessage.grid(row = 10, column = 0, columnspan = 4)
        
    def encryptmessage(self):
        """ Z. """
        # pobierz wartości z interfejsu GUI
        Text = person_ent.get()
        
        encryptmessage = ""
        if self.GADERYPOLUKI.get():
            encryptmessage == Text.replace('g', 'd', 'r', 'p', 'l','k' ).replace('a', 'e', 'y', 'o', 'u','i' )
        if self.MALINOWEBUTY.get():
            encryptmessage == Text.replace('g', 'd', 'r', 'p', 'l','k' ).replace('a', 'e', 'y', 'o', 'u','i' )
        if self.WOJNAOCHMURY.get():
            encryptmessage == Text.replace('g', 'd', 'r', 'p', 'l','k' ).replace('a', 'e', 'y', 'o', 'u','i' )
        
           
        # wyświetl zaszyfrowaną wiadomosć                                
        encryptmessage.delete(0.0, END)
        encryptmessage.insert(0.0, encryptmessage)

# część główna
root = Tk()
root.title("SZYFRATOR")
app = Application(root)
root.mainloop()



# tekst = "To jest przykładowy tekst z literami a i g."
# encrypt_message = tekst.replace('a', 'd').replace('g', 'h')
# print(tekst_zmieniony)
