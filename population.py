from random import randint, choice
import matplotlib.pyplot as plt

def distance(pos) : return pos[0]**2 + pos[1] **2
def genere(N) :
    """ Genere une population de taille aléatoire comprise entre N/2 et 2*N
        les individus sont non marqués 'b'
    """
    n = randint(N//2,2*N)
    
    return[ [randint(0,400), randint(0,400),'b']  for _ in range(n)]


def represente(pop) :
    """ représentation d'une population
    """

    plt.scatter([v[0] for v in pop], [v[1] for v in pop],c = [v[2] for v in pop], marker = r"$\propto$")


def capture(pop, m) :
    """ capture m individus de la population et les marque
    """

    pop.sort(key = distance)
    for i in range(m) : pop[i][2] = 'r'

def melange(pop) :
    for individu in pop :
        individu[0],individu[1] = randint(0,400),randint(0,400)
