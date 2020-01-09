class Noeud

    id = ""
    nom = ""
    liaisons []

    def __init__(self) 

    def getNom():
        return nom

    def setNom(nom):
        this.nom = nom

    def getLiaisons():
        return liaisons 

    def setLiaisons(liaison):
        liaisons.append(liaison)

class Liaison
    
    id = ""
    distance = 0
    temps = 0
    noeuds = []

    def __init__(self, id, distance, temps, noeud1, noeud2 ):
        self.id = id
        self.distance = distance
        self.temps = temps
        self.noeuds.append(noeud1) 
        self.noeuds.append(noeud2)


    def getNoeuds():
        return noeuds
    

    def setNoeuds(noeud):
        noeuds.append(noeud)

class Main

    Noeud noeudA()
    Noeud noeudB()
    Noeud noeudC()
    Noeud noeudD()
    Noeud noeudE()
    Liaison liaisonAB("", 2, 0, A)
    Noeud noeudA()