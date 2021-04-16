# The Graphic game function which contain the graphic game
# Importe toutes les données relatives au mots, phrases, et complétements
from data import selectList
import pygame  # Permettra d'importe la librairie pygame
import time  # Importe le temps
# Permet d'avoir une taille d'écran relative à la résolution (taille dynamique)
from tkinter import Tk
from PlayerClass import Combattant
from game import CategorieStr, CohenrenceCheck, CheckSensibility


def GraphicGame():
    # Initier les fenetres
    pygame.init()

    # Initier quelques couleurs
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Définir le titre du jeu
    pygame.display.set_caption("Battle Punchliners")

    # Pour que le jeu soit en plein écran (taille dynamique)
    screen = pygame.display.set_mode((1920, 1080))

    # On charge le fond d'écran
    background = pygame.image.load('assets/bg3.jpg')

    # Variable importantes
    HomeMenu = True  # Permet de vérifier si l'utilisateur a choisi ces joueurs, et affiche le menu principal
    AttackPlayer = False  # Pour contrôler le déroulement du jeu
    HaveSelect = False  # Pour checker si l'utilisateur a choisi sa phrase
    select = True
    attackSubj = ""  # Stocke les Mots choisi par l'utilisateur
    attackCompl = ""  # Sujets
    attackVerb = ""  # Compléments
    LocalSuj = []  # Initier les lists où seront stockés les mots prposé
    LocalVerb = []
    LocalComplement = []
    center_x, center_y = 320, 240  # Coordonnées
    PlayersSelected = 0
    coherence = 0

    # Charger nos joueurs
    player = Combattant('baby')
    player2 = Combattant('grandma')

    # Permettra de spécifier un taux de rafraichissement (grâce à clock.tick)
    clock = pygame.time.Clock()

    # Polices
    font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
    police = pygame.font.SysFont('impact', 23)

    # On initie deux textes, dont l'un representera l'Input
    prompt = font.render('Entrez un nombre : ', True, BLACK)
    prompt_rect = prompt.get_rect(center=(center_x, center_y))
    UserInputValue = ""
    UserInput = font.render(UserInputValue, True, BLACK)
    # Permet de situer le texte juste à droite du texte "prompt"
    user_input_rect = UserInput.get_rect(topleft=prompt_rect.topright)

    # Fonction d'affichage

    def CheckValue(string, context):
        """Fonction qui vérifie les entrés utilisateurs en fonction de deux contextes, spécifiés par True et False"""
        if context:
            if len(string) != 1:
                return False
            L = ['1', '2', '3', '4', '5']
        elif context == False:
            if len(string) != 3:
                return False
            L = ['1', '2', '3', '4', '5', '6']
        for value in string:
            if value in L:
                continue
            else:
                return False
        return True

    def DisplayText(txt, x, y):
        """Fonction qui affiche le texte txt, dans les coordonnées x et y """
        screen.blit(police.render(txt, True, WHITE), (x, y))

    def PrintCoherence(score):
        """Fonction qui affiche un exte en fonction du score"""
        if score == 3:
            return "LA PHRASE EST COHERENTE"
        elif score == 2:
            return "LA PHRASE EST MOYENNEMENT COHERENTE"
        else:
            return "LA PHRASE N'EST PAS COHERENTE"

    running = True
    tour = 0

    while running:
        # Appliqur le bg du jeu
        screen.blit(background, (0, 0))

        if HomeMenu:  # Si on est dans le menu principal
            prompt_rect.x = 1650
            listsOfCharacters = [Combattant("grandma"), Combattant("baby"), Combattant(
                "criminal"), Combattant("IronMan"), Combattant("B2O Biatch")]
            v = 1
            for value in listsOfCharacters:
                screen.blit(value.image, value.rect)
                if v == 1:
                    screen.blit(police.render(str(v), True, BLACK),
                                (value.rect.x + 70, value.rect.y + 50))
                elif v == 2:
                    DisplayText(str(v), value.rect.x + 200, value.rect.y + 100)
                else:
                    DisplayText(str(v), value.rect.x + 50, value.rect.y + 50)

                v += 1

            if PlayersSelected == 1:
                if select:
                    player = listsOfCharacters[int(UserInputValue) - 1]
                    UserInputValue = ''
                    select = False
                DisplayText(
                    "JOUEUR 2 VEUILLEZ CHOISIR VOTRE PERSONNAGE", 1400, 650)
            elif PlayersSelected == 2:
                player2 = listsOfCharacters[int(UserInputValue) - 1]
                UserInputValue = ""
                HomeMenu = False
        else:  # Si on est sur une partie
            # Appliquer images joueurs et afficher pv
            screen.blit(player.image, (1200, 360))
            screen.blit(player2.image, (100, 360))
            screen.blit(police.render(
                "PV : " + str(player2.pv), True, WHITE), (50, 1000))
            screen.blit(police.render(
                "PV : " + str(player.pv), True, WHITE), (1600, 1000))

            # Si on a pas proposé au joueur de phrase
            if AttackPlayer == False:
                # Et que le joueur a déjà attacké
                if HaveSelect == True:
                    # On enregistre son score d'attaque et on donne le tour au deuxième joueur
                    attack = UserInputValue
                    # Si l'utilisateur entre des valeurs possibles
                    if CheckValue(attack, False):
                        # Cette vérification permet de vérifier que l'utilisateur n'entre pas des caractères invalides
                        attack = int(attack)
                        attackSubj = LocalSuj[(attack // 100) - 1]
                        attackVerb = LocalVerb[((attack % 100) // 10) - 1]
                        attackCompl = LocalComplement[(attack % 10) - 1]
                        coherence = CohenrenceCheck(CategorieStr(attackSubj, 0), CategorieStr(
                            attackVerb, 1), CategorieStr(attackCompl, 2))
                        if tour % 2 == 0:
                            degats = coherence * player.culot * 2 * \
                                CheckSensibility(
                                    attackSubj, attackVerb, attackCompl, player2)
                            player2.pv -= degats
                            if player2.pv <= 0:
                                HomeMenu = True
                                PlayersSelected = 0
                                select = True
                        else:
                            degats = coherence * player2.culot * 2 * \
                                CheckSensibility(
                                    attackSubj, attackVerb, attackCompl, player)
                            player.pv -= degats
                            if player.pv <= 0:
                                HomeMenu = True
                                PlayersSelected = 0
                                select = True
                    HaveSelect = False
                    UserInputValue = ""
                    tour += 1
                # On propose de nouveau mot
                AttackPlayer = True
                LocalSuj = selectList("Subj")
                LocalVerb = selectList("Verb")
                LocalComplement = selectList("Compl")

            # Ici on affiche les mots
            for key in range(6):
                DisplayText(str(key + 1) + " : " +
                            LocalSuj[key], 700, (50 * (key + 1)))
                DisplayText(str(key + 1) + " : " +
                            LocalVerb[key], 700, (300 + 50 * (key + 1)))
                DisplayText(str(key + 1) + " : " +
                            LocalComplement[key], 700, (600 + 50 * (key + 1)))
                if key == 5:
                    # Pour bien séparer les sujets du verbe, on met un séprateur de ligne
                    DisplayText(
                        "-----------------------------------------------------------------------------", 600, 325)
                    DisplayText(
                        "-----------------------------------------------------------------------------", 600, 625)

            if tour % 2 == 0:  # Si c'est au joueur 2
                DisplayText("PUNCHLINE DE " + player2.name + " : " + attackSubj + " "
                            + " " + attackVerb + " " + attackCompl, 100, 10)
                DisplayText(PrintCoherence(coherence), 100, 40)
                prompt_rect.x = 1550
            else:  # Si c'est au joueur 1
                DisplayText("PUNCHLINE DE " + player.name + " : " + attackSubj + " "
                            + " " + attackVerb + " " + attackCompl, 1000, 10)
                DisplayText(PrintCoherence(coherence), 1000, 40)
                prompt_rect.x = 100

        for event in pygame.event.get():
            # Si le joueur ferme la fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:  # Si l'utilisateur appuie sur un bouton
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Si l'utilisateur appuie sur entrer
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if HomeMenu and CheckValue(UserInputValue, True):
                        if PlayersSelected == 0:
                            PlayersSelected = 1
                        else:
                            PlayersSelected = 2
                    else:
                        AttackPlayer = False
                        HaveSelect = True
                # Si l'utilisateur appuie sur "Retour" (ou supprimer)
                elif event.key == pygame.K_BACKSPACE:
                    # On enlève à l'input la dernière valeur ecrite
                    UserInputValue = UserInputValue[:-1]
                else:  # Sinon
                    UserInputValue += event.unicode  # On lui attribue la valeur écrite
                UserInput = font.render(UserInputValue, True, BLACK)
                user_input_rect = UserInput.get_rect(
                    topleft=prompt_rect.topright)
        screen.blit(UserInput, user_input_rect)
        screen.blit(prompt, prompt_rect)
        DisplayText("Appuyer sur Échap pour quitter", 800, 1000)

        # Mettre à jour l'écran
        clock.tick(30)  # Afficher à 30 fps le jeu
        pygame.display.flip()

    pygame.quit()
