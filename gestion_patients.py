from utilitaires import charger_donnees, sauvegarder_donnees, generer_matricule

FICHIER_PATIENTS = "patients.txt"

# Ajouter un patient
from utilitaires import charger_donnees, sauvegarder_donnees, generer_matricule

FICHIER_PATIENTS = "patients.txt"

def ajouter_patient(nom, prenom, contact, medecin_id):
    patients = charger_donnees(FICHIER_PATIENTS)

    # Vérifier que le médecin existe avant d'affecter le patient
    utilisateurs = charger_donnees("utilisateurs.txt")
    if medecin_id not in utilisateurs:
        return None  # Médecin inexistant

    # Générer un matricule unique
    matricule = generer_matricule("P", FICHIER_PATIENTS)

    # Ajouter le patient
    patients[matricule] = {
        "nom": nom,
        "prenom": prenom,
        "contact": contact,
        "medecin_affecte": medecin_id
    }

    sauvegarder_donnees(FICHIER_PATIENTS, patients)
    return matricule  # Retourne la matricule pour confirmer l'ajout

#
def get_patients_par_medecin(medecin_id):
    patients = charger_donnees(FICHIER_PATIENTS)
    patients_medecin = [
        {"matricule": matricule, **info}  # Ajoute la matricule dans chaque patient
        for matricule, info in patients.items() if info["medecin_affecte"] == medecin_id
    ]
    return patients_medecin
def archiver_patient(matricule, user):
    patients = charger_donnees("patients.txt")
    archivages = charger_donnees("archivages.txt")

    if matricule in patients:
        archivages[matricule] = patients.pop(matricule)
        sauvegarder_donnees("patients.txt", patients)
        sauvegarder_donnees("archivages.txt", archivages)
        enregistrer_log(f"Archivage du patient {matricule}", user)
        return True
    return False
def modifier_patient(matricule, nom=None, prenom=None, contact=None, medecin_affecte=None):
    patients = charger_donnees(FICHIER_PATIENTS)

    if matricule not in patients:
        return False  # Patient introuvable

    if nom:
        patients[matricule]["nom"] = nom
    if prenom:
        patients[matricule]["prenom"] = prenom
    if contact:
        patients[matricule]["contact"] = contact
    if medecin_affecte:
        patients[matricule]["medecin_affecte"] = medecin_affecte

    sauvegarder_donnees(FICHIER_PATIENTS, patients)
    return True


# Modifier les informations d'un patient
def modifier_patient(matricule, nom=None, prenom=None, contact=None, medecin_affecte=None):
    patients = charger_donnees(FICHIER_PATIENTS)
    if matricule not in patients:
        return False
    
    if nom:
        patients[matricule]["nom"] = nom
    if prenom:
        patients[matricule]["prenom"] = prenom
    if contact:
        patients[matricule]["contact"] = contact
    if medecin_affecte:
        patients[matricule]["medecin_affecte"] = medecin_affecte
    
    sauvegarder_donnees(FICHIER_PATIENTS, patients)
    return True
