import hashlib
import json

def verif():
    while True:    
        minuscule =  "abcdefghijklmnopqrstuvwxyz"
        majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_char = "(!, @, #, $, %, ^, &, *, .)"
        chiffre = "0123456789"
        l, u, p, d = 0, 0, 0, 0,
        password = input("Entre un mot de passe : ")

        if len(password) >= 8:
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
        elif l ==0:
            print("Le mot de passe dois contenir au moins une minuscule")
        elif u == 0:
           print("Le mot de passe dois contenir au moins une majuscule")
        elif p == 0:
            print("le mot de passe dois contenir au moins un chiffre")
        elif d == 0:
            print("Le mot de passe dois contenir au moins une caractère spécial (!, @, #, $, %, ^, &, *, .)")
        else:
            print("Mot de passe validé")
            return(password)
        

Password = (verif())

hash = hashlib.sha256(Password.encode()).hexdigest()
# print(hash)

def save_json(mdp):
    with open("data.json", "r+") as fichier:
        save = json.load(fichier)
        save["mdp"].append({"mdp":mdp}) 
        fichier.seek(0)
        json.dump(save, fichier, indent=4) 

save_json(hash)
# my_dict = hash 
# jsonData = json.dumps(my_dict)
# jsonFile = open("data.json", "a")
# jsonFile.write(jsonData)
# jsonFile.close()