from input import input
from input import startVal
from input import vals
from input import valMin
from input import valMax

currentVal = startVal
for val in input:
    action = val[0]
    clicks = int(val[1:]) % valMax

    if action == "L":
        # Soustraction
        currentVal = currentVal - clicks
        if currentVal < valMin:
            currentVal = currentVal + valMax

    if action == "R":
        # Addition
        currentVal = currentVal + clicks
        if currentVal >= valMax:
            currentVal = currentVal - valMax

    if currentVal == 0:
        cpt = cpt + 1

    vals.append(currentVal)

print(vals)
print(cpt)
