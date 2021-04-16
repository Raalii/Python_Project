# That programm will contain the "Combattant" class which represent the characters of the game
import pygame

class Combattant(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        if name == "grandma":
            self.name = name
            self.pv = 380
            self.sensibility = ["burqa", "DUC", "Mimi Mathy", "sale vielle peau", "30000 ans"]
            self.culot = 15
            self.image = pygame.image.load('assets/' + name + '.png')
            self.rect = self.image.get_rect()
            self.rect.x = 20
            self.rect.y = 20
        elif name == "baby":
            self.name = name
            self.pv = 250
            self.sensibility = ["une vrai tête de taré",
                                "visage", "pas", "très jolie", "gamin", "nourisson", "suce encore son pouce"]
            self.culot = 20
            self.image = pygame.image.load('assets/Baby.png')
            self.rect = self.image.get_rect()
            self.rect.x = 300
            self.rect.y = 10
        elif name == "criminal":
            self.name = name
            self.pv = 70
            self.sensibility = ["le prix de l'immobilier",
                                "chuter", "ta bouche", "en public", "vas"]
            self.culot = 70
            self.image = pygame.image.load('assets/criminal.png')
            self.rect = self.image.get_rect()
            self.rect.x = 1400
            self.rect.y = 710
        elif name == "IronMan":
            self.name = name
            self.pv = 900
            self.sensibility = [
                "gros", "dans une vitrine à Amsterdam", "visage", "deformé", "vieux robot", "rouillé"]
            self.culot = 7
            self.image = pygame.image.load('assets/IronMan.png')
            self.rect = self.image.get_rect()
            self.rect.x = 1200
            self.rect.y = 10
        elif name == "B2O Biatch":
            self.name = name
            self.pv = 1500
            self.sensibility = ["Kaaris", "sur la place handicapé",
                                "concour de dunk", "ton cd dans ma caisse", "punchline merdique",]
            self.culot = 9
            self.image = pygame.image.load('assets/rappeur.png')
            self.rect = self.image.get_rect()
            self.rect.x = 600
            self.rect.y = 600

    def __str__(self):
        return self.name + "  -  " + str(self.pv) + "pv  -  culot : " + str(self.culot)
