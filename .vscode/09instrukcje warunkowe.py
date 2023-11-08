from contextlib import redirect_stderr


print ("Jakie jest światło? (red, green, yellow?)")

light = input()

if light =='red':
    print("czekaj")
elif light == 'yellow':
    print("przygotuj się")
elif light == 'green':
    print("jedź")
else:
    print("niewłaściwa wartość")

