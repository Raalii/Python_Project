# The main function wich execute the principal program
from game import game
from GraphicGame import GraphicGame

value = input("Bienvenue sur Battle punchliners ! Voulez vous jouer en graphique (tapez 1), ou en console (tapez 2), ou quitter (tapez 3) ? ")

while value != '1' and value != '2' and value != '3' :
    value = input("Veuillez taper 1 pour jouer en graphique, 2 en console et 3 pour quitter : ")


value = int(value)

if value == 1 :
    GraphicGame()
elif value == 2 :
    game()
else :
    print("FIN DU PROGRAMME !")


