

import random as rnd


class Cours:
	def __init__(self,nom, prof, classe, specificite_salle):
		self._prof = prof
		self._nom = nom
		self._classe = classe
		self._specificite_salle = specificite_salle
		self._creneau = None
		self._salle = None
	
	def get_prof(self): 
		return self._prof
	def get_classe(self): 
		return self._classe

class Professeur(object):
	"""docstring for Professeur"""
	def __init__(self,nom, creneau_indispo):
		self._creneau_indispo= creneau_indispo
		self._nom = nom	
	
	def get_nom(self): 
		return self._nom
	def get_creneau_indispo(self): 
		return self._creneau_indispo


class Salle(object):
	"""docstring for Salle"""
	def __init__(self, nom_salle, caracteristique_salle):
		self._nom_salle = nom_salle
		self._caracteristique_salle = caracteristique_salle
	def get_nom_salle(self): 
		return self._nom_salle
	def get_type_salle(self): 
		return self._caracteristique_salle


class Creneaux(object):
	"""docstring for Creneaux"""
	def __init__(self, identifiant, jour, heure_debut):
		self._identifiant = identifiant
		self._jour = jour
		self._heure_debut = heure_debut
	


class Classe(object):
	"""docstring for Classe"""
	def __init__(self,nom,creneaux_indisponible):
		self._creneaux_indisponible = creneaux_indisponible
		self._nom = nom
		

class Data(object):
	"""docstring for Data"""
	



	def __init__(self):
		#Creation salles
		Salle201A = Salle("201A", "Miage")
		Salle201B = Salle("201B", "Miage")
		Salle401 = Salle("401","Blanche")
		#Creation crenaux
		Creneau1 = Creneaux("1","lundi","8h30");Creneau2 = Creneaux("2","lundi","10h30");Creneau3 = Creneaux("3","lundi","14h");Creneau4 = Creneaux("4","lundi","16h")
		Creneau5 = Creneaux("5","mardi","8h30");Creneau6 = Creneaux("6","mardi","10h30");Creneau7 = Creneaux("7","mardi","14h");Creneau8 = Creneaux("8","mardi","16h")
		Creneau9 = Creneaux("9","mercredi","8h30");Creneau10 = Creneaux("10","mercredi","10h30");Creneau11 = Creneaux("11","mercredi","14h");Creneau12 = Creneaux("12","mercredi","16h")
		Creneau13 = Creneaux("13","jeudi","8h30");Creneau14 = Creneaux("14","jeudi","10h30");Creneau15 = Creneaux("15","jeudi","14h");Creneau16 = Creneaux("16","jeudi","16h")
		Creneau17 = Creneaux("17","vendredi","8h30");Creneau18 = Creneaux("18","vendredi","10h30");Creneau19 = Creneaux("19","vendredi","14h");Creneau20 = Creneaux("20","vendredi","16h")
		CreneauVide = Creneaux("vide", "vide", "vide")
		#Creation prof
		Hillah= Professeur("Hillah",[Creneau11,Creneau12])
		Macone= Professeur("Macone",[Creneau15,Creneau16])
		Gervais= Professeur("Gervais",[Creneau17,Creneau18])
		Legond= Professeur("Legond",[Creneau13,Creneau14])
		Rukoz= Professeur("Rukoz",[Creneau9,Creneau10])
		Guehis= Professeur("Guehis",[Creneau9,Creneau10])
		Quinio= Professeur("Quinio",[Creneau5,Creneau6])
		Lebarbier= Professeur("Lebarbier",[Creneau1,Creneau2])
		Leloir= Professeur("Leloir",[Creneau3,Creneau4])
		Naudin= Professeur("Naudin",[Creneau15,Creneau16])
		Coneau= Professeur("Coneau",[Creneau5,Creneau6])
		#Creation des classe
		M2APP = Classe("M2APP",[CreneauVide])
		M2CLA = Classe("M2CLA",[Creneau1,Creneau2,Creneau3,Creneau4,Creneau5,Creneau6,Creneau7,Creneau8])
		#Creation des cours
		FSRAPP1= Cours("FSRAPP1",Gervais,M2APP,"Miage")
		FSRAPP2= Cours("FSRAPP2",Gervais,M2APP,"Miage")
		FSRCLA= Cours("FSRCLA",Gervais,M2CLA,"Miage")
		SSIAPP1= Cours("SSIAPP1",Legond,M2APP,"Miage")
		SSIAPP2= Cours("SSIAPP2",Legond,M2APP,"Miage")
		SSICLA= Cours("SSICLA",Legond,M2CLA,"Miage")
		TDMAPP1= Cours("TDMAPP1",Rukoz,M2APP,"Miage")
		TDMAPP2= Cours("TDMAPP2",Rukoz,M2APP,"Miage")
		TDMCLA= Cours("TDMCLA",Rukoz,M2CLA,"Miage")
		ASICAPP1= Cours("ASICAPP1",Hillah,M2APP,"Miage")
		ASICAPP2= Cours("ASICAPP2",Hillah,M2APP,"Miage")
		ASICCLA= Cours("ASICCLA",Hillah,M2CLA,"Miage")
		TRANS_DIGI_APP1= Cours("TRANS_DIGI_APP1",Quinio,M2APP,"Miage")
		TRANS_DIGI_APP2= Cours("TRANS_DIGI_APP2",Quinio,M2APP,"Miage")
		TRANS_DIGI_CLA= Cours("TRANS_DIGI_CLA",Quinio,M2CLA,"Miage")
		DATA_ANALYSE_APP= Cours("DATA_ANALYSE_APP",Guehis,M2APP,"Miage")
		DATA_ANALYSE_CLA= Cours("DATA_ANALYSE_CLA",Guehis,M2CLA,"Miage")
		DATA_MINING_APP= Cours("DATA_MINING_APP",Lebarbier,M2APP,"Miage")
		DATA_MINING_CLA= Cours("DATA_MINING_CLA",Lebarbier,M2CLA,"Miage")
		ANGLAIS_APP= Cours("ANGLAIS_APP",Macone,M2APP,"Blanche")
		ANGLAIS_CLA= Cours("ANGLAIS_CLA",Coneau,M2CLA,"Blanche")
		ENTREPR_APP= Cours("ENTREPR_APP",Naudin,M2APP,"Blanche")
		ENTREPR_CLA= Cours("ENTREPR_CLA",Naudin,M2CLA,"Blanche")
		DROIT_APP= Cours("DROIT_APP",Leloir,M2APP,"Blanche")
		DROIT_CLA= Cours("DROIT_CLA",Leloir,M2CLA,"Blanche")
		self._salles = [Salle201A,Salle201B]
		self._creneaux = [Creneau1,Creneau2,Creneau3,Creneau4,Creneau5,Creneau6,Creneau7,Creneau8,Creneau9,Creneau10,
		Creneau11,Creneau12,Creneau13,Creneau14,Creneau15,Creneau16,Creneau17,Creneau18,Creneau19,Creneau20]
		self._profs = [Hillah,Macone,Gervais,Legond,Rukoz,Guehis,Quinio,Lebarbier,Leloir,Naudin,Coneau]
		self._classes =[FSRAPP1,FSRAPP2,FSRCLA,SSIAPP1,SSIAPP2,SSICLA,TDMAPP1,TDMAPP2,
		TDMCLA,ASICAPP1,ASICAPP2,ASICCLA,TRANS_DIGI_APP1,TRANS_DIGI_APP2,TRANS_DIGI_CLA,
		DATA_ANALYSE_APP,DATA_ANALYSE_CLA,DATA_MINING_CLA,ANGLAIS_APP,ANGLAIS_CLA,ENTREPR_APP,ENTREPR_CLA,
		DROIT_APP,DROIT_CLA]
		self.nombre_classe = len(self._classes)+1
		print(self.nombre_classe)

		#print(Salle201A._caracteristique_salle)
		#print(Salle201A._nom_salle)
		

