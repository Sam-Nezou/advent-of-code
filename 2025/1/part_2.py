from input import input
from input import startVal
from input import vals
from input import valMin
from input import valMax
from input import cpt

currentVal = startVal
input_2 = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
for val in input_2:
    action = val[0]
    clicks = int(val[1:])
    # Récupération du nombre de rotation
    nbRotation = int(clicks / valMax)
    if nbRotation > 1:
        cpt += nbRotation

    clicks = clicks % valMax

    if action == "L":
        # Soustraction
        print(currentVal)
        currentVal = currentVal - clicks
        if currentVal < valMin:
            print(currentVal)
            currentVal = currentVal + valMax
            print(currentVal)
            if currentVal != 0:
                cpt += 1
            print("depasse")

    if action == "R":
        # Addition
        print(currentVal)

        currentVal = currentVal + clicks
        if currentVal >= valMax:
            print(currentVal)

            currentVal = currentVal - valMax
            print(currentVal)
            if currentVal != 0:
                cpt += 1
            print("dessous")

    if currentVal == 0:
        cpt = cpt + 1

    vals.append(currentVal)

print(vals)
print(cpt)
