import hashlib
import json

def verif():
    while True:
        # Définition des caractères nécessaires pour un mot de passe fort
        minuscule =  "abcdefghijklmnopqrstuvwxyz"
        majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_char = "(!, @, #, $, %, ^, &, *, .)"
        chiffre = "0123456789"
        # Initialisation des compteurs pour les caractères requis
        l, u, p, d = 0, 0, 0, 0

        # Demande de saisie d'un mot de passe à l'utilisateur
        password = input("Entre un mot de passe : ")

        # Vérification de la longueur du mot de passe saisi
        if len(password) >= 8:
            # Vérification de la présence des caractères requis dans le mot de passe
            for i in password:

                if i in minuscule:
                    l += 1 
                
                if i in majuscule:
                    u += 1 
                
                if i in special_char:
                    d += 1

                if i in chiffre:
                    p += 1

        if len(password) < 8 :
            print("Votre mot de passe doit contenir au moins 8 caractère")
        # Affichage d'un message d'erreur si le mot de passe ne remplit pas les critères requis
        elif l ==0:
            print("Le mot de passe dois contenir au moins une minuscule")
        elif u == 0:
           print("Le mot de passe dois contenir au moins une majuscule")
        elif p == 0:
            print("le mot de passe dois contenir au moins un chiffre")
        elif d == 0:
            print("Le mot de passe dois contenir au moins une caractère spécial (!, @, #, $, %, ^, &, *, .)")
        else:
            # Si le mot de passe est valide, retourner le mot de passe
            print("Mot de passe validé")
            return(password)

# Appel de la fonction de vérification de mot de passe et 
Password = verif()

def cryptage():
    # Hashage du mot de passe avec l'algorithme SHA-256
    hash = hashlib.sha256(Password.encode()).hexdigest()
    # print(hash)
    return hash
hash = cryptage()

def check():
    with open("data.json", "r") as temp:
        load = json.load(temp)
        for check in load["mdp"]:
            # for value in check['mdp']:
            print(check['mdp'])
            print(hash)
            if check['mdp'] == hash:
                print("Le mot de passe existe deja veuillez en choisir un autre")
                verif()
            else:
                print("enregistrement dans la base de donné ")

check()
#Fonction pour sauvegarder le hash du mot de passe dans un fichier JSON
def save_json(mdp):
    with open("data.json", "r+") as fichier:
        save = json.load(fichier)
        save["mdp"].append({"mdp":mdp}) 
        fichier.seek(0)
        json.dump(save, fichier, indent=4) 

# Appel de la fonction pour sauvegarder le hash du mot de passe dans le fichier JSON
save_json(hash)