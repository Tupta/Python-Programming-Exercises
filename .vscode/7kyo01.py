#! python

#DESCRIPTION:
# Simply find the closest value to zero from the list. 
# Notice that there are negatives in the list.
# List is always not empty and contains only integers. Return None 
# if it is not possible to define only one of such values. 
# And of course, we are expecting 0 as closest value to zero.

# Examples:
# [2, 4, -1, -3]  => -1
# [5, 2, -2]      => None
# [5, 2, 2]       => 2
# [13, 0, -6]     => 0

def closest_to_zero(lst):
    if not lst:  # Sprawdzenie, czy lista nie jest pusta
        return None

    # Rozwijanie zagnieżdżonych list
    flat_list = []
    for sublist in lst:
        if isinstance(sublist, list):
            flat_list.extend(sublist)
        else:
            flat_list.append(sublist)

    closest_values = sorted(set(flat_list), key=lambda x: (abs(x), flat_list.count(x)))

    if len(closest_values) == 1:  # Jeśli jest tylko jedna najbliższa wartość, zwracamy ją
        return closest_values[0]
    elif abs(closest_values[0]) == abs(closest_values[1]):  # Sprawdzenie, czy istnieje więcej niż jedna najbliższa wartość
        return None
    else:
        return closest_values[0]  # W przeciwnym razie zwracamy najbliższą wartość

########################poniżej skrocona wersja :):):)
def closest(lst):
    m = min(lst, key=abs)
    return m if m == 0 or -m not in lst else None

