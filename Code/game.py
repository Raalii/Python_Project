# File for class game with pygame

from PlayerClass import Combattant
from random import randint
from data import *
# from GraphicGame import GraphicGame

listsOfCharacters = [Combattant("grandma"), Combattant("baby"), Combattant(
    "criminal"), Combattant("IronMan"), Combattant("B2O Biatch")]


def CategorieStr(mot, nbr):
    if mot in LIST_JE[nbr]:
        return "je"
    elif mot in LIST_TU[nbr]:
        return "tu"
    else:
        return "il"


def CohenrenceCheck(str1, str2, str3):
    if str1 == str2:
        if str2 == str3:
            return 3
        else:
            return 2
    else:
        if str1 == str3:
            return 2
        else:
            if str2 == str3:
                return 2
            else:
                return 1


def InputCheck(userInput, context):
    if context == "SELECT_CHARACTERS":
        if len(userInput) != 1 :
            return False
        L = ["1", "2", "3", "4", "5"]
        if userInput in L :
            return True
        else :
            return False
    elif context == "SELECT_ATTACK":
        L = ["1", "2", "3", "4", "5", "6"]
        if len(userInput) != 3 :
            return False
        for char in userInput : 
            if char in L : 
                continue
            else :
                return False
        return True
    
         

def CheckSensibility(Sub, Verb, Compl, player):
    """Fonction qui vérifie si une phrase utilisé par l'utilisateur ne represente pas le point faible de l'autre"""
    check = 1
    if Sub in player.sensibility:  # Si un Sujet est présent dans les points faibles de l'utilisateur
        check += 5
    if Verb in player.sensibility:  # Si un Verbe est présent dans les points faibles de l'utilisateur
        check += 5
    if Compl in player.sensibility:  # Si un Complément est présent dans les points faibles de l'utilisateur
        check += 5
    return check


def game():
    player1 = input("Il y a 5 personnages disponibles, veuillez choisir le votre, en selectionnant un nombre de 1 à 5. Voici les personnages : \n- Granma \n- Baby \n- Criminel \n- IronMan \n- B2OBiatch \nJoueur 1 choisissez votre joueur : ")
    while InputCheck(player1, "SELECT_CHARACTERS") == False:
        player1 = input("Veuillez donner une valeur correcte : ")
    player2 = input(
        f"Joueur 2, veuillez choisir votre joueur, de 1 à 5, en excluant la valeur {player1} qui correspont au joueur {listsOfCharacters[int(player1) - 1].name} : ")
    while InputCheck(player2, "SELECT_CHARACTERS") == False or player1 == player2:
        player2 = input("Veuillez rentrer une valeur correcte : ")

    player1 = listsOfCharacters[int(player1) - 1] 
    player2 = listsOfCharacters[int(player2) - 1]

    print("C'est partie pour le combat....\n\n Chargement en cours......... \n\n")

    

    print("C'est PARTIE ! ")

    tour = 0
    running = True
    while running:
        if tour % 2 == 0 :
            Attack, Defender = player1, player2
            nbr = 1
        else :
            Attack, Defender = player2, player1
            nbr = 2
        print('Au tour du joueur ', nbr)
        LocalSuj = selectList("Subj")
        LocalVerb = selectList("Verb")
        LocalComplement = selectList("Complement")
        print('Voici vos sujets : ',
              LocalSuj, '\nVoici vos verbe : ', LocalVerb,  '\nVoici vos compléments : ', LocalComplement)
        attack = input(
            "Veuillez choisir, en commençant par le sujet, verbe, compléments, votre séléction : ")

        if InputCheck(attack, "SELECT_ATTACK") :
            attack = int(attack)
            attackSubj = LocalSuj[(attack // 100) - 1]
            attackVerb = LocalVerb[((attack % 100) // 10) - 1]
            attackCompl = LocalComplement[(attack % 10) - 1]

            print("PUNCHLINE DE", Attack.name, " : ", attackSubj,
                attackVerb, attackCompl, "\n\n\n")

            coherence = CohenrenceCheck(CategorieStr(attackSubj, 0), CategorieStr(
                attackVerb, 1), CategorieStr(attackCompl, 2))
            dégats = coherence * Attack.culot * CheckSensibility(attackSubj, attackVerb, attackCompl, Defender)

            print("VOTRE SCORE D'ATTACK EST DE : ", dégats)
            print("VOTRE SCORE DE COHERENCE EST DE : ", coherence)
            print("PPPWWWWAAAAAA\n\n\n\n\n")

            Defender.pv -= dégats

            if Defender.pv <= 0:
                print("Le joueur ", nbr, " a perduuu !!!!!!")
                print("FIN DU JEUUUUUUU")
                running = False
            else:
                print(Defender.name, " a encore ", Defender.pv, " pv")

        else : 
            print("\n\n\nVALEUR INCORRECTE !!! ATTAQUE ACTUELLE : 0 pv !! \n\n\n")

        tour += 1   