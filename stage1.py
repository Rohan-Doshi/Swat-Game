import pygame,sys,random    #to import required modules
from pygame.locals import*	#to use some constants such as quit and k_up

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
BROWN=(150,50,0)
FPS=60
global fb
fb=0
keys={"player_up":False,"welcome":False,"playerdash":False,"continue":False,"pause":False}
intro=[]
flag=0
pygame.init()
#set clock screen and its caption
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
pygame.display.set_caption('swat kat')
rect_image=pygame.image.load('blackbar.png')
back1=pygame.image.load("welc.png")
back2=pygame.image.load("back_final.jpg")
lost=pygame.image.load("lost.png")


clock = pygame.time.Clock()
intro1=pygame.image.load("s1.png")
intro.append(intro1)
intro2=pygame.image.load("s2.png")
intro.append(intro2)
intro3=pygame.image.load("s3.png")
intro.append(intro3)
intro4=pygame.image.load("s4.png")
intro.append(intro4)
intro5=pygame.image.load("s5.png")
intro.append(intro5)




player=pygame.image.load("Fighter.png")
playerrect=player.get_rect()
playerrect.width=playerrect.width-50
playerrect.height=playerrect.height-10



rect_list=[]
rect_list1=[]

def playerHasHitPipe(playerRect, pipe):
	for p in pipe:
		if playerRect.colliderect(p):
			return True
		#if playerRect.colliderect(p['rect2']):
			#return True 
	return False

#---------------------------------------build obstacles-----------------------------
def getrect():
	i=0
	j=60
	k=0
	#screen.fill((0,255,255))
	start=1366
	max=60
	
	
	#For Upward
	
	while k<300:	
		if(i<max/2):
			j=j+4
			i+=1
			start+=5
			rect_list.append(pygame.Rect([start,0,10,j]))
			
		elif (i<max):
			j=j-4
			i+=1
			start+=5
			rect_list.append(pygame.Rect([start,0,10,j]))
			
		if(i==max):
			max=random.randrange(20,120)
			i=0
			j=60
			
		k=k+1
	
	
	
	
	#for Downward 
	i=0
	j=700
	k=0
	#screen.fill((0,255,255))
	start=1336
	max=60
	
	
	while k<300:	
		if(i<max/2):
			j=j-4
			i+=1
			start+=5
			rect_list1.append(pygame.Rect([start,j,10,768]))
			
		elif (i<max):
			j=j+4
			i+=1
			start+=5
			rect_list1.append(pygame.Rect([start,j,10,768]))
			
		if(i==max):
			max=random.randrange(20,150)
			i=0
			j=700
			
		k=k+1

#-------------------------------------------------------------------------


#--------------------------------------------Gameloop-------------------------

