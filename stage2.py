import pygame,sys,random,time    #to import required modules
from pygame.locals import*	#to use some constants such as quit and k_up



BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
BROWN=(150,50,0)
YELLOW=(255,255,0)
FPS=60
fb=0


#---------------------------------------------------------------------------------------------------------------

class func:
	
	rect_x=0
	rect_x1=400+150
	rect_x2=rect_x1+400+150
	rect_x3=rect_x2+400+150
	rect_x4=rect_x3+400+150


	rect1_x=0
	rect1_x1=400+150
	rect1_x2=rect_x1+400+150
	rect1_x3=rect_x2+400+150
	rect1_x4=rect_x3+400+150
	

	rect_wid=400
	rect_wid1=400
	rect_wid2=400
	rect_wid3=400
	rect_wid4=400

	rect1_wid=400
	rect1_wid1=400
	rect1_wid2=400
	rect1_wid3=400
	rect1_wid4=400
	
	vill_health=0
	
	cat1=pygame.image.load('catch1.png')	
	cat2=pygame.image.load('catch2.png')
	cat3=pygame.image.load('catch3.png')
	
	bull_x=450+58	
	
	rect2_1=rect2_2=rect2_3=rect2_4=rect2_5=0
	rect1_1=rect1_2=rect1_3=rect1_4=rect1_5=0
	bull=0
	
	
	bullet=[]
	move =1366-150
	villain_player=[]
	hcnt=False
	vbullet=[]
	bull_pos=420
	flag =1	
	res=1366-150
	
	l=0
	u=0
	x=0
	w=0
	pos=0
	villain_player=0
	ring=0
	player_lives=10 
	powerup=0
	gp=0
	pwe=[]
	power=pygame.image.load('power.png')
	pox=1366
	def fun(x):
		font=pygame.font.Font(None,25)
		text=font.render("Player Lives=%d"%(func.player_lives),True,BLUE)	
		
		func.rect1_1=pygame.draw.rect(screen,YELLOW,[func.rect_x,func.rect_y,func.rect_wid,30])

		func.rect1_2=pygame.draw.rect(screen,YELLOW,[func.rect_x1,func.rect_y,func.rect_wid1,30])

		func.rect1_3=pygame.draw.rect(screen,YELLOW,[func.rect_x2,func.rect_y,func.rect_wid2,30])

		func.rect1_4=pygame.draw.rect(screen,YELLOW,[func.rect_x3,func.rect_y,func.rect_wid3,30])

		func.rect1_5=pygame.draw.rect(screen,YELLOW,[func.rect_x4,func.rect_y,func.rect_wid4,30])
	
		func.rect_x-=6
		func.rect_x1-=6
		func.rect_x2-=6
		func.rect_x3-=6
		func.rect_x4-=6
		

		if func.rect_x1<=-400:
			func.rect_x=func.rect_x4+func.rect_wid4+150
			#func.rect_wid=random.randrange(350,400)

		if func.rect_x2<=-400:
			func.rect_x1=func.rect_x+func.rect_wid+150
			#func.rect_wid1=random.randrange(350,400)

		if func.rect_x3<=-400:
			func.rect_x2=func.rect_x1+func.rect_wid1+150
			#func.rect_wid2=random.randrange(350,400)

		if func.rect_x4<=-400:
			func.rect_x3=func.rect_x2+func.rect_wid2+150
			#func.rect_wid3=random.randrange(350,400)

		if func.rect_x<=-400:
			func.rect_x4=func.rect_x3+func.rect_wid3+150
			#func.rect_wid4=random.randrange(350,400)



		#level2
		func.rect2_1=pygame.draw.rect(screen,YELLOW,[func.rect1_x,func.rect_y1,func.rect1_wid,30])

		func.rect2_2=pygame.draw.rect(screen,YELLOW,[func.rect1_x1,func.rect_y1,func.rect1_wid1,30])

		func.rect2_3=pygame.draw.rect(screen,YELLOW,[func.rect1_x2,func.rect_y1,func.rect1_wid2,30])

		func.rect2_4=pygame.draw.rect(screen,YELLOW,[func.rect1_x3,func.rect_y1,func.rect1_wid3,30])

		func.rect2_5=pygame.draw.rect(screen,YELLOW,[func.rect1_x4,func.rect_y1,func.rect1_wid4,30])


		func.rect1_x-=6
		func.rect1_x1-=6
		func.rect1_x2-=6
		func.rect1_x3-=6
		func.rect1_x4-=6

		if func.rect1_x1<=-400:
			func.rect1_x=func.rect1_x4+func.rect1_wid4+150
			#func.rect1_wid=random.randrange(350,400)

		if func.rect1_x2<=-400:
			func.rect1_x1=func.rect1_x+func.rect1_wid+150
			#func.rect1_wid1=random.randrange(350,400)

		if func.rect1_x3<=-400:
			func.rect1_x2=func.rect1_x1+func.rect1_wid1+150
			#func.rect1_wid2=random.randrange(350,400)

		if func.rect1_x4<=-400:
			func.rect1_x3=func.rect1_x2+func.rect1_wid2+150
			#func.rect1_wid3=random.randrange(350,400)

		if func.rect1_x<=-400:
			func.rect1_x4=func.rect1_x3+func.rect1_wid3+150
			#func.rect1_wid4=random.randrange(350,400)
		
		pygame.draw.rect(screen,RED,[1050,10,300,15])
		pygame.draw.rect(screen,BLACK,[1050,10,func.vill_health,15])	
		

		screen.blit(text,[10,10])


		if func.player_lives<=5 and func.gp==0:
			func.pwe=pygame.draw.rect(screen,YELLOW,[func.pox,170,15,15]) 
			func.pox-=4
			screen.blit(func.power,func.pwe)


		if func.player_lives<=5:
			if player.colliderect(func.pwe):
				func.powerup=1
				func.gp=1


	def vill(r):
		
		if func.l==100 or func.l==0:
			func.x=random.randrange(0,2)
			if func.l==100:
				func.l=0
			if func.u==0 or func.x==0:
				func.u=1
				func.var=400
			elif func.u==1 or func.x==0:
				func.var=300
				func.u=0

		func.l+=1
		func.villain_player=pygame.Rect(1366-100,func.var-100,120,94)
		screen.blit(villain,func.villain_player)
		
		


	def stage(v):
		for m in range(fire1.get_width()+1):
		#for n in range(fire1.get_height()+1):
			i=random.randrange(0,4)
			screen.blit(fire[i],(m*35,650))
		
			
			
			
			
	def villain_bullets(r):
		if func.flag==1:
			func.z=func.var-100
			func.bull_pos=func.z+60
		func.move = -20
		func.res+=func.move
		func.flag = 0
		if player.top+player.height==func.z+120:
			func.vbullet=pygame.draw.rect(screen,BLACK,[func.res,func.bull_pos,1,1])
			screen.blit(vill_bull,func.vbullet)
		elif player.top+player.height>func.z+120:
			func.bull_pos+=2
			func.vbullet=pygame.draw.rect(screen,BLACK,[func.res,func.bull_pos,1,1])
			screen.blit(vill_bull,func.vbullet)
		elif player.top+player.height<func.z+120:
			func.bull_pos-=2
			func.vbullet=pygame.draw.rect(screen,BLACK,[func.res,func.bull_pos,1,1])
			screen.blit(vill_bull,func.vbullet)
		if player.colliderect(func.vbullet):
			func.res-=1376
			func.player_lives-=1
			
		if (func.res<=0):
			func.res=1366-150
			func.flag=1	

			
	def bullet(self):
		if player_shoot==True:
			func.pos=player.top
			func.bull=pygame.draw.rect(screen,BLACK,[func.bull_x,func.pos,1,1])
			func.w=1

		if func.powerup==1:				
			if(func.bull_x<=1366)and(func.w==1):
				func.bull=pygame.draw.rect(screen,BLACK,[func.bull_x,func.pos,1,1])
				if(f.ring<15):
					screen.blit(func.cat1,func.bull)
				elif f.ring<30:
					screen.blit(func.cat2,func.bull)
				elif f.ring<45:
					screen.blit(func.cat3,func.bull)
					f.ring=0
				f.ring+=1
				#print func.bull
				func.bull_x+=10
				if((func.bull).colliderect(func.villain_player)):
					func.vill_health+=20
					#func.bull_x=450+58
					func.w=0

			else:
				func.w=0
				func.bull_x=450+58
		else:
			if(func.bull_x<=1366)and(func.w==1):
				func.bull=pygame.draw.rect(screen,BLACK,[func.bull_x,func.pos,1,1])
				screen.blit(pl_bull,func.bull)
				func.bull_x+=10
				if((func.bull).colliderect(func.villain_player)):
					func.vill_health+=10
					func.w=0
			
			
			else:
				func.w=0
				func.bull_x=450+58
		



