import pygame,sys,random    #to import required modules
from pygame.locals import*	#to use some constants such as quit and k_up

WHITE=(0,0,0)
RED=(255,0,0)
WH=(255,255,255)

pygame.init()
intro=[]
flag=0
fb=1
screen=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)



#
intro1=pygame.image.load("d1.png")

clock = pygame.time.Clock()

intro.append(intro1)
intro2=pygame.image.load("d2.png")
intro.append(intro2)
intro3=pygame.image.load("d3.png")
intro.append(intro3)
intro4=pygame.image.load("d4.png")
intro.append(intro4)
intro5=pygame.image.load("d5.png")
intro.append(intro5)
intro6=pygame.image.load("d6.png")
intro.append(intro6)
intro7=pygame.image.load("d7.png")
intro.append(intro7)
intro8=pygame.image.load("d8.png")
intro.append(intro8)
intro9=pygame.image.load("d9.png")
intro.append(intro9)
intro10=pygame.image.load("d10.png")
intro.append(intro10)
back1=pygame.image.load("welc.png")
welcome=False
while(True):
	rect_list=[]
	rect_list1=[]	
	
	screen.fill((0,0,0))
	back=pygame.transform.scale(back1,(1080,560))
	screen.blit(back,(180,0))
	font=pygame.font.Font(None,30)
	text0=font.render("Prepared by-",True,WH)
	screen.blit(text0,(900,365))
	text=font.render("Rohan Doshi (06)",True,WH)
	screen.blit(text,(900,400))
	text1=font.render("Rushikesh Fanse (08)",True,WH)
	screen.blit(text1,(900,435))
	text2=font.render("Prasad Ghangal (12)",True,WH)
	screen.blit(text2,(900,470))
	text3=font.render("Pranay Jaipuriya (24)",True,WH)
	screen.blit(text3,(900,510))
	text4=font.render("Kirtish Dhande (41)",True,WH)
	screen.blit(text4,(900,545))
	text5=font.render("Guided by-Professor Ketan bahulkar",True,WH)
	screen.blit(text5,(900,600))
	
    
	for event in pygame.event.get():
	    if(event.type==pygame.KEYDOWN):
		if event.key==K_ESCAPE:
		    pygame.quit()
		    sys.exit()
		elif event.key==K_SPACE:
		    welcome=True
	if fb==0:
		break
	
	if welcome:
	    welcome=False
	    break
	pygame.display.update()

screen.fill(WHITE)



for i in range(0,10):
	screen1=pygame.transform.scale(intro[i],(1080,560))
	screen.blit(screen1,(150,100))
	pygame.display.update()
	clock.tick(3)
	#print 1
while 1:

	font1=pygame.font.Font(None,50)
	text=font1.render(" OHH ! IT SEEMS LIKE EVEN NATURE WANNA TEST OUR MIGHT...",True,RED)
	text2=font1.render("ITS GOING TO BE HARD TIME TRAVERSING THROUGH THIS CAVE LETS SEE....",True,RED)

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
import stage1
