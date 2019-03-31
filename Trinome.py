
try :
	from math import * 
	import os
	import pygame
	import sys
except ImportError :
	print("Erreur Importation !")

pygame.init()
LARGEUR, HAUTEUR = 1000,1000

screenSize = (LARGEUR, HAUTEUR)
#screen = pygame.display.set_mode(screenSize)

Blanc = (255,255,255)
Rouge = (255,0,0)
Gris = (215,215,215)
VertFond = (100,145,100)
Noir = (0,0,0)
BleuTresFonce = (2,6,17)

maFont = pygame.font.SysFont("comicsansms" , 10) 
texte = maFont.render("F11/F12 = Minimum/Maximum", True, Noir)  

i = float(-LARGEUR/2)

a = float()
b = float()
c = float()

listeDesPoints = []
listeDesResultats = []

minimum = 0
maximum = 0

def  demanderA():
	''' Demande la valeur de 'a' à l'utilisateur '''

	a = input("Quelle la valeur de a ?\n")

	try :
		a = float(a)
	except:
		demanderA()
	else :
		return a	

def  demanderB():
	''' Demande la valeur de 'b' à l'utilisateur '''

	b = input("Quelle la valeur de b ?\n")

	try :
		b = float(b)
	except:
		demanderB()
	else :
		return b	

def  demanderC():
	''' Demande la valeur de 'a' à l'utilisateur '''

	c = input("Quelle la valeur de c ?\n")

	try :
		c = float(c)
	except:
		demanderC()
	else :
		return c

def demanderABC() :
	''' reunit les fonction "demanderA", "demanderB" et "demanderC"	'''

	a = demanderA()
	b = demanderB()
	c = demanderC()

	return a,b,c


def drawAxeXEtAxeY(ecran):

	''' Dessine les axe X et Y sur l'ecran '''

	axeXRect = pygame.Rect((0, HAUTEUR/2), (LARGEUR, 1))
	axeYRect = pygame.Rect((LARGEUR/2, 0), (HAUTEUR, 1))
	axeYRect.h = HAUTEUR
	axeYRect.w = 1
	axeYRect.x = LARGEUR/2
	axeYRect.y = 0

	pygame.draw.rect(ecran, Noir, axeXRect)
	pygame.draw.rect(ecran, Noir, axeYRect) 

def drawUnPoint(fonction, espace, ecran):
	
	'''Affiche chaque point qui a pour  coordonées(i , fonction.fDeX(i)), -LARGEUR/2 < i < LARGEUR/2. '''

	global i
	global listeDesPoints

	point = pygame.draw.rect(ecran, BleuTresFonce, [(i + LARGEUR/2 , fonction.fDeX(i)),(1,1)])
	listeDesPoints.append(point)
	pygame.display.update()	
	i += espace


class FonctionLineaire():

	def __init__(self,aChoisi,bChoisi) :

		self._a = aChoisi
		self._b = bChoisi

		self.formeDeveloppee = str(self._a)+"x + ("+str(self._b)+")"

	def afficherForme(self):
		
		print("Forme Développée = "+self.formeDeveloppee)	

	def fDeX(self, x):

		''' calcul f(x) avec f = forme developpée + return la position du point par rapport aux centres
		des	axes X et Y'''

		resultat = self._a*x + self._b

		if resultat > 0 :
			resultat = HAUTEUR/2 - resultat
			return resultat
		elif resultat < 0 :
			resultat = HAUTEUR/2 - resultat
			return resultat
		elif resultat == 0 :
			return resultat		

	def trouverMin(self):
		print("N\' a pas de minimum")

	def trouverMax(self):
		print("N\' a pas de maximum")			


