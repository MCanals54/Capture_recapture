from random import randint, choice, sample
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [15, 10]

BIG = 2000
MEDIUM = 500
SMALL = 100

def distance(pos) : return pos[0]**2 + pos[1] **2
def generer(N) :
    """ Genere une population de taille aléatoire comprise entre N/2 et 2*N
        les individus sont non marqués 'b'
    """
    n = randint(N//2,2*N)
    
    return[ [randint(0,400), randint(0,400),'b']  for _ in range(n)]


def representer(pop,title = "Représentation de l'etang") :
    """ représentation d'une population
    """
    
    plt.scatter([v[0] for v in pop], [v[1] for v in pop],c = [v[2] for v in pop], marker = r"$\propto$")
    plt.xlim(0, 400)
    plt.ylim(0, 400)
    plt.title(title)


def marquer(pop, m) :
    """ capture m individus de la population et les marque
    """

    pop.sort(key = distance)
    for i in range(m) : pop[i][2] = 'r'

def melanger(pop) :
    for individu in pop :
        individu[0],individu[1] = randint(0,400),randint(0,400)

def echantillonner(pop, size) :
    pop.sort(key = distance)
    return pop[0:size]

def compter_marques(pop) :
    count = 0
    for fish in pop :
        if fish[2] == 'r' :count +=1
    return count