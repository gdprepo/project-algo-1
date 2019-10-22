print ('-------------Bienvenue---------------')
print ('----------Liste des villes-----------')
print ('-----[Bordeaux, Paris, Marseille]----')
print ('-------------------------------------')
print ('Veuillez entrer la ville de depart : ')
depart = input()
print ('Veuillez entrer la ville d arrivée : ')
arrive = input()

def set_time(distance) :
    distance = int(distance)
    check_time = 9
    check_dist = 6
    res = 0
    minute = 0

    while (check_dist + 6 < distance) :
        if (check_time % 120 == 0) :
            check_time += 20
            check_dist += 12
        elif (check_time + 10 != distance - 6):
            check_time = check_time + 60/90
        check_dist += 1

    check_time = round(check_time + 9)
    res = '{:02d}/{:02d}'.format(*divmod(check_time, 60))

    return res

def set_tab(depart, arrive) :
    distance = 0
    temps = 0
    if (depart == "Bordeaux" and arrive == "Paris" or depart == "Paris" and arrive == "Bordeaux") :
        distance = "582"
    elif (depart == "Bordeaux" and arrive == "Marseille" or depart == "Marseille" and arrive == "Bordeaux") :
        distance = "646"
    elif (depart == "Paris" and arrive == "Marseille" or depart == "Marseille" and arrive == "Paris") :
        distance = "773"
    else :
        print("Erreur: Choisir un ville dans la liste.. Relancer le programme.")
        exit()

    temps = set_time(distance)

    tableau=[["Depart","Arrive","Distance","Temps"],[depart,arrive,distance,temps]]
    forma="{0:10} | {1:10} | {2:10} | {3:10}"
    for valeur in tableau:
        print (forma.format(*valeur))

set_tab(depart, arrive)
