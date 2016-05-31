import pygame
import Proyectil

class naveEspacial(pygame.sprite.Sprite):

	def __init__(self,ancho,alto):
		pygame.sprite.Sprite.__init__(self)
		self.ImageNave = pygame.image.load('imagen/nave.jpg')
		self.ImageExplosion = pygame.image.load('imagen/explosion.jpg')

		self.rect = self.ImageNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto-30

		self.listaDisparo = []
		self.Vida = True

		self.velocidad = 20

		#self.sonidoDisparo = pygame.mixer.Sound('sonidos/disparo.mp3')
		#self.sonidoExplosion = pygame.mixer.sound('sonidos/explosion.mp3')

	def movimientoDerecha(self):
		self.rect.right += self.velocidad
		self.__movimiento()

	def movimientoIzquierda(self):
		self.rect.left -= self.velocidad
		self.__movimiento()

	def __movimiento(self):
		if self.Vida == True:
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right>870:
				self.rect.right = 840

	def disparar(self,x,y):
		#print "Disparo"
		miProyectil = Proyectil.Proyectil(x,y,"imagen/disparoa.jpg",True)
		self.listaDisparo.append(miProyectil)
		#self.sonidoDisparo.play()

	def Destruccion(self):
		#self.sonidoExplosion.play()
		self.Vida = False
		self.velocidad = 0
		self.ImageNave = self.ImageExplosion

	def dibujar(self, superficie):
		superficie.blit(self.ImageNave, self.rect)