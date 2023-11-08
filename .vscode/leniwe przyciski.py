# # Leniwe przyciski.  Demonstruje tworzenie przycisków

# from tkinter import*

# #tworzneie głownego okna
# root = Tk()
# root.title = ("Leniwe przyciski")
# root.geometry("300x90")

# #ramka dla i na inne widgety
# app = Frame(root)
# app.grid()

# #utworzenie przycisku w ramce

# bttn1 = Button(app, text = "Nic nie robie")
# bttn1.grid()

# #utworzenie drugiego przycisku w ramce

# bttn2 = Button(app)
# bttn2.grid()
# bttn2.configure(text="ja tez nic nie robie")

# #utworzenie trzeciego przycisku w ramce

# bttn3 = Button(app)
# bttn3.grid()
# bttn3["text"]=("ja tez nic nie robie jak dwaj pozostali")

# #uruchomienie petli zdarzen okna glownego
# root.mainloop()

###############################
# #############Leniwe przyciski 2. 
# Demonstruje tworzenie przycisków przy użyciu klas
######################################################

from tkinter import*

#tworzneie głownego okna przy uzyciu kalsy

class Application(Frame):
    # """ Aplikacja oparta na GUI z trzema przyciskami. """

    ##zdefinowaeni konstruktora w klasie application

    def __init__(self, master):
        """inicjalizacja ramki"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utworzenie 3 przycisków które nic nie robią"""
        #pierwszy przycisk
        self.bttn1 = Button(self, text = "nic nie robie")
        self.bttn1.grid()
        
        #drugi przycisk
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "ja tez nic nie robie")
        
        #trzeci przycisk
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "tez nic nie robie jak ci dwaj przede mna"
    
#czesc glowna
root = Tk()
root.title("Leniwe przyciski 2")
root.geometry("300x200")
app = Application(root)
root.mainloop()
