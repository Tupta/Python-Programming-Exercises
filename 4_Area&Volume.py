#!python

# 4_Area&Volume
#Area, perimeter, volume, 
# and surface area are straightforward calculations.

def area(L,W):
    area=L*W
    return area

def perimeter(L,W):
    perimeter=(L+W)*2
    return perimeter

def volume(L,W,H):
    volume=L*W*H
    return volume

def surfaceArea(L,W,H):
    surfaceArea=(L*W*2)+(L*H*2)+(W*H*2)
    return surfaceArea


#Asserational functions

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340    

print("All tests passed!")