#--------------------------------------------------------
#-------------------------------------------------------





pygame.init()
#set clock screen and its caption
func.rect_size=100
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1366,768))#,pygame.FULLSCREEN)

func.rect_y=400-100
func.rect_y1=400

func.rect_x=0
func.rect_x1=400+150
func.rect_x2=func.rect_x1+400+150
func.rect_x3=func.rect_x2+400+150
func.rect_x4=func.rect_x3+400+150


func.rect1_x=-200
func.rect1_x1=200+150
func.rect1_x2=func.rect_x1+200+150
func.rect1_x3=func.rect_x2+200+150
func.rect1_x4=func.rect_x3+200+150

func.rect_wid=400
func.rect_wid1=400
func.rect_wid2=400
func.rect_wid3=400
func.rect_wid4=400

func.rect1_wid=400
func.rect1_wid1=400
func.rect1_wid2=400
func.rect1_wid3=400
func.rect1_wid4=400

swat=[]
swat_run2=pygame.image.load('swat-run4.png')
swat.append(swat_run2)
swat_run3=pygame.image.load('swat-run5.png')
swat.append(swat_run3)
swat_run4=pygame.image.load('swat-run6.png')
swat.append(swat_run4)
swat_run1=pygame.image.load('swat-run3.png')
swat.append(swat_run1)

