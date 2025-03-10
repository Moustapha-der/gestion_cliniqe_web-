import json
import os

# Charger les données depuis un fichier
def charger_donnees(fichier):
    if not os.path.exists(fichier):  # Vérifie si le fichier existe
        with open(fichier, "w") as f:
            f.write("{}")

    with open(fichier, "r", encoding="utf-8") as f:
        try:
            contenu = f.read().strip()  # Supprime les espaces inutiles
            return json.loads(contenu) if contenu else {}
        except json.JSONDecodeError:
            print(f"❌ Erreur JSON dans {fichier}, réinitialisation...")
            return {}

def sauvegarder_donnees(fichier, donnees):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4)
def enregistrer_log(action, user):
    with open("logs.txt", "a") as f:
        f.write(f"{action} effectué par {user} \n")

# Générer un matricule unique
def generer_matricule(prefixe, fichier):
    donnees = charger_donnees(fichier)
    num = len(donnees) + 1
    return f"{prefixe}-{str(num).zfill(3)}"

# Vérifier l'existence d'un utilisateur ou patient
def verifier_existence(matricule, fichier):
    donnees = charger_donnees(fichier)
    return matricule in donnees
