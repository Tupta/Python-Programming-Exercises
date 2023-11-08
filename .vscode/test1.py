# print ("podaj wartość zmienne")
# spam = input()
# spam = int(spam)
# if spam == 1:
#     print ("witaj")
# if spam == 2:
#         print ("nie ten argument")

# if spam >> 2:
#        print ("srututututu")



# text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth.
# On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature 
# of the Moon is 127 C."""
# print(text)

# sentences = text.split('. ')
# print(sentences)

# for sentence in sentences:
#     if 'temperature' in sentence:
#         print(sentence)

######################################################
# j = 1042 // 60
# print(j)
# d = 38 % 6
# print(d)

# print(abs(12-34))


######################################################
# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# bus_weight = 12650 # in kilograms, on Earth

# print("On Earth, a double-decker bus weighs", bus_weight, "kg")
# print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
# print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")


######################################################
# lista1 = [1000,2000,30,10,15,54,]
# lista1.sort()
# print(lista1)

# ######################################################
# countdown = [4, 3, 2, 1, 0]
# for number in countdown:
#     print(number)
# print("Blast off!! 🚀")

######################################################

# rainfall = {
#     'october': 3.5,
#     'november': 4.2,
#     'december': 2.1
# }

# for key in rainfall.keys():
#     print(f'{key}: {rainfall[key]}cm')
   ######################################################
# from datetime import timedelta, datetime

# def arrival_time(hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours)
#     return arrival.strftime("Arrival: %A %H:%M")

# x = arrival_time("Moon", hours=0.15)
# print(x)
# print (arrival_time())

#  ######################################################
 
# def sequence_time(*args):
#     total_minutes = sum(args)
#     if total_minutes < 60:
#         return f"Total time to launch is {total_minutes} minutes"
#     else:
#         return f"Total time to launch is {total_minutes/60} hours"

# x = sequence_time(4,50,20,50)   
# print(x)
# print((sequence_time(4,50,20,50)))
# print(sequence_time(1,2,3,4,5,6,6,))

  ######################################################
 
# def sequence_time(*args):
#     total_minutes = sum(args)
#     if total_minutes < 60:
#         return f"Total time to launch is {total_minutes} minutes"
#     else:
#         return f"Total time to launch is {total_minutes/60} hours"
    
# x = sequence_time(4, 14, 18)
# print(x)

  ######################################################
#def variable_length(**kwargs):
#     print(kwargs)
# x = (variable_length(tanks=1, day="Wednesday", pilots=3))
# print(x)
#variable_length(tanks=1, day="Wednesday", pilots=3
                
  ######################################################
# def crew_members(**kwargs):
#     print(f"{len(kwargs)} astronauts assigned for this mission:")
#     for title, name in kwargs.items():
#         print(f"{title}: {name}")

# crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
 
 
  ######################################################
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)
fuel_report()