swat_jump1=pygame.image.load('swat-jump1.png')
swat.append(swat_jump1)
swat_jump2=pygame.image.load('swat-jump2.png')
swat.append(swat_jump2)
swat_jump3=pygame.image.load('swat-jump3.png')
swat.append(swat_jump3)
swat_jump4=pygame.image.load('swat-jump4.png')
swat.append(swat_jump4)

won=pygame.image.load("win.png")
lost=pygame.image.load("lost.png")

fire=[]
fire1=pygame.image.load('1.png')
fire.append(fire1)
fire2=pygame.image.load('2.png')
fire.append(fire2)
fire3=pygame.image.load('3.png')
fire.append(fire3)
fire4=pygame.image.load('4.png')
fire.append(fire4)


vill_bull=pygame.image.load('cat4.png')
pl_bull=pygame.image.load('bul1.png')

back=pygame.image.load('level2_back.jpg')


player = pygame.Rect(450,300-46, 58, 50)

villain=pygame.image.load('dark.png')
#print swat
player_up=player_down=player_left=False
player_right=True
player_shoot=False
pause=False

i=0
k=0
rect=[0,0,0,0]
rect1=[0,0,0,0]
f=func()
z=0
y=0
x=0
p=0


change_down=70



#---------------------------------------------------------------------------------------------------------------




const=1366
while(True):

	screen.blit(back,[0,0])

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

		if event.type==KEYDOWN:
		#if event.key==K_RIGHT:
			#player_right=True
			if event.key==K_UP:
				player_up=True
				#i=5

			elif event.key==K_SPACE and f.w==0:
				player_shoot=True
			
			if event.key==K_1:
				pause=True
				
			if event.key==K_2:
				pause=False
			
			if event.key==K_c:
				f.player_lives=10

			
		if event.type==KEYUP:
			#if event.key==K_RIGHT:
				#player_right=False
				#i=0
			if event.key==K_UP:
				player_up=False
				#i=0

			if event.key==K_SPACE:
				player_shoot=False
	
			if event.key==K_ESCAPE:
				pygame.quit()
				sys.exit()



