from gestion_patients import ajouter_patient
import json

# Ajouter un patient test
matricule = ajouter_patient("Test", "User", "0612345678", "M-001")

# Vérifier si le patient a bien été ajouté
with open("patients.txt", "r", encoding="utf-8") as f:
    patients = json.load(f)

print("✅ Nouveau patient ajouté :", patients.get(matricule))
