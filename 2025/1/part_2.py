from input import input
from input import startVal
from input import vals
from input import valMin
from input import valMax
from input import cpt

currentVal = startVal
for val in input:
    action = val[0]
    clicks = int(val[1:])
    # Récupération du nombre de rotation
    nbRotation = int(clicks / valMax) 
    if nbRotation >= 1:
        cpt += nbRotation

    clicks = clicks % valMax
    lastValue = currentVal
    if action == "L":
        # Soustraction
        currentVal = currentVal - clicks
        if currentVal < valMin :
            currentVal = currentVal + valMax
            if  (lastValue != 0) & (currentVal != 0):
                cpt += 1

    if action == "R":
        # Addition
        currentVal = currentVal + clicks
        if currentVal >= valMax:
            currentVal = currentVal - valMax
            if (lastValue != 0) & (currentVal != 0):
                cpt += 1

    if currentVal == 0:
        cpt = cpt + 1

    vals.append(currentVal)

print(cpt)
