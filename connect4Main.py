import pygame
import time

h = 840 
l = 840
largeur_cases = l/7
hauteur_cases = h/7

pygame.init()
screen = pygame.display.set_mode((l, h))



##variables

continuer = 1
list_Rect_jetons = []
list_Rect_jetons_couleurs = []
list_corners = []
jeton_encours_rect = []
descente = 0
next_tour = 0
droit_modifier_couleur = 1


def tour(couleur_pale,couleur_foncee):
		global continuer,list_Rect_jetons,h,l,largeur_cases,hauteur_cases,list_corners,jeton_encours_rect,descente,next_tour,list_Rect_jetons_couleurs,droit_modifier_couleur,couleur_jeton_encours,couleur_pale_jeton_encours

	##screen set
		screen.fill((100,100,255))
		pygame.draw.rect(screen,(150,150,150),pygame.Rect(0,0,840,hauteur_cases))
		x,y = 0,hauteur_cases
		list_corners = []
		for colonne in range(1,7):
			for position in range(0,7):
				pygame.draw.rect(screen,(10,10,10),pygame.Rect(x,y,hauteur_cases,largeur_cases), 1)
				pygame.draw.circle(screen,(150,150,200),(x+largeur_cases/2,y+hauteur_cases/2),50)
				list_corners.append([x,y])
				x+=largeur_cases
			x = 0
			y+=hauteur_cases	
		compteur = 0
		for i in list_Rect_jetons:
			pygame.draw.circle(screen,list_Rect_jetons_couleurs[compteur],(i.x+largeur_cases/2,i.y+hauteur_cases/2),50)
			compteur += 1

		if descente != 1:
			posSouris = pygame.mouse.get_pos()
			jeton_encours_rect = pygame.Rect(posSouris[0],0,largeur_cases,hauteur_cases)
			for i in range(0,120):
				for e in range(0,len(list_corners)):
					if posSouris[0]-i == list_corners[e][0]:
						jeton_encours_rect.x = posSouris[0]-i
			pygame.draw.circle(screen,couleur_pale,(jeton_encours_rect.x+largeur_cases/2,jeton_encours_rect.y+hauteur_cases/2),50)
			
		else:

			pygame.draw.circle(screen,couleur_foncee,(jeton_encours_rect.x+largeur_cases/2,jeton_encours_rect.y+hauteur_cases/2),50)
			jeton_encours_rect.y += hauteur_cases
			time.sleep(0.05)


			if jeton_encours_rect.y == h:
				list_Rect_jetons.append(pygame.Rect(jeton_encours_rect.x,jeton_encours_rect.y-hauteur_cases,largeur_cases,hauteur_cases))
				list_Rect_jetons_couleurs.append(couleur_foncee)
				droit_modifier_couleur = 1
				descente = 0
				next_tour = 1
			if pygame.Rect.collidelist(jeton_encours_rect,list_Rect_jetons) != -1:
				list_Rect_jetons_couleurs.append(couleur_foncee)
				droit_modifier_couleur = 1
				list_Rect_jetons.append(pygame.Rect(jeton_encours_rect.x,jeton_encours_rect.y-120,largeur_cases,hauteur_cases))
				descente = 0
				next_tour = 1

			


while continuer == 1:
	next_tour = 0
	while next_tour == 0:
		next_tour = 0
		##rouge
		tour((200,100,100), (200,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONUP:
				descente = 1
		pygame.display.flip()

	next_tour = 0
	while next_tour == 0:
		next_tour = 0
		##blue
		tour((100,100,200), (0,0,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONUP:
				descente = 1

		pygame.display.flip()

