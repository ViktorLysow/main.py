import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Grafik/hintergrund.png")
screen = pygame.display.set_mode([1200,595])
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Tutorial")

angriffLinks = pygame.image.load("Grafik/angriffLinks.png")
angriffRechts = pygame.image.load("Grafik/angriffRechts.png")
sprung = pygame.image.load("Grafik/sprung.png")
rechtsGehen = [pygame.image.load("Grafik/rechts1.png"),pygame.image.load("Grafik/rechts2.png"),pygame.image.load("Grafik/rechts3.png"),pygame.image.load("Grafik/rechts4.png"),pygame.image.load("Grafik/rechts5.png"),pygame.image.load("Grafik/rechts6.png"),pygame.image.load("Grafik/rechts7.png"),pygame.image.load("Grafik/rechts8.png")]
linksGehen = [pygame.image.load("Grafik/links1.png"),pygame.image.load("Grafik/links2.png"),pygame.image.load("Grafik/links3.png"),pygame.image.load("Grafik/links4.png"),pygame.image.load("Grafik/links5.png"),pygame.image.load("Grafik/links6.png"),pygame.image.load("Grafik/links7.png"),pygame.image.load("Grafik/links8.png")]
sprungSound = pygame.mixer.Sound("Sound/sprung.wav")

class spieler:
	def __init__(self,x,y,geschw,breite,hoehe,sprungvar,richtg,schritteRechts,schritteLinks):
		self.x = x
		self.y = y
		self.geschw = geschw
		self.breite = breite
		self.hoehe = hoehe
		self.sprungvar = sprungvar
		self.richtg = richtg
		self.schritteRechts = schritteRechts
		self.schritteLinks = schritteLinks
		self.sprung = False
		self.last = [1,0]
		self.ok = True
	def laufen(self,liste):
		if liste[0]:
			self.x -= self.geschw
			self.richtg = [1,0,0,0]
			self.schritteLinks += 1
		if liste[1]:
			self.x += self.geschw
			self.richtg = [0,1,0,0]
			self.schritteRechts += 1
	def resetSchritte(self):
		self.schritteLinks = 0
		self.schritteRechts = 0
	def stehen(self):
		self.richtg = [0,0,1,0]
		self.resetSchritte()
	def sprungSetzen(self):
		if self.sprungvar == -16:
			self.sprung = True
			self.sprungvar = 15
			pygame.mixer.Sound.play(sprungSound)
	def springen(self):
		if self.sprung:
			self.richtg = [0,0,0,1]
			if self.sprungvar >= -15:
				n = 1
				if self.sprungvar < 0:
					n = -1
				self.y -= (self.sprungvar**2)*0.17*n
				self.sprungvar -= 1
			else:
				self.sprung = False
	def spZeichnen(self):
		if self.schritteRechts == 63:
			self.schritteRechts = 0
		if self.schritteLinks == 63:
			self.schritteLinks = 0

		if self.richtg[0]:
			screen.blit(linksGehen[self.schritteLinks//8], (self.x,self.y))
			self.last = [1,0]

		if self.richtg[1]:
			screen.blit(rechtsGehen[self.schritteRechts//8], (self.x,self.y))
			self.last = [0,1]

		if self.richtg[2]:
			if self.last[0]:
				screen.blit(angriffLinks, (self.x,self.y))
			else:
				screen.blit(angriffRechts, (self.x,self.y))

		if self.richtg[3]:
			screen.blit(sprung, (self.x,self.y))

class kugel:
	def __init__(self,spX,spY,richtung,radius,farbe,geschw):
		self.x = spX
		self.y = spY
		if richtung[0]:
			self.x += 5
			self.geschw = -1 * geschw
		elif richtung[1]:
			self.x += 92
			self.geschw = geschw
		self.y += 84
		self.radius = radius
		self.farbe = farbe
	def bewegen(self):
		self.x += self.geschw
	def zeichnen(self):
		pygame.draw.circle(screen, self.farbe, (self.x, self.y), self.radius, 0)

class zombie:
	def __init__(self,x,y,geschw,breite,hoehe,richtg,xMin,xMax):
		self.x = x
		self.y = y
		self.geschw = geschw
		self.breite = breite
		self.hoehe = hoehe
		self.richtg = richtg
		self.schritteRechts = 0
		self.schritteLinks = 0
		self.xMin = xMin
		self.xMax = xMax
		self.leben = 6
		self.linksListe = [pygame.image.load("Grafik/l1.png"), pygame.image.load("Grafik/l2.png"),
						   pygame.image.load("Grafik/l3.png"), pygame.image.load("Grafik/l4.png"),
						   pygame.image.load("Grafik/l5.png"), pygame.image.load("Grafik/l6.png"),
						   pygame.image.load("Grafik/l7.png"), pygame.image.load("Grafik/l8.png")]

		self.rechtsListe = [pygame.image.load("Grafik/R1.png"), pygame.image.load("Grafik/R2.png"),
							pygame.image.load("Grafik/R3.png"), pygame.image.load("Grafik/R4.png"),
							pygame.image.load("Grafik/R5.png"), pygame.image.load("Grafik/R6.png"),
							pygame.image.load("Grafik/R7.png"), pygame.image.load("Grafik/R8.png")]

		self.ganz = pygame.image.load("Grafik/voll.png")
		self.halb = pygame.image.load("Grafik/halb.png")
		self.leer = pygame.image.load("Grafik/leer.png")
	def herzen(self):
		if self.leben >= 2:
			screen.blit(self.ganz, (507,15))
		if self.leben >= 4:
			screen.blit(self.ganz, (569,15))
		if self.leben == 6:
			screen.blit(self.ganz, (631,15))

		if self.leben == 1:
			screen.blit(self.halb, (507,15))
		elif self.leben == 3:
			screen.blit(self.halb, (569,15))
		elif self.leben == 5:
			screen.blit(self.halb, (631,15))

		if self.leben <= 0:
			screen.blit(self.leer, (507,15))
		if self.leben <= 2:
			screen.blit(self.leer, (569,15))
		if self.leben <= 4:
			screen.blit(self.leer, (631,15))
	def zZeichnen(self):
		if self.schritteRechts == 63:
			self.schritteRechts = 0
		if self.schritteLinks == 63:
			self.schritteLinks = 0

		if self.richtg[0]:
			screen.blit(self.linksListe[self.schritteLinks//8], (self.x,self.y))
		if self.richtg[1]:
			screen.blit(self.rechtsListe[self.schritteRechts//8], (self.x,self.y))
	def Laufen(self):
		self.x += self.geschw
		if self.geschw > 0:
			self.richtg = [0,1]
			self.schritteRechts += 1
		if self.geschw < 0:
			self.richtg = [1,0]
			self.schritteLinks += 1
	def hinHer(self):
		if self.x > self.xMax:
			self.geschw *= -1
		elif self.x < self.xMin:
			self.geschw *= -1
		self.Laufen()

def zeichnen():
	screen.blit(hintergrund, (0,0))
	for k in kugeln:
		k.zeichnen()
	spieler1.spZeichnen()
	zombie1.zZeichnen()
	zombie1.herzen()
	pygame.display.update()

def kugelHandler():
	global kugeln
	for k in kugeln:
		if k.x >= 0 and k.x <= 1200:
			k.bewegen()
		else:
			kugeln.remove(k)

def Kollision():
	global kugeln
	zombieRechteck = pygame.Rect(zombie1.x+18,zombie1.y+24,zombie1.breite-36,zombie1.hoehe-24)

	for k in kugeln:
		kugelRechteck = pygame.Rect(k.x-k.radius,k.y-k.radius,k.radius*2,k.radius*2)
		if zombieRechteck.colliderect(kugelRechteck):
			kugeln.remove(k)
			zombie1.leben -= 1

linkeWand = pygame.draw.rect(screen, (0,0,0), (-2,0,2,600), 0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1201,0,2,600), 0)
spieler1 = spieler(300,393,5,96,128,-16,[0,0,1,0],0,0)
zombie1 = zombie(600,393,4,96,128,[0,0],40,1090)
kugeln = []
go = True
while go:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,96,128)
	gedrueckt = pygame.key.get_pressed()

	if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
		spieler1.laufen([0,1])
	elif gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
		spieler1.laufen([1,0])
	else:
		spieler1.stehen()

	if gedrueckt[pygame.K_UP]:
		spieler1.sprungSetzen()
	spieler1.springen()

	if gedrueckt[pygame.K_SPACE]:
		if len(kugeln) <= 4 and spieler1.ok:
			kugeln.append(kugel(round(spieler1.x),round(spieler1.y),spieler1.last,8,(0,0,0),7))
		spieler1.ok = False

	if not gedrueckt[pygame.K_SPACE]:
		spieler1.ok = True

	kugelHandler()
	zombie1.hinHer()

	Kollision()
	zeichnen()
	clock.tick(60)