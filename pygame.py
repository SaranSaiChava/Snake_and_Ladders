from random import randint



def game_init():
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	p1_pos=0
	p2_pos=0
	steps=0
	lad_list=[4,9,20,28,40,51,63,71]
	sn_list=[17,54,62,64,87,93,95,99]
	lad_dict={4:14,9:31,20:38,28:84,40:59,51:67,63:81,71:91}
	sn_dict={17:7,54:34,62:19,64:60,87:24,93:73,95:75,99:78}



def coin_set_p1(new_pos_p1):
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	if(p1_pos+new_pos_p1>100):
		print("-")
	else:
		p1_pos+=new_pos_p1
		ladders(p1_pos,1)
		snakes(p1_pos,1)

def coin_set_p2(new_pos_p2):
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	if(p2_pos+new_pos_p2>100):
		print("-")
	else:
		p2_pos+=new_pos_p2
		ladders(p2_pos,2)
		snakes(p2_pos,2)




def ladders(climb,player_a):
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	if(climb in lad_list):
		if(player_a==1):
			print("Yay!! Player 1 is now on ladder")
			p1_pos=lad_dict[climb]
		else:
			print("Yay!! Player 2 is now on ladder")
			p2_pos=lad_dict[climb]

def snakes(fall,player_b):
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	if(fall in sn_list):
		if(player_b==1):
			print("Ohh!! Player 1 should get some snake medicine")
			p1_pos=sn_dict[fall]
		else:
			print("Ohh!! Player 2 should get some snake medicine")
			p2_pos=sn_dict[fall]



def game_start():
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	while(True):
		print(p1_pos,p2_pos)
		if(p1_pos<100 and p2_pos<100):
			steps+=1
			if (steps%2!=0):
				print("Player 1, Please roll the dice")
				p1_play=input()
				if(p1_play=='r'):
					p1_feed=roll_die()
					while(p1_feed==6):
						print(p1_pos,p2_pos)
						print("YAY!!! You got another chance")
						print("Player 1, Please roll the dice")
						coin_set_p1(p1_feed)
						p1_play=input()
						if(p1_play=='r'):
							p1_feed=roll_die()
						elif(p1_play=='Q'):
							game_quit(p1_pos)
					coin_set_p1(p1_feed)
				elif(p1_play=='Q'):
					game_quit(p1_pos)
			else:
				print("Player 2, Please roll the dice")
				p2_play=input()
				if(p2_play=='r'):
					p2_feed=roll_die()
					while(p2_feed==6):
						print(p1_pos,p2_pos)
						print("YAY!!! You got another chance")
						print("Player 2, Please roll the dice")
						coin_set_p2(p2_feed)
						p2_play=input()
						if(p2_play=='r'):
							p2_feed=roll_die()
						elif(p2_play=='Q'):
							game_quit(p1_pos)
					coin_set_p2(p2_feed)
				elif(p2_play=='Q'):
					game_quit(p1_pos)
		else:
			game_end()


def roll_die():
	return(randint(1,6))

def game_quit(a):
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	if(a==p1_pos):
		print("Sorry!, Player one left the game")
	if(a==p2_pos):
		print("Sorry!, Player two left the game")
	game_end()




def game_end():
	global p1_pos,p2_pos,steps,lad_list,sn_list,lad_dict,sn_dict
	if(p1_pos==100):
		print("Yay!!! Player one, You won")
	elif(p2_pos==100):
		print("Yay!!! Player two, You won")
	else:
		print("Game-Over")
	quit()

def quit():
	exit()


if __name__ == "__main__":
	game_init()
	print("Press enter to start")
	if(input()==""):
		game_start()
	else:
		quit()
	