#level1
#


	if(pause):
		continue
	

	f.fun()



	


#LEVEL 1 ----------------------------------------------------------------------

	#player_right== True: #and i<=3:
	#player.move_ip(1*8,0)
		
	if player_up==True:
		player_up=False
		for j in range(4,6):
			player.move_ip(0,-1*70)
			screen.blit(back,[0,0])
			f.fun()
			
			screen.blit(swat[j],player)
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			pygame.display.update()
			clock.tick(15)
	
		for j in range(6,8):
			player.move_ip(0,change_down)
			
			#print change_down
			screen.blit(back,[0,0])
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			if player.colliderect(f.rect2_1):
				change_down=0-28
				rect=f.rect2_1
				z=1
			elif player.colliderect(f.rect2_2):
				change_down=0-28
				rect=f.rect2_2
				z=1
			elif player.colliderect(f.rect2_3):
				change_down=0-28
				rect=f.rect2_3
				z=1
			elif player.colliderect(f.rect2_4):
				change_down=0-28
				rect=f.rect2_4
				z=1
			elif player.colliderect(f.rect2_5):			
				change_down=0-28
				rect=f.rect2_5
				z=1

			#2nd
			elif player.colliderect(f.rect1_1):
				change_down=0-28
				rect1=f.rect1_1
				y=1
				z=0
			elif player.colliderect(f.rect1_2):
				change_down=0-28
				rect1=f.rect1_2
				y=1
				z=0
			elif player.colliderect(f.rect1_3):
				change_down=0-28
				rect1=f.rect1_3
				z=0
				y=1
			elif player.colliderect(f.rect1_4):
				change_down=0-28
				rect1=f.rect1_4
				y=1
				z=0

			
			elif player.colliderect(f.rect1_5):			
				change_down=0-28
				rect1=f.rect1_5
				y=1
				z=0

			else:
				change_down=70
				rect=[0,0,0,0]
				z=1
				y=1
			#change_down=70
			screen.blit(swat[j],player)
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			pygame.display.update()
			clock.tick(15)
		#i=0


	if player.colliderect(f.rect2_1):
		change_down=0-28
		rect=f.rect2_1
		z=1
		y=0
		f.pos=300-46
		
	elif player.colliderect(f.rect2_2):
		change_down=0-28
		rect=f.rect2_2
		z=1
		y=0
		f.pos=300-46
	elif player.colliderect(f.rect2_3):
		change_down=0-28
		rect=f.rect2_3
		z=1
		y=0
		f.pos=300-46
	elif player.colliderect(f.rect2_4):
		change_down=0-28
		rect=f.rect2_4
		z=1
		y=0
		f.pos=300-46
	elif player.colliderect(f.rect2_5):			
		change_down=0-28
		rect=f.rect2_5
		z=1
		y=0
		f.pos=300-46



	#2nd
	elif player.colliderect(f.rect1_1):
		change_down=0-28
		rect1=f.rect1_1
		y=1
		z=0
		f.pos=400-46

	elif player.colliderect(f.rect1_2):
		change_down=0-28
		rect1=f.rect1_2
		y=1
		z=0
		f.pos=400-46

	elif player.colliderect(f.rect1_3):
		change_down=0-28
		rect1=f.rect1_3
		y=1
		z=0
		f.pos=400-46

	elif player.colliderect(f.rect1_4):
		change_down=0-28
		rect1=f.rect1_4
		y=1
		z=0
		f.pos=400-46
	
	elif player.colliderect(f.rect1_5):			
		change_down=0-28
		rect1=f.rect1_5
		y=1
		z=0
		f.pos=400-46

	else:
		rect=[0,0,0,0]
		rect1=[0,0,0,0]
		z=1
		y=1
		f.pos=400-46
		x=1



	#if((player.left>=f.rect1_1[0]+f.rect1_1[2])or(player.left>=f.rect1_2[0]+f.rect1_2[2])or(player.left>=f.rect1_3[0]+f.rect1_3[2])or(player.left>=f.rect1_4[0]+f.rect1_4[2])or(player.left>=f.rect1_5[0]+f.rect1_5[2]))and(z==1):

		

	#2nd
	if(500>=rect1[0]+rect1[2]and(y==1)and(z==0)):
		y=0
		z=1
		x=1
		
		change_down=70-21
		for j in range(6,8):
			player.move_ip(0,change_down)		
			screen.blit(back,[0,0])
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			#change_down=70
			screen.blit(swat[j],player)
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			pygame.display.update()
			clock.tick(15)
					
	#print rect1[0]+rect1[2]


	elif (480>=rect[0]+rect[2]and(z==1)and(y==0)):
		z=0
		x=0
		
		change_down=70-21
		for j in range(6,8):
			player.move_ip(0,change_down)		
			screen.blit(back,[0,0])
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			#change_down=70
			screen.blit(swat[j],player)
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			pygame.display.update()
			clock.tick(15)
			
	#print f.pos

	if((x==0)):