def Gameloop():

	
	player_x=224
	score_ref=player_x
	player_y=500
	speed=10
	spd=0	
	s1=0

	change_up=10
	change_down=5	
	getrect()
	score=0			
	i=0
	t=0
	
	while True:
		#getrect()
		font=pygame.font.Font(None,30)
		font1=pygame.font.Font(None,50)
		text=font.render("Score : %s"%(score),True,GREEN)
		text1=font.render("New map is Generated dynamically in accordance with player's skill set",True,RED)
		text2=font.render("the speed of the sprite is increased in accordance with the score",True,GREEN)
		text3=font.render("the difficulty level is increased in accordance with player's skill set",True,BLUE)
		text4=font1.render("PAUSED",True,WHITE)
		
		#	screen.fill(WHITE)
		screen.blit(back2,(0,0))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
				
			if(event.type==pygame.KEYDOWN):
				if event.key==K_1:
				    keys["pause"]=True

				if event.key==K_2:
					keys["pause"]=False
				    
				elif event.key==K_UP:
				    keys["player_up"]=True
				    
				elif event.key==K_SPACE:
				    keys["playerdash"]=True

				if event.key==K_ESCAPE:
					pygame.quit()
					sys.exit()
		    
				
				    
			elif(event.type==pygame.KEYUP):
				    
				if event.key==K_UP:
				    keys["player_up"]=False 
				    
				elif event.key==K_SPACE:
				    keys["playerdash"]=False            



	#pause
		if keys["pause"]:
			keys["player_up"]=False
			screen.blit(text4,[1366/2,768/2])
			continue
		
			
								
				
				
		    
		if keys["player_up"]:
			player_y-=change_up
		else:
			player_y+=change_down    
			

			
	#show list		
		for r in rect_list:
				r.move_ip(-1*speed,0)
			
		for r in rect_list[:]:
				if r.left<0:
					rect_list.remove(r)
	
		for r in rect_list:
				y=pygame.transform.scale(rect_image,(r.width,r.height))
				screen.blit(y,r)
				
	
	#show list1
			
		for r in rect_list1:
				r.move_ip(-1*speed,0)
			
		for r in rect_list1[:]:
				if r.left<0:
					rect_list1.remove(r)
	
		for r in rect_list1:
				y=pygame.transform.scale(rect_image,(r.width,r.height))
				screen.blit(y,r)				
				
		if player_y<=0:
			player_y=0
		
		elif player_y>=768-playerrect.height:
			player_y=768-playerrect.height								
				
	#increase speed

		if(spd==5):
			speed+=1
			spd=0	
			s1+=1

		if((score%5)==0):
			screen.blit(text2,[300,40])
			
		if((score%7)==0):
			screen.blit(text3,[300,70])

	#To print score and msg		
		i+=1
		t+=1

		if(t==50):
			score+=1
			spd+=1
			t=0
			
		if s1<12:
			if i>=150-12*s1:
				getrect()
				i=0
		else:
			getrect()
			i=0				

		if(i<30):
			screen.blit(text1,[300,10])

			
		
		screen.blit(text,[10,10])		
		
		playerrect.topleft=(player_x,player_y)
		screen.blit(player,playerrect)
		if playerHasHitPipe(playerrect,rect_list) or playerHasHitPipe(playerrect,rect_list1):
			keys["player_up"]=False
			global fb
			fb=0
			break
			
		
		pygame.display.update()
		
		clock.tick(FPS)

		if score>=10:
			global fb
			fb=1
			break

	
	#Game Over

		
#------------------------------------------------------------------------------------


#---------------------------------------Welcome screen-------------------

#-------------------------------------------------------------------------
Gameloop()

if fb==1:

	screen.fill((0,0,0))
	#screen=pygame.display.set_mode((1366,768))#,pygame.FULLSCREEN)

	for i in range(0,5):
		screen1=pygame.transform.scale(intro[i],(1080,560))
		screen.blit(screen1,(150,100))
		pygame.display.update()
		clock.tick(3)
		#print 1
	while 1:

		font1=pygame.font.Font(None,50)
		text=font1.render(" The protagonist comes out of the plane after crash",True,RED)
		text2=font1.render("now its time to face the villain",True,RED)

		for event in pygame.event.get():
				if event.type==QUIT:
					pygame.quit()
					sys.exit()

				if event.type==KEYDOWN:
					if event.key==K_ESCAPE:
						pygame.quit() 
						sys.exit()
					if event.key==K_RETURN:
						fb=0
						break 
		if fb==0:
			break
		screen.blit(text,[10,10])
		screen.blit(text2,[10,50])
		screen1=pygame.transform.scale(intro[i],(1080,560))
		screen.blit(screen1,(150,100))
		if flag==0:
			RED=(255,255,255)
			flag=1
		elif flag==1:
			RED=(255,0,0)
			flag=0
		clock.tick(1)
		pygame.display.update()
	import stage2

if(fb==0 or stage2.fb==0):
	while(True):

		screen.fill(0)
		screen.blit(lost,(180,0))
		font=pygame.font.Font(None,60)
		font2=pygame.font.Font(None,30)
		font1=pygame.font.Font(None, 100)

		
		


		text1=font1.render("GAME OVER !",True,RED)
		#text=font.render("Your Score is : %s"%(score),True,BLUE)
		text2=font2.render("Hit SPACE to continue..",True,BLUE)
		
	
		for event in pygame.event.get():
			if(event.type==pygame.KEYDOWN):
				if event.key==K_ESCAPE:
					pygame.quit()
					sys.exit()
	
				elif event.key==K_SPACE:
					keys["continue"]=True		    
	
		if keys["continue"]:
			keys["continue"]=False
			break

		screen.blit(text1,[1366/3,300])
		screen.blit(text2,[1366/2,500])
		#screen.blit(text,[500,400])
		pygame.display.update()	




