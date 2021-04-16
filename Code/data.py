# That programm will contain all the important data (lists)

from random import randint


# Liste des verbes, sujets en "je"
LIST_JE = [["Je", "J'", "Pour moi je" , "Je pense sincèrement que je"], ["me balade", "charbonne", "vois", "mange",
                                                                                                  "suis", "défouraille", "arrache", "bois", "allume", "vends", "souléve", "dessine", "filme", "écrase", "Brosse"], ["dans une vitrine à Amsterdam", "le meilleur", 'tes grands morts', "dans une porcherie ", "avec t'es ancêtres", "face à ton avenir", "avec ton chien", "dans une grotte", "dans une cabane", "en public", "sur la place handicapé", "ton cd dans ma caisse"]]


# Liste des verbes, sujets en "tu"
LIST_TU = [["Pour moi tu", 'Tu', "En toute honneteté tu", "Je pense que tu",
            "A mon humble avis tu", "t'", "te", "ta bouche"], ["es", "vas", "ressembles", "réprésentes", "laveras", "crois", "mangeras", "manges", "pues", "sens", "pense", "repousse", "nettoies", "choisiras", "salira", "salis", "choisira", "vise"],
           ["ta mère", "ton honneur", "ta destinée en tant que bouffon dans la street", "une vrai tête de taré" "la viellesse", "la mocheté à son paroxysme", "débile comme tes pieds", "un chasseur de fuck", "le chien affamé", "Ryad", "la lune", "un putain de geek", "comme Mimi Mathy dans un concour de Dunk", "chuter", "éclaté au sol", "un tableau de Picasso", "dans une bouche d'égout", "avec le president", "dans une télé novela", "dans un film d'horreur", "les cités de france naravlo", "suce encore son pouce"]]


# Liste des verbes, sujets en "il"
LIST_IL = [["ta tête", "ton visage", "Ta soeur", "Pour toi, le port de la burka", "le rap", "le", "le mec", "il", "ta frimousse", "Ton père", "la fille de ta fille"], [
    "n'est pas", "devrait", "être", "aurait dû", "voit", "a", "pris", "prend", "est", "pense", "sait", "dort", "ressemble", "donne", "regarde", "tue", "termine", "décape", "avale", "refoule", "balance", "rouillé"], ["très jolie", "pour toi", "obligatoire", "à un robot", "un compte Dofus", "pour un Anonymous", "un putain de geek", "pas compter", "au chomage", "dans une maison hanté", "à chucky", "par Bruce Lee", "un Viking", "DUC", "sale vieille peau", "30000 ans", "gros", "deformé", "kaaris", "gamin", "nourisson", "vieux robot", "punchline merdique", "moins fort que"]]


# Grande liste qui stocke toutes les valeurs
LIST_TOTAL = [LIST_JE, LIST_TU, LIST_IL]


def selectList(type):
    """Fonction qui retourne en fonction du type une liste de 6 mot pseudo aléatoires"""
    # Si le type entré est un sujet
    if type == 'Subj':
        L = [LIST_TOTAL[randint(0, 2)][0][randint(0, len(LIST_TOTAL[0]) - 1)]
             for n in range(2)]
        for loop in range(2):
            categorie = randint(0, 2)
            L.append(LIST_TOTAL[categorie][0]
                     [randint(0, len(LIST_TOTAL[categorie][0]) - 1)])
            categorie = randint(0, 2)
            L.append(LIST_TOTAL[categorie][0]
                     [randint(0, len(LIST_TOTAL[categorie][0]) - 1)])
        return L
    # Si le type entré est un sujet
    elif type == 'Verb':
        L = [LIST_TOTAL[randint(0, 2)][1][randint(0, len(LIST_TOTAL[0]) - 1)]
             for n in range(2)]
        for loop in range(2):
            categorie = randint(0, 2)
            L.append(LIST_TOTAL[categorie][1]
                     [randint(0, len(LIST_TOTAL[categorie][1]) - 1)])
            categorie = randint(0, 2)
            L.append(LIST_TOTAL[categorie][1]
                     [randint(0, len(LIST_TOTAL[categorie][1]) - 1)])

        return L
    # Si le type entré est un complément
    else:
        L = [LIST_TOTAL[randint(0, 2)][2][randint(0, len(LIST_TOTAL[0]) - 1)]
             for n in range(2)]
        for loop in range(2):
            categorie = randint(0, 2)
            L.append(LIST_TOTAL[categorie][2]
                     [randint(0, len(LIST_TOTAL[categorie][2]) - 1)])
            categorie = randint(0, 2)
            L.append(LIST_TOTAL[categorie][2]
                     [randint(0, len(LIST_TOTAL[categorie][2]) - 1)])
        return L
