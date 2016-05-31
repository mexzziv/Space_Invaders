#desarrollo de juego en pygame Space Invader

import pygame,sys
from pygame.locals import*

from clases import Nave
from clases import Invasor as Enemigo

#variables globales
ancho = 900
alto = 480
listaEnemigos = []

def detenerTodo():
	for enemigo in listaEnemigos:
		for disparo in enemigo.listaDisparo:
			enemigo.listaDisparo.remove(disparo)

		enemigo.conquista = True

def cargarEnemigos():
	posx = 100
	for x in range(1,5):
		enemigo = Enemigo(posx,100,40,'imagen/MarcianoA.jpg','imagen/MarcianoB.jpg')
		listaEnemigos.append(enemigo)
		posx = posx + 200

	posx = 100
	for x in range(1,5):
		enemigo = Enemigo(posx,0,40,'imagen/Marciano2A.jpg','imagen/Marciano2B.jpg')
		listaEnemigos.append(enemigo)
		posx = posx + 200

	posx = 100
	for x in range(1,5):
		enemigo = Enemigo(posx,-100,40,'imagen/Marciano3A.jpg','imagen/Marciano3B.jpg')
		listaEnemigos.append(enemigo)
		posx = posx + 200

def SapceInvader():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Space Invader")

	ImagenFondo = pygame.image.load('imagen/Fondo.jpg')

	pygame.mixer.music.load('sonidos/intro.mp3')
	pygame.mixer.music.play(3)

	miFuenteSistema = pygame.font.SysFont("Arial",30)
	Texto = miFuenteSistema.render("Fin del Juego",0,(120,100,40))

	jugador = Nave.naveEspacial(ancho,alto)
	cargarEnemigos()

	#DemoProyectil = Proyectil(ancho/2, alto-30)

	enJuego = True
	reloj = pygame.time.Clock()

	while True:
		reloj.tick(60)

		tiempo = pygame.time.get_ticks()/1000

		#jugador.movimiento()
		#DemoProyectil.trayectoria()

		for evento in pygame.event.get():
			if evento == QUIT:
				pygame.quit()
				sys.exit()

			if enJuego == True:
				if evento.type == pygame.KEYDOWN:
					if evento.key == K_LEFT:
						#jugador.rect.left -= jugador.velocidad
						jugador.movimientoIzquierda()
					elif evento.key == K_RIGHT:
						#jugador.rect.right += jugador.velocidad
						jugador.movimientoDerecha()
					elif evento.key == K_s:
						#jugador.disparar()
						x,y = jugador.rect.center
						jugador.disparar(x,y)

		ventana.blit(ImagenFondo, (0,0))
		#DemoProyectil.dibujar(ventana)
		jugador.dibujar(ventana)
		if len(jugador.listaDisparo)>0:
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()

				if x.rect.top < -10:
					jugador.listaDisparo.remove(x)
				else:
					for enemigo in listaEnemigos:
						if x.rect.colliderect(enemigo.rect):
							listaEnemigos.remove(enemigo)
							jugador.listaDisparo.remove(x)

		if len(listaEnemigos)>0:
			for enemigo in listaEnemigos:
				enemigo.comportamiento(tiempo)
				enemigo.dibujar(ventana)

				if enemigo.rect.colliderect(jugador.rect):
					jugador.Destruccion
					enJuego = False
					detenerTodo()

				if len(enemigo.listaDisparo)>0:
					for x in enemigo.listaDisparo:
						x.dibujar(ventana)
						x.trayectoria()
						if x.rect.colliderect(jugador.rect):
							jugador.Destruccion()
							enJuego = False
							detenerTodo()

						if x.rect.top > 900:
							enemigo.listaDisparo.remove(x)
						else:
							for disparo in jugador.listaDisparo:
								if x.rect.colliderect(disparo.rect):
									jugador.listaDisparo.remove(disparo)
									enemigo.listaDisparo.remove(x)

		if enJuego == False:
			pygame.mixer.music.fadeout(3000)
			ventana.blit(Texto,(300,300))
		pygame.display.update()

SapceInvader()