#		z=0
#		x=0		
		change_down=100-21
		for j in range(6,8):
			player.move_ip(0,change_down)		
			screen.blit(back,[0,0])
			f.fun()
			#change_down=70
			screen.blit(swat[j],player)
			f.fun()
			f.vill()
			f.villain_bullets()
			f.stage()
			f.bullet()
			pygame.display.update()
			clock.tick(15)
			#screen.blit(text,[10,10])
		global fb
		fb=1
		break
		#exit(0)


	change_down=70
		
#---------------------------------------------------------------------------------------------------------


#--------------------------Game over-------------------------------------------------------------


	#if player_shoot==True:
		#pygame.draw.rect(screen,BLACK,[bull_x,bull_y,10,10])
		#w=1
	
	#if(bull_x<=1366)and(w==1):
		#pygame.draw.rect(screen,BLACK,[bull_x,bull_y,10,10])
		#bull_x+=10
	#else:
		#w=0
		#bull_x=450


	if f.player_lives==0:
		global fb
		fb=1
		break
	
	if f.vill_health>=300:
		global fb
		fb=0
		break
#--------------------------------------------------------------------------------------------------------	

	
	#rect=[0,0,0,0]
	#screen.fill(BLACK)
	if(k==2):
		screen.blit(swat[i], player)
		i+=1
		k=0
		pygame.display.update()
	else:
		k+=1
		screen.blit(swat[i], player)

	
#	if(Player_shoot==True):
#		pygame.draw.circle()

	f.vill()
	f.villain_bullets()
	f.stage()
	f.bullet()
	if i==3:
		#player.move_ip(-1*2,0)
		i=0
		#print i



		
#--------------------------------fire--------------------------------------------------------------------
	

#--------------------------------------------------------------------------------------------------------
	
	

	pygame.display.update()
	clock.tick(40)


if fb==0:
	while(True):
	
		#screen.blit(won,(0,0))
		screen.fill((0,0,0))
		back=pygame.transform.scale(won,(1080,560))
		screen.blit(won,(180,0))
		font=pygame.font.Font(None,50)
		text0=font.render("YOU WON",True,WHITE)
		screen.blit(text0,(900,365))

		
		for event in pygame.event.get():
			if(event.type==pygame.KEYDOWN):
				if event.key==K_ESCAPE:
					pygame.quit()
					sys.exit()


		pygame.display.update()

elif fb==1:
	while(True):
	
		#screen.blit(won,(0,0))
		screen.fill((0,0,0))
		back=pygame.transform.scale(lost,(1080,560))
		screen.blit(lost,(180,0))
		font=pygame.font.Font(None,50)
		text0=font.render("YOU LOST",True,WHITE)
		screen.blit(text0,(900,365))

		
		for event in pygame.event.get():
			if(event.type==pygame.KEYDOWN):
				if event.key==K_ESCAPE:
					pygame.quit()
					sys.exit()


		pygame.display.update()



pygame.quit()
