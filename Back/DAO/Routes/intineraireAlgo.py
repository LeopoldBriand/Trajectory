class Noeud:
    def __init__(self, nom, id, liaisons):
        self.nom = nom
        self.id = id
        self.liaisons = liaisons

    def getNom(self):
        return self.nom

    def setNom(nom):
        self.nom = nom

    def getLiaisons(self):
        return self.liaisons 

    def setLiaison(self, liaison):
        self.liaisons.append(liaison)

class Liaison:
    def __init__(self, id, distance, noeud1, noeud2):
        self.id = id
        self.distance = distance
        self.noeuds = []
        self.noeuds.append(noeud1) 
        self.noeuds.append(noeud2)

    def getId(self):
        return self.id

    def getNoeuds(self):
        return self.noeuds

    def getDistance(self):
        return self.distance
        
class Chemin:
    def __init__(self, noeuds, distance):
        self.noeuds = []
        self.distance = 0
    
    def getNoeuds(self):
        return self.noeuds

    def getDistance(self):
        return self.distance

    def addNoeud(self, noeud):
        self.noeuds.append(noeud)
    
    def addDistance(self, distance):
        self.distance += distance
                
class Main:
    def __init__(self, noeuds, liaisons, sourceId, destinationId):
        self.noeuds = noeuds
        self.liaisons = liaisons
        self.noeudSource = self.getNodeById(sourceId)
        self.noeudDestination = self.getNodeById(destinationId)
        self.chemins = []
        self.initWays()

    def initWays(self):
        for liaisonID in self.noeudSource.liaisons:
            liaison = self.getLiaisonById(liaisonID)
            self.chemins.append(Chemin(noeuds = [], distance = 0))
            nouveauNoeud = self.getNodeById(liaison.noeuds[-1])
            distance = liaison.getDistance()
            self.chemins[-1].addDistance(distance)
            self.chemins[-1].addNoeud(self.noeudSource)
            self.chemins[-1].addNoeud(nouveauNoeud)

    def getNodeById(self, id):
        for noeud in self.noeuds:
            if noeud.id == id:
                return noeud
                break
    
    def getLiaisonById(self, id):
        for liaison in self.liaisons:
            if liaison.id == id:
                return liaison
                break

    def getShortestWay(self):
        self.chemins.sort(key=lambda chemin: chemin.distance)

    def goToNewHorizon(self):
        self.getShortestWay()
        for liaisonID in self.chemins[0].noeuds[-1].liaisons:
            liaison = self.getLiaisonById(liaisonID)
            self.chemins.append(Chemin(noeuds = [], distance = 0))
            nouveauxNoeuds=self.chemins[0].getNoeuds()
            for nouveauNoeud in nouveauxNoeuds:
                self.chemins[-1].addNoeud(nouveauNoeud)
            nouveauNoeud = self.getNodeById(liaison.noeuds[-1])
            self.chemins[-1].addNoeud(nouveauNoeud)
            distance = self.chemins[0].getDistance() + liaison.getDistance()
            self.chemins[-1].addDistance(distance)
        del(self.chemins[0])

        self.getShortestWay()
        if not(self.noeudDestination.id == self.chemins[0].noeuds[-1].id):
            return self.goToNewHorizon()
        else:
            return self.chemins[0].noeuds

#     def ajoutDesNoeudsTraverses(self):
#         noeuds = []
#         noeuds = self.petitChemin.getNoeuds()
#         if self.noeudsTraverses[-1].getNom() == noeuds[0].getNom():
#             self.noeudsTraverses.append(noeuds[1])
#         elif noeuds[0].getNom() not in self.noeudsTraverses.__getitem__().__getattribute__("nom"): 
#             self.noeudsTraverses.append(noeuds[0])
            
#     def constitutionNomChemin(self, noeud1, chemin, i):
#         #Constitution du nom du chemin à l'aide des noms des noeuds dans les liaisons rencontrées
#         noeuds = []
#         noeuds = self.liaisonsNoeud[i].getNoeuds()
#         for j in range(0, len(noeuds)):
#                 # On ajoute un noeud s'il n'a pas déjà était traversé
#             if noeuds[j] not in self.noeudsTraverses:
#                 chemin.agrandirNom(noeuds[j].getNom())
#                 chemin.appendNoeud(noeuds[j])
#         return chemin

