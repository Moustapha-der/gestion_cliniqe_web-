from utilitaires import charger_donnees, sauvegarder_donnees
from utilitaires import enregistrer_log

FICHIER_UTILISATEURS = "utilisateurs.txt"

# Authentification des utilisateurs
def authentifier(email, mot_de_passe):
    utilisateurs = charger_donnees(FICHIER_UTILISATEURS)
    for matricule, info in utilisateurs.items():
        if info["email"] == email and info["mot_de_passe"] == mot_de_passe:
            return matricule, info["role"]
    return None, None

# Ajouter un utilisateur (Médecin ou Secrétaire)
def ajouter_utilisateur(nom, prenom, role, email, mot_de_passe):
    utilisateurs = charger_donnees(FICHIER_UTILISATEURS)
    prefixe = "M" if role == "medecin" else "S"
    matricule = generer_matricule(prefixe, FICHIER_UTILISATEURS)
    
    utilisateurs[matricule] = {
        "nom": nom,
        "prenom": prenom,
        "role": role,
        "email": email,
        "mot_de_passe": mot_de_passe
    }
def ajouter_patient(nom, prenom, contact, medecin_id, user):
    patients = charger_donnees("patients.txt")
    matricule = generer_matricule("P", "patients.txt")

    patients[matricule] = {
        "nom": nom,
        "prenom": prenom,
        "contact": contact,
        "medecin_affecte": medecin_id
    }
    
    sauvegarder_donnees("patients.txt", patients)
    enregistrer_log(f"Ajout du patient {matricule}", user)
    return matricule   
    sauvegarder_donnees(FICHIER_UTILISATEURS, utilisateurs)
    return matricule
