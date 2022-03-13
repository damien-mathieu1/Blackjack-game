import random


#Somme de base : 200

Argent = 200

while Argent > 0:
    cartes_croupier = [] # Cartes du croupier

    cartes_joueur = [] # Cartes du joueur

    # Distribuer les cartes
    # Dévoiler les cartes

    # Croupier
    while len(cartes_croupier) != 2:
        cartes_croupier.append(random.randint(2, 11))
        if len(cartes_croupier) == 2:
            print("Le croupier a une carte cachée & ", cartes_croupier[1])
        

    # Joueur
    while len(cartes_joueur) != 2:
       cartes_joueur.append(random.randint(2, 11))
    if len(cartes_joueur) == 2:
            print("Tu as ", cartes_joueur ,"donc tu as "+ str(sum(cartes_joueur)))
    Mise = float(input("Vous avez " + str(Argent) + " euros, combien souhaitez vous miser?"))
    if Mise <= Argent :
               Argent = Argent - Mise
               print("Vous misez " + str(Mise) + " euros, vous avez encore " + str(Argent))
               
    elif Mise > Argent:
        print("Vous ne pouvez pas miser plus que ce que vous avez.")
        Mise = float(input("Vous avez " + str(Argent) + " euros, combien souhaitez vous miser?"))
    elif Mise <= 0:
        print("Vous ne pouvez pas jouer sans miser.")
        Mise = float(input("Vous avez " + str(Argent) + " euros, combien souhaitez vous miser?"))
       
    #Jeu en fonctionnement
        
    while sum(cartes_joueur) < 21:
        prendre_laisser = str(input("Voulez vous prendre ou laisser ? "))
        if prendre_laisser == "Prendre":
            cartes_joueur.append(random.randint(2, 11))
            print("Vous avez maintenant un total de " + str(sum(cartes_joueur)) + " avec ces cartes ", cartes_joueur)

            if 11 in cartes_joueur and sum(cartes_joueur) > 21:
                cartes_joueur.remove(11)
                cartes_joueur.append(1)
                print("Tu as donc "+ str(sum(cartes_joueur)) +" avec ces cartes", cartes_joueur ,", ton 11 est devenue un 1")

            
        #Répétition du "if" pour éviter la casse entre minuscule et MAJ
            
        if prendre_laisser == "prendre":
            cartes_joueur.append(random.randint(2, 11))
            print("Vous avez maintenant un total de " + str(sum(cartes_joueur)) + " avec ces cartes ", cartes_joueur)

            if 11 in cartes_joueur and sum(cartes_joueur) > 21:
                cartes_joueur.remove(11)
                cartes_joueur.append(1)
                print("Tu as donc "+ str(sum(cartes_joueur)) +" avec ces cartes", cartes_joueur ,", ton 11 est devenue un 1")

            
        else :
            
            print("Le croupier a un total de " + str(sum(cartes_croupier)) + " avec ", cartes_croupier)
            print("Vous avez un total de  " + str(sum(cartes_joueur)) + " avec ", cartes_joueur)

            if sum(cartes_croupier)== 21 :
                print("BLACKJACK ! La banque gagne")
                break

            if sum(cartes_croupier) > sum(cartes_joueur):
                print("La banque gagne!")
                break
            
            while sum(cartes_croupier) < 17 :
                print("Le croupier a " + str(sum(cartes_croupier))+ " il tire une carte.")
                cartes_croupier.append(random.randint(2, 11))    
                print("Le croupier a maintenant "+ str(sum(cartes_croupier))+ " avec ", cartes_croupier)

                if 11 in cartes_croupier and sum(cartes_croupier) > 21 :
                    cartes_croupier.remove(11)
                    cartes_croupier.append(1)
                    print("Le croupier a donc "+ str(sum(cartes_joueur)) +" avec ces cartes", cartes_joueur ,", son 11 est devenue un 1")

                
            if sum(cartes_croupier)== 21 :
                print("BLACKJACK ! La banque gagne.")
                print ("Vous avez maintenant" + str(Argent) + " euros.")
                break
            
            if sum(cartes_croupier)>21 :
                print("La banque perd. Vous avez gagné !")
                Argent = Argent + (Mise *2)
                print ("Vous avez maintenant" + str(Argent) + " euros.")
                break

            if sum(cartes_croupier) > sum(cartes_joueur):
                print("La banque gagne!")
                print ("Vous avez maintenant" + str(Argent) + " euros.")
                break

            elif sum(cartes_croupier) == sum(cartes_joueur):
                print("Egalité !")
                Argent = Argent + Mise
                print ("Vous avez été remboursé et avez maintenant" + str(Argent) + " euros.")
                break

            else:
                print("Vous avez gagné !")
                Argent = Argent + (Mise *2)
                print ("Vous avez maintenant" + str(Argent) + " euros.")
                break

    if sum(cartes_joueur) > 21:
        print("Vous avez perdu ! La banque gagne.")
        print ("Vous avez maintenant" + str(Argent) + " euros.")

    elif sum(cartes_joueur) == 21:
        print("BLACKJACK ! Vous avez gagné! 21")
        Argent = Argent + (Mise *2.5)
        print ("Vous avez maintenant" + str(Argent) + " euros.")
