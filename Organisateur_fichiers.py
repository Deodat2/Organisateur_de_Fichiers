import os
import shutil


def organisation_dossier(dossier):
    # Dictionnaire pour ranger les extensions
    types_fichiers = {
        "Images" : [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Videos" : [".mp4", ".avi", ".mkv"],
        "Documents" : [".doc", ".docx", ".pdf", ".txt", "xlsx"],
        "Audios" : [".mp3", ".wav"],
        "Archives" : [".zip", ".rar", ".7z", ".tar"],
    }
    # Parcourir les fichiers du dossier
    for fichier in os.listdir(dossier):     # os.listdir(dossier) permet de lister tous les fichiers et sous-dossiers présent dans le dossier
        chemin_complet_fichier = os.path.join(dossier, fichier)     # os.path.join(dossier, fichier) permet de créer un chemin pour chaque fichier
        # Parcourir les fichiers des sous-dossiers existants
        if os.path.isdir(chemin_complet_fichier):     # os.path.isdir() permet de vérifier si l'élément est un sous-dossier
            organisation_dossier(chemin_complet_fichier)
        # Triez les fichiers par extension
        _, extension = os.path.splitext(fichier)     # os.path.splitext(fichier) permet de diviser le nom du fichier en deux parties, le nom de base (avant le point) et l'extension (apres le point). (_, extension), le (_) est utilisé pour ignorer la partie "nom de base". Nous avons juste besion de l'extension.
        for type_fichier, extensions in types_fichiers.items():
            if extension.lower() in extensions:
                sous_dossier = os.path.join(dossier, type_fichier)
                os.makedirs(sous_dossier, exist_ok=True)     # os.makedirs() permet de creer un sous-dossier pour le type de fichier
                shutil.move(chemin_complet_fichier, os.path.join(sous_dossier, fichier))     #shutil.move() permet de déplacer le fichier dans le sous-dossier approprié
                print(f"Déplacé : {fichier} -> {sous_dossier}")     # Afficher un message à chaque fois qu'un fichier est déplacé
                break

dossier_cible = input("Entrez le chemin du dossier à organiser :").strip()
if os.path.exists(dossier_cible):
    organisation_dossier(dossier_cible)
else:
    print("Le dossier spécifié n'existe pas")