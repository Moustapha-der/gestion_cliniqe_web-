import json
import os

# Charger les données depuis un fichier
def charger_donnees(fichier):
    if not os.path.exists(fichier):
        with open(fichier, "w") as f:
            f.write("{}")
    with open(fichier, "r") as f:
        return json.load(f)

# Sauvegarder les données dans un fichier
def sauvegarder_donnees(fichier, donnees):
    with open(fichier, "w") as f:
        json.dump(donnees, f, indent=4)

# Générer un matricule unique
def generer_matricule(prefixe, fichier):
    donnees = charger_donnees(fichier)
    num = len(donnees) + 1
    return f"{prefixe}-{str(num).zfill(3)}"

# Vérifier l'existence d'un utilisateur ou patient
def verifier_existence(matricule, fichier):
    donnees = charger_donnees(fichier)
    return matricule in donnees
