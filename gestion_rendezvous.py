from utilitaires import charger_donnees, sauvegarder_donnees, generer_matricule
from datetime import datetime
from utilitaires import charger_donnees
FICHIER_RDV = "rendezvous.txt"

# Planifier un rendez-vous
def planifier_rendezvous(date, heure, patient_id, medecin_id):
    rdvs = charger_donnees(FICHIER_RDV)
    identifiant = generer_matricule("RDV", FICHIER_RDV)
def get_rendezvous_du_jour(medecin_id):
    rdvs = charger_donnees(FICHIER_RDV)
    today = datetime.today().strftime('%Y-%m-%d')
    
    rdvs_du_jour = [
        {"id": rdv_id, **info}
        for rdv_id, info in rdvs.items()
        if info["medecin_id"] == medecin_id and info["date"] == today
    ]
    return rdvs_du_jour
    # Vérifier s'il y a un conflit d'horaire
    for rdv in rdvs.values():
        if rdv["date"] == date and rdv["heure"] == heure:
            if rdv["medecin_id"] == medecin_id or rdv["patient"] == patient_id:
                return None  # Conflit détecté
    
    rdvs[identifiant] = {
        "date": date,
        "heure": heure,
        "patient": patient_id,
        "medecin_id": medecin_id
    }
from datetime import datetime
def planifier_rendezvous(date, heure, patient_id, medecin_id):
    rdvs = charger_donnees(FICHIER_RDV)

    # Vérifier si le patient et le médecin existent
    patients = charger_donnees("patients.txt")
    utilisateurs = charger_donnees("utilisateurs.txt")

    if patient_id not in patients:
        print("❌ Erreur : Patient introuvable.")
        return None
    if medecin_id not in utilisateurs or utilisateurs[medecin_id]["role"] != "medecin":
        print("❌ Erreur : Médecin introuvable ou matricule invalide.")
        return None

    # Vérifier si le patient a déjà un rendez-vous à cette heure
    for rdv in rdvs.values():
        if rdv["date"] == date and rdv["heure"] == heure and rdv["patient"] == patient_id:
            print("❌ Conflit : Le patient a déjà un rendez-vous à cette heure.")
            return None  # Refuser si le patient est déjà pris

    # Générer un ID unique
    rdv_id = generer_matricule("RDV", FICHIER_RDV)

    # Ajouter le rendez-vous
    rdvs[rdv_id] = {
        "date": date,
        "heure": heure,
        "patient": patient_id,
        "medecin_id": medecin_id
    }

    sauvegarder_donnees(FICHIER_RDV, rdvs)
    return rdv_id

def get_rendezvous_par_medecin(medecin_id):
    rdvs = charger_donnees(FICHIER_RDV)

    # Filtrer les rendez-vous du médecin
    rdvs_medecin = [
        {"id": rdv_id, **info}  # Ajoute l'ID du rendez-vous
        for rdv_id, info in rdvs.items()
        if info["medecin_id"] == medecin_id
    ]
    
    return rdvs_medecin
    # Vérifier si le créneau est déjà pris
    for rdv in rdvs.values():
        if rdv["date"] == date and rdv["heure"] == heure:
            if rdv["medecin_id"] == medecin_id or rdv["patient"] == patient_id:
                print("❌ Conflit : Le créneau est déjà pris.")
                return None  # Conflit détecté

    # Générer un ID unique
    rdv_id = generer_matricule("RDV", FICHIER_RDV)

    # Ajouter le rendez-vous
    rdvs[rdv_id] = {
        "date": date,
        "heure": heure,
        "patient": patient_id,
        "medecin_id": medecin_id
    }

    sauvegarder_donnees(FICHIER_RDV, rdvs)
    return rdv_id
def get_rendezvous_du_jour(medecin_id):
    rdvs = charger_donnees("rendezvous.txt")
    today = datetime.today().strftime('%Y-%m-%d')
    return [rdv for rdv in rdvs.values() if rdv["medecin_id"] == medecin_id and rdv["date"] == today]

    sauvegarder_donnees(FICHIER_RDV, rdvs)
    return identifiant
