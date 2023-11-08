from tkinter import*

class Application(Frame):
    def __init__(self, master):
        """Tworzy ramkę główną okna"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """Tworzymy zawartość okna - wszystko co jest w środku"""
        # Tworzymy etykietę z instrukcją
        self.inst_lbl = Label(self, text="Wybierz i zaznacz potrawy, które chciałbyś zamówić")
        self.inst_lbl.grid(row=1, column=3, columnspan=3, sticky=W)
        Label(self, text="DZISIAJ W MENU MAMY DO WYBORU:").grid(row=1, column=5, sticky=W)
        
        ################################################## PRZYSTAWKI ###################################
        Label(self, text="PRZYSTAWKI:").grid(row=2, column=2, sticky=W)
                                  
        # utwórz pole wyboru przystawka 1
        self.przystawka_1 = BooleanVar()
        Checkbutton(self, text="przystawka_1", 
                    variable=self.przystawka_1, 
                    command=self.update_price
                    ).grid(row=3, column=2, sticky=W)

        # utwórz etykietę z ceną przystawka_1
        self.przystawka_1_lbl = Label(self, text="2 zł")
        self.przystawka_1_lbl.grid(row=3, column=5, sticky=W)
         
        # utwórz pole wyboru przystawka_2
        self.przystawka_2 = BooleanVar()
        Checkbutton(self, text="Przystawka_2", 
                    variable=self.przystawka_2, 
                    command=self.update_price).grid(row=4, column=2, sticky=W)

        # utwórz etykietę z ceną przystawka_2
        self.przystawka_2_lbl = Label(self, text="4 zł")
        self.przystawka_2_lbl.grid(row=4, column=5, sticky=W)
         
        # utwórz pole wyboru przystawka_3
        self.przystawka_3 = BooleanVar()
        Checkbutton(self,
                     text = "przystawka_3",
                     variable = self.przystawka_3,
                     command = self.update_price
                     ).grid(row = 5, column=2, sticky=W)

         # utwórz etykietę z ceną przystawka_3
        self.przystawka_3_lbl = Label(self, text="7 zł")
        self.przystawka_3_lbl.grid(row=5, column=5, sticky=W)
         
         # utwórz pole wyboru przystawka_4
        self.przystawka_4 = BooleanVar()
        Checkbutton(self,
                     text = "Przystawka 4",
                     variable = self.przystawka_4,
                     command = self.update_price
                     ).grid(row = 6, column=2, sticky=W)

        # utwórz etykietę z ceną przystawki 4
        self.przystawka_4_lbl = Label(self, text="17 zł")
        self.przystawka_4_lbl.grid(row=6, column=5, sticky=W)
         
         ################################################ ZUPY ################################################
        Label(self,
               text = " NASZE ZUPY:"
               ).grid(row = 8, column = 2, sticky = W)
                                  
        # utwórz pole wyboru zupa z trupa
        self.zupa_z_trupa = BooleanVar()
        Checkbutton(self,
                     text = "Zupa z trupa",
                     variable = self.zupa_z_trupa,
                     command = self.update_price
                     ).grid(row = 9, column=2, sticky=W)

         # utwórz etykietę z ceną zupy z trupa
        self.zupa_z_trupa_cena_lbl = Label(self, text="12 zł")
        self.zupa_z_trupa_cena_lbl.grid(row=9, column=5, sticky=W)
         
         # utwórz pole wyboru zupa Barszcz
        self.zupa_barszcz = BooleanVar()
        Checkbutton(self,
                     text = "Zupa Barszcz",
                     variable = self.zupa_barszcz,
                     command = self.update_price
                     ).grid(row = 10, column=2, sticky=W)

        # utwórz etykietę z ceną zupy barszcz
        self.zupa_barszcz_cena_lbl = Label(self, text="14 zł")
        self.zupa_barszcz_cena_lbl.grid(row=10, column=5, sticky=W)
         
        # utwórz pole wyboru zupa Krupnik
        self.zupa_krupnik = BooleanVar()
        Checkbutton(self,
                     text = "Zupa Krupnik",
                     variable = self.zupa_krupnik,
                     command = self.update_price
                     ).grid(row = 11, column=2, sticky=W)

        # utwórz etykietę z ceną zupy krupnik
        self.zupa_krupnik_cena_lbl = Label(self, text="17 zł")
        self.zupa_krupnik_cena_lbl.grid(row=11, column=5, sticky=W)
         
        # utwórz pole wyboru zupa rosół
        self.zupa_rosol = BooleanVar()
        Checkbutton(self,
                     text = "Zupa Rosół",
                     variable = self.zupa_rosol,
                     command = self.update_price
                     ).grid(row = 12, column=2, sticky=W)

        # utwórz etykietę z ceną zupy rosol
        self.zupa_rosol_cena_lbl = Label(self, text="21 zł")
        self.zupa_rosol_cena_lbl.grid(row=12, column=5, sticky=W)
         
                
        ################################################ 2 danie ################################################
        Label(self,
               text = " Dania główne:"
               ).grid(row = 13, column = 2, sticky = W)
                                  
        # utwórz pole wyboru Placki po węgiersku
        self.placek_po_wegiersku = BooleanVar()
        Checkbutton(self,
                     text = "Zupa z trupa",
                     variable = self.placek_po_wegiersku,
                     command = self.update_price
                     ).grid(row = 15, column=2, sticky=W)

        # utwórz etykietę z ceną placek_po_wegiersku
        self.placek_cena_lbl = Label(self, text="18 zł")
        self.placek_cena_lbl.grid(row=15, column=5, sticky=W)
         
        # utwórz pole wyboru pizza
        self.pizza = BooleanVar()
        Checkbutton(self,
                     text = "Pizza",
                     variable = self.pizza,
                     command = self.update_price
                     ).grid(row = 16, column=2, sticky=W)

        # utwórz etykietę z ceną pizza
        self.pizza_cena_lbl = Label(self, text="15 zł")
        self.pizza_cena_lbl.grid(row=16, column=5, sticky=W)
         
        # utwórz pole wyboru Schabowy
        self.schabowy = BooleanVar()
        Checkbutton(self,
                     text = "Schabowy z dinozaura",
                     variable = self.schabowy,
                     command = self.update_price
                     ).grid(row = 17, column=2, sticky=W)

        # utwórz etykietę z ceną schabowy
        self.schabowy_cena_lbl = Label(self, text="17 zł")
        self.schabowy_cena_lbl.grid(row=17, column=5, sticky=W)
         
        # utwórz pole wyboru łazanki
        self.lazanki = BooleanVar()
        Checkbutton(self,
                     text = "Łazanki",
                     variable = self.lazanki,
                     command = self.update_price
                     ).grid(row = 18, column=2, sticky=W)

        # utwórz etykietę z ceną lazanki
        self.lazanki_cena_lbl = Label(self, text="10 zł")
        self.lazanki_cena_lbl.grid(row=18, column=5, sticky=W) 
        ######################################################################### 
                      
        # utwórz etykietę z łączną ceną zamówienia
        self.total_price_lbl = Label(self, text="Łączna cena wybranych potraw: 0 zł")
        self.total_price_lbl.grid(row=26, column=3, sticky=W)
            
         
        # utwórz przycisk 'Złóż zamówienie'
        self.submit_bttn = Button(self, text="Złóż zamówienie")
        self.submit_bttn.grid(row=26, column=5, sticky=W)
    
            
    def update_price(self):
        price = 0
        if self.przystawka_1.get():
            price += 2
        if self.przystawka_2.get():
            price += 4
        if self.przystawka_3.get():
            price += 7
        if self.przystawka_4.get():
            price += 17
        if self.zupa_z_trupa.get():
            price += 12
        if self.zupa_barszcz.get():
            price += 14
        if self.zupa_krupnik.get():
            price += 15
        if self.zupa_rosol.get():
            price += 21
        if self.placek_po_wegiersku.get():
            price += 18
        if self.pizza.get():
            price += 15
        if self.schabowy.get():
            price += 17
        if self.lazanki.get():
            price += 10

        self.total_price_lbl.config(text="Łączna cena wybranych potraw: " + str(price) + " zł")
      
    
root = Tk()
root.title("Wybierz co chciałbyś dzisiaj zjeść")
root.geometry("800x600")

app = Application(root)
root.mainloop()

