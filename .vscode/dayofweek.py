#!python
# 


dayofweek =int(input("Podaj dzień tygodnia według zasady poniedziałek = 1, a niedziela = 7\n"))

if dayofweek == 1:
    print("Mamy poniedziałek")
elif dayofweek == 2:
     print("Mamy wtorek")
elif dayofweek == 3:
     print("Mamy środę")
elif dayofweek == 4:
     print("Mamy czwartek")
elif dayofweek == 5:
     print("Mamy piątek")
elif dayofweek == 6:
     print("Mamy sobotę")
elif dayofweek == 7:
     print("Mamy niedzielę")
                        
if dayofweek in (6,7):
    print ("MAMY WEEKEND")
else:
    print("dzisiaj idziesz do pracy")