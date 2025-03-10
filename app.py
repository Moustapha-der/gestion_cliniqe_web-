from flask import Flask, render_template, request, redirect, url_for, session
from gestion_utilisateurs import authentifier
from flask import Flask, render_template, session
from gestion_patients import get_patients_par_medecin
from gestion_rendezvous import get_rendezvous_du_jour
from flask import Flask, render_template, request, redirect, url_for, session, flash
from gestion_patients import ajouter_patient  # ✅ Vérifie bien cette ligne !
from gestion_rendezvous import get_rendezvous_par_medecin

from gestion_rendezvous import get_rendezvous_par_medecin, get_rendezvous_du_jour

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        matricule, role = authentifier(email, password)
        
        if matricule:
            session["user"] = {"matricule": matricule, "role": role}
            if role == "medecin":
                return redirect(url_for("dashboard_medecin"))
            elif role == "secretaire":
                return redirect(url_for("dashboard_secretaire"))
        
        return render_template("login.html", error="Email ou mot de passe incorrect.")

    return render_template("login.html")
@app.route("/ajouter_patient", methods=["POST"])
def route_ajouter_patient():  # Change le nom pour éviter le conflit avec la fonction
    if "user" not in session or session["user"]["role"] != "secretaire":
        return redirect(url_for("login"))

    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    contact = request.form.get("contact")
    medecin_id = request.form.get("medecin_id")

    matricule = ajouter_patient(nom, prenom, contact, medecin_id)  # Appel correct

    if matricule:
        flash(f"✅ Patient {matricule} ajouté avec succès.", "success")
    else:
        flash("❌ Erreur lors de l'ajout du patient.", "danger")

    return redirect(url_for("dashboard_secretaire"))
@app.route("/modifier_patient", methods=["POST"])
def modifier_patient():
    if "user" not in session or session["user"]["role"] != "secretaire":
        return redirect(url_for("login"))

    matricule = request.form.get("matricule")
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    contact = request.form.get("contact")
    medecin_affecte = request.form.get("medecin_affecte")

    if modifier_patient(matricule, nom, prenom, contact, medecin_affecte):
        flash(f"✅ Patient {matricule} modifié avec succès.", "success")
    else:
        flash("❌ Erreur lors de la modification.", "danger")

    return redirect(url_for("dashboard_secretaire"))


@app.route("/dashboard_medecin")
def dashboard_medecin():
    if "user" not in session or session["user"]["role"] != "medecin":
        return redirect(url_for("login"))

    matricule_medecin = session["user"]["matricule"]
    patients = get_patients_par_medecin(matricule_medecin)
    rdvs_medecin = get_rendezvous_par_medecin(matricule_medecin)
    rdvs_du_jour = get_rendezvous_du_jour(matricule_medecin)  # ✅ Ajoute les rendez-vous du jour

    return render_template(
        "dashboard_medecin.html", 
        user=session["user"], 
        patients=patients, 
        rdvs_medecin=rdvs_medecin, 
        rdvs_du_jour=rdvs_du_jour  # ✅ Envoie bien cette variable au template
    )



@app.route("/dashboard_secretaire")
def dashboard_secretaire():
    if "user" not in session or session["user"]["role"] != "secretaire":
        return redirect(url_for("login"))
    return render_template("dashboard_secretaire.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
@app.route("/planifier_rdv", methods=["POST"])
def planifier_rdv():
    if "user" not in session or session["user"]["role"] != "secretaire":
        return redirect(url_for("login"))

    date = request.form.get("date")
    heure = request.form.get("heure")
    patient_id = request.form.get("patient_id")
    medecin_id = request.form.get("medecin_id")

    from gestion_rendezvous import planifier_rendezvous  # ✅ Vérifier que la fonction est bien importée
    rdv_id = planifier_rendezvous(date, heure, patient_id, medecin_id)

    if rdv_id:
        flash(f"✅ Rendez-vous {rdv_id} ajouté avec succès.", "success")
    else:
        flash("❌ Erreur : Conflit d’horaire ou données incorrectes.", "danger")

    return redirect(url_for("dashboard_secretaire"))

if __name__ == "__main__":
    app.run(debug=True)
print("DEBUG: ajouter_patient =", ajouter_patient)

