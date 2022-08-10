import random
import time
import os
S='         \/ \n         /\ \n        /  \ \n       00  00           \n  \n      scissor'         
P=('         _____ \n        /……™./ \n       /………./ \n      /…™…./        \n \n      paper')
R=('      ,o0o, \n      o000o \n      \'o0o\' \n \n      rock')
print('	R-rock  P-paper S-scissor')
print()
global finalscore
finalscore=int(input('         Enter maximum score:'))
print()

global list
list=[R,P,S]
global uscore
uscore=0
global cscore
cscore=0


def game():
	global list
	global finalscore
	global uscore
	global cscore
	user=False
	while user==False:
		user=str(input('		Enter:'))
		if user=='R':
			user=R
		if user=='P':
			user=P
		if user=='S':
			user=S
		comp=random.choice(list)
	
	
		if user==R:
			if comp==S:
				uscore+=1
			if comp==P:
				cscore+=1
		if user==P:
			if comp==R:
				uscore+=1
			if comp==S:
				cscore+=1
		if user==S:
			if comp==P:
				uscore+=1
			if comp==R:
				cscore+=1
		os.system('clear')
		

		
		print()	
		print (comp)
		print ('______________________      Computer:',cscore)
		print()	
		print(user)
		print('______________________          You:',uscore)
		print ()
		
		if user==comp:
			print('		_ TIE _')
		
	
		print()
		print()
		if uscore==finalscore:
			print('		**YOU WON**')
			print()
			print('		--Created by Jayaram--')
			time.sleep(999)
		if cscore==finalscore:
			print ('		**YOU LOST**')
			print()
			print('		--Created by Jayaram--')
			time.sleep(999)		
			
		user=False			
			
	
		
game()	
	

     				