class FonctionTrinome():
	
	def __init__(self, aChoisi, bChoisi, cChoisi):

		''' Class definissant une fonction polynome de degré 2'''

		self._a = aChoisi
		self._b = bChoisi
		self._c = cChoisi

		self._delta = self._b*self._b - (4*self._a*self._c)
		self._alpha = -self._b/(2*self._a)
		self._beta = -self._delta/(4*self._a)

		self.formeFactorisee = ""
		self.formeCanonique = ""
		self.formeDeveloppe = str(self._a)+"x² + (" + str(self._b) + ("x) + (") + str(self._c)+")"


	def setFormeFactorisee(self):

		''' Definit la forme factorisée de la fonction grace à "a", "b" et "c" '''

		solution1 = float()
		solution2 = float()
	
		if self._delta < 0:
			self.formeFactorisee = "Non possible dans l\'ensemble des réels"

		elif self._delta == 0:

			solution1 = -self._b/(2*self._a)
			self.formeFactorisee = str(self._a)+"(x "+str(-solution1)+")²"

		elif self._delta > 0:

			solution1 =	(-self._b - sqrt(self._delta))/(2*self._a)

			solution2 = (-self._b + sqrt(self._delta))/(2*self._a)

			self.formeFactorisee = str(self._a)+"(x -("+str(-solution1)+"))(x -("+str(-solution2)+"))"

		else :
			print("Wtf")


	def setFormeCanonique(self):
		
		''' Definit la forme canonique de la fonction grace à "a", "b" et "c" '''

		self.formeCanonique = str(self._a)+"(x - ("+str(-self._alpha)+"))² + ("+str(self._beta)+")"


	def afficherFormes(self):

		''' Affiche les 3 formes de la fonction sur la console '''

		print("Forme développée = ", self.formeDeveloppe)
		print("Forme factorisee = ", self.formeFactorisee)
		print("Forme canonique = ", self.formeCanonique)

	def fDeX(self, x):

		''' calcul f(x) avec f = forme developpée + return la position du point par rapport aux centres
		des	axes X et Y'''

		resultat = self._a*(x*x) + self._b*x + self._c
		listeDesResultats.append(resultat)

		if resultat > 0 :
			resultat = HAUTEUR/2 - resultat
			return resultat
		elif resultat < 0 :
			resultat = HAUTEUR/2 - resultat
			return resultat
		elif resultat == 0 :
			return resultat		

		#return self._a*(x*x) + self._b*x + self._c
	
	def trouverMax(self):
		''' Calcul le max de la fonction '''
		maximum = listeDesResultats[0]

		if self._a < 0 :
			for resultat in listeDesResultats :
				if resultat > maximum :
					maximum = resultat
			print("Maximum = ",maximum)
		else :
			print("N\' a pas de maximum")	

	def trouverMin(self):
		''' calcul le min de la fonction '''
		minimum = listeDesResultats[0]

		if self._a > 0 :
			for resultat in listeDesResultats :
				if resultat < minimum :
					minimum = resultat	

			print("Minimum = ",minimum)
		else :
			print("N\'a pas de minimum")				


def quitter():
	''' fonction pour quitter le programme '''

	pygame.quit()
	sys.exit()

def main():

	try :
		a, b, c = demanderABC()
	except :
		print("N\'a pas pu saisir la/les valeurs de a, b ou/et c ")
		

	if a != 0:	
		fonction = FonctionTrinome(a,b,c)

		fonction.setFormeCanonique()
		fonction.setFormeFactorisee()

		fonction.afficherFormes()

	else:
		fonction = FonctionLineaire(b,c)

		fonction.afficherForme()	


	screen = pygame.display.set_mode(screenSize)
	screen.fill(VertFond)
	drawAxeXEtAxeY(screen)
	pygame.display.update()
	screen.blit(texte, (3,3))

	while True : 

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitter()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F11:
					fonction.trouverMin()	
				elif event.key == pygame.K_F12:
					fonction.trouverMax()

		if i <= LARGEUR/2 :		
			drawUnPoint(fonction, 0.5, screen)
		else :
			pass
			#detruireLesPoints()			

		pygame.display.update()		


try :
	main()	
except BaseException as exp :
	print(exp)
	os.system("pause")	



