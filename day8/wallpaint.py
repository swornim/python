import math
def paint_calc(hegiht, wdith, cover):
    n = (hegiht * wdith)/cover
    n_can = math.ceil(n) 
    print(f"we need total of {n_can} cans")

test_h = int(input("height of wall:"))
test_w = int(input("width of wall: "))
coverate = 5
paint_calc(hegiht = test_h, wdith = test_w, cover = coverate)
 
