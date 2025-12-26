# Adevent of code 2025 Day 2
from input import input

# Convertit une chaine de caractère en tableau de valeur
# Les valeurs sont séparées par ',' 
def convertInputInTable(inputVals):
    inputTable = []

    i = 0
    str = ""
    for i in range(len(inputVals)):
        char = input[i]
        if char == ",":
            inputTable.append(str)
            str = ""
        else:
            str += char

    inputTable.append(str)
    return inputTable

# Fait la somme des valeurs du tableau en paramètre
def addingInvalids(invalidsIds):
    print("nb ids:" + str(len(invalidIds)))
    print(invalidIds)
    res = 0
    for id in invalidIds:
        res += int(id)    
    
    return res

# MAIN

invalidIds = []

inputTable = convertInputInTable(input) 
for val in inputTable:
    
    print(str(inputTable.index(val)) + "/" + str(len(inputTable)))
    
    indexMiddle = val.index('-')
    startVal = val[:indexMiddle]
    endVal = int(val[indexMiddle+1:])
    
    currentVal = int(startVal)

    while currentVal <= endVal:
        strCurrentVal = str(currentVal)
        size = len(strCurrentVal)
        middle = int(size/2)
        
        # Contrôle via des tailles de paquet
        for i in range(1, middle + 1):
 
            toCompare = str(currentVal)[:i]
            invalidIdRepeat = True
            
            # Si le nombre de paquet ne couvre pas toute la valeur on pas à la taille de paquet suivant
            if size % i > 0:
                continue
            
            nbPaquet = int(size/i)
            
            # On vérifie que chaque paquet est identique
            for j in range(1, nbPaquet):
                startIndex = j*i
                compare = strCurrentVal[startIndex:startIndex + i]
                invalidIdRepeat = toCompare == compare

                # Si le paquet est différent on break pour passer à la taille de paquet suivant
                if invalidIdRepeat == False:
                    break
            # Si une taille de pacquet se repète alors on l'ajoute à la liste des ids invalides 
            # On break pour passer à la valeur suivante
            if invalidIdRepeat:
                invalidIds.append(strCurrentVal)
                break
        currentVal += 1

# Résultat
print(addingInvalids(invalidIds))