#     def constitutionDuChemin(self, noeud1, i):
#         '''
#         arg chemins : liste de chemins, pour les nouveaux qui vont apparaître.
#         arg i : liaison en cours d'analyse.
#         '''
#         repriseChemin = Chemin()
#         repriseChemin = copy.deepcopy(self.petitChemin)
#         repriseChemin = self.constitutionNomChemin(noeud1, repriseChemin, i)
        
#         if repriseChemin.getNom() != self.petitChemin.getNom():
#             #Ajout de la distance
#             repriseChemin.augmenterDistance(self.liaisonsNoeud[i].getDistance())
#             #Ajout du chemin à la liste des chemins que l'on va rencontrer, et avancer selon les distances.
#             self.cheminsPrecedents.append(repriseChemin)

#     def cheminLePlusCourt(self, noeud1, noeud2):
#         '''
#         Rempli "petitChemin"
#         '''
#         self.liaisonsNoeud = noeud1.getLiaisons()
#         for i in range(0, len(self.liaisonsNoeud)):
#             self.constitutionDuChemin(noeud1, i) # i : liaison en cours d'analyse
        
#         self.cheminsPrecedents.remove(self.petitChemin) #On va agrandir "petitChemin" , alors on supprime l'ancienne instance de la liste pour la remplacer
#         self.petitChemin = Chemin()

#         #Tri les chemins par ordre de distance
#         self.cheminsPrecedents = sorted(self.cheminsPrecedents, key=lambda Chemin: Chemin.distance)    

#         #Détermine quel chemin est désormais le plus court
#         self.petitChemin = self.cheminsPrecedents[0]

#         #On récupère le nouveau noeud courant en l'ajoutant aux noeuds traverses
#         self.ajoutDesNoeudsTraverses()
        
#     def calcDist(self, noeud1, noeud2):
#         '''
#         noeud1 => Position actuelle
#         noeud2 => Destination finale
#         '''            
#         #Determine le chemin le plus court parmi les liaisons du noeud passé en premier paramètre
#         self.cheminLePlusCourt(noeud1, noeud2)
#         print(self.petitChemin.getNom() + " " + str(self.petitChemin.getDistance()))
#         if(self.petitChemin.getNom() == "ACBE"): # Mauvais test final
#             exit
        
#         dernierNoeud = self.petitChemin.getNoeuds()
#         self.calcDist(dernierNoeud[-1], noeud2)

#     def createData(self):     
#         #Noeud de départ
#         self.noeudA = Noeud("A")

#         #Noeuds intermédiaires
#         self.noeudB = Noeud("B")
#         self.noeudC = Noeud("C")
#         self.noeudD = Noeud("D")
        
#         #Noeud d'arrivé
#         self.noeudE = Noeud("E")
        
#         self.liaisonAB = Liaison("", 4, 0, self.noeudA, self.noeudB)
#         self.liaisonAC = Liaison("", 3, 0, self.noeudA, self.noeudC)
#         self.liaisonAD = Liaison("", 7, 0, self.noeudA, self.noeudD)

#         self.liaisonBC = Liaison("", 2, 0, self.noeudB, self.noeudC)
#         self.liaisonBE = Liaison("", 3, 0, self.noeudB, self.noeudE)
#         self.liaisonCE = Liaison("", 6, 0, self.noeudC, self.noeudE)
#         self.liaisonDE = Liaison("", 1, 0, self.noeudD, self.noeudE)

#         self.noeudA.setLiaison(self.liaisonAB)
#         self.noeudA.setLiaison(self.liaisonAC)
#         self.noeudA.setLiaison(self.liaisonAD)

#         self.noeudB.setLiaison(self.liaisonAB)
#         self.noeudB.setLiaison(self.liaisonBC)
#         self.noeudB.setLiaison(self.liaisonBE)

#         self.noeudC.setLiaison(self.liaisonAC)
#         self.noeudC.setLiaison(self.liaisonBC)
#         self.noeudC.setLiaison(self.liaisonCE)

#         self.noeudD.setLiaison(self.liaisonAD)
#         self.noeudD.setLiaison(self.liaisonDE)

#         self.noeudE.setLiaison(self.liaisonBE)
#         self.noeudE.setLiaison(self.liaisonCE)
#         self.noeudE.setLiaison(self.liaisonDE)


#         self.noeudDeDepart = self.noeudA
#         self.noeudDeFin = self.noeudE

# main = Main()