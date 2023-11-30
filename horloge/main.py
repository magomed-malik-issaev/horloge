import time

def afficher_heure(heure):
    while True:
        heure_actuelle = time.localtime()
        heure = heure_actuelle.tm_hour
        minute = heure_actuelle.tm_min
        seconde = heure_actuelle.tm_sec
        heure_formattee = f"{heure:02d}:{minute:02d}:{seconde:02d}"
        print(heure_formattee, end='\r', flush=True)
        time.sleep(1)

def regler_heure():
    heures = int(input("Entrez l'heure : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    heure = (heures, minutes, secondes)
    print("Heure réglée avec succès.")
    return heure

def regler_alarme():
    heures = int(input("Entrez l'heure de l'alarme : "))
    minutes = int(input("Entrez les minutes de l'alarme : "))
    secondes = int(input("Entrez les secondes de l'alarme : "))
    alarme = (heures, minutes, secondes)
    print("Alarme réglée avec succès.")
    return alarme

def verifier_alarme(heure_actuelle, alarme):
    if heure_actuelle == alarme:
        print("L'heure de l'alarme est atteinte !")

try:
    heure = regler_heure()
    alarme = regler_alarme()
    afficher_heure(heure)
    while True:
        heure_actuelle = time.localtime()
        verifier_alarme(heure_actuelle, alarme)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nArrêt du programme.")