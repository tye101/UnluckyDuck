import pygame
import random
import pygame.mixer
from pygame.locals import *

pygame.init()

pygame.mixer.init()
#sets music
sound = pygame.mixer.Sound("coinsound.wav")
sound.set_volume(1.0)

music = pygame.mixer.Sound("music.wav")
music.set_volume(0.025)

gameOverMusic = pygame.mixer.Sound("gameovermusic.wav")
gameOverMusic.set_volume(0.5)
pygame.font.init()
font = pygame.font.Font(None, 60)



#loads image of bird
bird = pygame.image.load("birdie.py")
birdX = 400
birdY = 470
bird = pygame.transform.scale(bird,(150,150))
bird_left = bird
bird_right = pygame.transform.flip(bird,True,False)

#loads image of dead bird
deadbird = pygame.image.load("deadbirdie.gif")
deadbirdX = -200
deadbirdY = -500
deadbird = pygame.transform.scale(deadbird,(1250,1250))
deadbird = pygame.transform.rotate(deadbird, 30)

#loads image of coin
coin = pygame.image.load("coin.py")
coin = pygame.transform.scale(coin,(385,120))
coinY = 485
coinX = random.randint (0,800)

coinWidth, coinHeight = coin.get_size()
coin_Width = coinWidth/6
coin_Height = coinHeight/6
coinPic = []
for i in range(6):
	coinPic.append (coin.subsurface(i*coin_Width,0, coin_Width, coinHeight)) 

#loads image of fireball
fireball = pygame.image.load("fireball.py")
fireball = pygame.transform.scale(fireball,(75,75))
fireballX = random.randint (0,800)
fireballY = 0
speed = 8

#loads image of the ground
back = pygame.image.load("cloudBackground.py")
back = pygame.transform.scale(back,(1000,650))
backX = 0
backY = 0


#sets opening screen
width = 820
height = 640
size = width, height		
screen = pygame.display.set_mode(size)
blue = 100,149,237
black = 0,0,0
screen.fill(black)
pygame.display.flip()

#title
title = font.render("UNLUCKY DUCK", False, (255,255,255))

#instructions
instructions = font.render("collect coins and dodge fireballs",False, (255,255,255))
#start
start = font.render ("PRESS SPACE BAR TO START", False, (255,255,255))
#you died
death = font.render ("YOU DIED", False, (255,255,255))




gameOver = False
gameOn = False
quit = False
titlescreenOn = True
#Front page
while titlescreenOn:
	music.play()
	screen.blit(start, (50,400))
	screen.blit(title, (300, 300))
	screen.blit(instructions, (10,350))
	pygame.display.flip() 
	
	
	for event in pygame.event.get():
		if event.type == QUIT: 
			gameOn =True
			quit = True
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				gameOn = True
				titlescreenOn = False

if quit == True:
	pygame.quit()
coins = 0
coinCount = 0
while gameOn:
	for event in pygame.event.get():
		if event.type == QUIT:
			quit = True
			gameOn = False   
		if event.type == KEYDOWN:
			    
			
			if event.key == K_RIGHT:      #walk right
				birdX = birdX +  50
				bird = bird_right
				    
				   
			elif event.key == K_LEFT:
				birdX = birdX - 50
				bird = bird_left

			

			
	

	fireballY = fireballY + speed
	if fireballY == 640:
		fireballY = 0
		fireballX = random.randint(0,800)
		
	if fireballY >= birdY and birdX >= fireballX - 50 and birdX <= fireballX + 10: 
		gameOver = True
		gameOn = False

		
	if birdX >= coinX - 35 and birdX <= coinX + 15:
		coins = coins + 1
		coinX = random.randint(0,800)
		sound.play()
	

	screen.blit(back,(backX,backY))
	screen.blit(bird,(birdX,birdY))              # put bird at new coords
	screen.blit(fireball,(fireballX,fireballY))
	screen.blit(coinPic[coinCount], (coinX, coinY))
	coinCount = coinCount + 1	
	pygame.display.flip()			 # flip screen onto window 

	coinCount = coinCount + 1
	if coinCount ==  4:
		coinCount = 0	


if quit == True:
	pygame.quit()
	
while gameOver:	

	music.stop()
	gameOverMusic.play()
	coins = str(coins)
	score2 = font.render(coins, False, (255,255,255))
	score1 = font.render("COLLECTED", False, (255,255,255))
	screen.blit(score1,(200,400))
	screen.blit(score2,(10,400))
	score3 = font.render("COINS", False, (255,255,255))
	screen.blit(score3,(50,400))	
	screen.blit(deadbird,(deadbirdX,deadbirdY)) 
	screen.blit(death, (25,100))	

	pygame.display.flip()
	screen.fill(blue)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
pygame.quit()
