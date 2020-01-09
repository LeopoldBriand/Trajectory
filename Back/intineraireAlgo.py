class Noeud

    id = ""
    nom = ""
    liaisons []

    def __init__(self, nom):
        this.nom = nom 

    def getNom():
        return nom

    def setNom(nom):
        this.nom = nom

    def getLiaisons():
        return liaisons 

    def setLiaison(liaison):
        liaisons.append(liaison)
        
    def getId():
        return id
    
    def setId(id):
        this.id = id

class Liaison
    
    id = ""
    distance = 0
    temps = 0
    noeuds = []

    def __init__(self, id, distance, temps, noeud1, noeud2):
        self.id = id
        self.distance = distance
        self.temps = temps
        self.noeuds.append(noeud1) 
        self.noeuds.append(noeud2)


    def getNoeuds():
        return noeuds
    

    def setNoeud(noeud):
        noeuds.append(noeud)

class Main

    #Noeud de départ
    Noeud noeudA("A")

    #Noeuds intermédiaires
    Noeud noeudB("B")
    Noeud noeudC("C")
    Noeud noeudD("D")
    
    #Noeud d'arrivé
    Noeud noeudE("E")
    
    Liaison liaisonAB("", 2, 0, noeudA, noeudB)
    Liaison liaisonAC("", 5, 0, noeudA, noeudC)
    Liaison liaisonAD("", 3, 0, noeudA, noeudD)

    Liaison liaisonBE("", 1, 0, noeudB, noeudE)
    Liaison liaisonCE("", 4, 0, noeudC, noeudE)
    Liaison liaisonDE("", 6, 0, noeudD, noeudE)

    setLiaisons(liaisonAB)
    setLiaisons(liaisonAC)
    setLiaisons(liaisonAD)

    def calcDist(noeud1, noeud2):

        liaisonNoeud1 = 
        