class EDT(object):
			"""docstring for EDT"""
			def __init__(self):
				self._data = data
				self._classes = []
				self._nbrconflits = 0
				
				

			def creer_edt(self):
				cours_data = data._classes

				for i in range(0, len(cours_data)):
					cours_temp = Cours(cours_data[i]._nom,cours_data[i]._prof, cours_data[i]._classe, cours_data[i]._specificite_salle)
					cours_temp._salle = data._salles[rnd.randrange(0, len(data._salles))]
					#print(clas._salle._nom_salle)
					cours_temp._creneau = data._creneaux[rnd.randrange(0, len(data._creneaux))]
					#print(cours_temp._creneau._jour + ":" + cours_temp._creneau._heure_debut )
					self._classes.append(cours_temp)
				return self


			def fitness_fonction(self):
				self._nbrconflits = 0
				cours_pour_calcul = self._classes
				for i in range(0,len(cours_pour_calcul)):
					#test H4
					if (cours_pour_calcul[i]._salle._caracteristique_salle != cours_pour_calcul[i]._specificite_salle):
						self._nbrconflits +=1
					if (cours_pour_calcul[i]._creneau in cours_pour_calcul[i]._prof._creneau_indispo) :
						self._nbrconflits +=1
					if (cours_pour_calcul[i]._creneau in cours_pour_calcul[i]._classe._creneaux_indisponible):
						self._nbrconflits +=1
					for j in range(0, len(cours_pour_calcul)):
						if j >= i:
							if(cours_pour_calcul[i]._creneau == cours_pour_calcul[j]._creneau and cours_pour_calcul[j] != cours_pour_calcul[i]):
								if  cours_pour_calcul[i]._salle == cours_pour_calcul[j]._salle: self._nbrconflits =+1
								if cours_pour_calcul[i]._prof == cours_pour_calcul[j]._prof: self._nbrconflits =+1
								if cours_pour_calcul[i]._classe == cours_pour_calcul[j]._classe: self._nbrconflits=+1
									

				return self


				
class Individus(object):
	"""docstring for Individus"""
	def __init__(self, taille):
		self._taille = taille
		self._data = data
		self._edt = []
		for x in range(0,taille):
			edt_temp = EDT().creer_edt().fitness_fonction()
			self._edt.append(edt_temp)
		
		



						
data = Data()
edt=EDT()
numero_generation=0
print("Numero generation" + str(numero_generation))
individus = Individus(20)
individus._edt.sort(key=lambda x: x._nbrconflits)
#sorted(individus._edt, key=lambda edt_1: edt_1._nbrconflits)
print(individus._edt[0]._nbrconflits)
print(individus._edt[1]._nbrconflits)
print(individus._edt[2]._nbrconflits)
edt.creer_edt()	
edt.fitness_fonction()	
#print("bonjour")
		







