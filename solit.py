import random
import time

#global variables
game_check = False #whether one game is finished or not
exit_game = 0
score_count = 0
black = ['b','e'] #last letters of ♣ & ♠
red = ['d','t'] #last letters of ♦ & ♥
firs = 0       # <- list row determiner
index_count = 0 # <- list index determiner
shown_cards=[]
suit_deck = {'Diamonds':["00"], 'Hearts':["00"], 'Clubs':["00"], 'Spades':["00"]}
high_scores=[1000,2000,5000,3000]
play_field = {1:[[]],2:[[]],3:[[]],4:[[]],5:[[]],6:[[]],7:[[]]}
card_choice = 0

def start(): #menu
	print("SOLITAIRE")
	print("[1] New Game")
	print("[2] Load Game")
	print("[3] High Scores")
	print("[4] Exit")

def cardNames() : #creates deck
	suits = ['diamond', 'heart', 'club', 'spade']
	cards = []

	for card_num in range(1, 14) :
		for card_suit in suits :
			str_card = str(card_num) if card_num > 9 else '0' + str(card_num) 
			cards.append(str_card + card_suit)
	random.shuffle(cards)
	return cards

def init_cards(): #creates rows of cards
	global play_field
	rows = 1
	while rows != 8:
		for rowc in range(0,rows):
			row = []
			row.append(cards[0:rows])
		del[cards[0:rows]]
		play_field[rows] = row
		rows+=1
	return play_field

def show():
	global shown_cards
	print()
	print("COLUMN")
	for firs in play_field:
		print("[",firs,"]	",end="")
		for cardss in play_field[firs][-1]:
			if cardss == play_field[firs][-1][-1]:
				shown_cards.append(cardss)				#appends cards to show 
				shown_cards = list(set(shown_cards))	#makes list unique
			if cardss in shown_cards:
				print(cardss,"	",end="")
			else:
				print(" x  	",end="")
		print()
	print("SUIT 		LAST CARD ON DECK")
	for first in suit_deck: 							#show first card on stack of suits to complete
		print(first,"           	",suit_deck[first][-1])
	print("SCORE =",score_count)
	print("\nCARDS REMAINING ON FREE DECK:",len(cards))
	if len(cards) != 0:	
		print("LAST CARD ON FREE DECK:",cards[0])
	print("")
	return suit_deck

def choose_card(): 
	global firs, card_choice, index_count, exit_game
	index_count = 0
	print("(Enter F to show next card on free deck)")
	print("(Enter E to EXIT game)")
	card_choice = input("Enter card choice (CASE SENSITIVE):	")
	find = 0
	if card_choice == "F":						#Get card from free deck
		cards.append(cards[0])					#Puts card on of last free deck stack
		cards.pop(0)							#deletes copy of card(uniqueness)
		find = 1
		return show(),choose_card()
	if card_choice == "E":
		exit_game = 1
		return exit_game
	if len(cards) != 0 and card_choice == cards[0]: 				#Chosen card is on free deck CASE
		print(card_choice,"chosen!")
		find = 1								#find = True
	for firs in play_field:
		index_count = 0
		for cardss in play_field[firs][-1]:
			index_count += 1 					#Search of card in playing field
			if card_choice == cardss: 
				print(card_choice,"chosen!")
				find = 1						#find = True
				return firs, index_count
	if find == 0:
		print("CARD NOT FOUND\n")
		return choose_card()

def move_card():
	global index_count, score_count
	print("(1 - Move card | 2 - Add card to suit deck)")
	col0_choice = input("Enter move choice:	")
	if col0_choice == "2":		#add to suit deck OPTION
		deck_choice = input("Which deck?(FIRST LETTER)	")
		if deck_choice == "D":
			if card_choice[-1] == "d":
				if int(suit_deck["Diamonds"][-1][0:2]) == int(card_choice[0:2])-1:
					suit_deck["Diamonds"].append(card_choice) #add card to diamonds
					if card_choice in play_field[firs][-1]:	#check card origin
						play_field[firs][-1].pop(-1)
						score_count+=10	
					elif card_choice in cards:
						cards.pop(0)						#deletes copy of card(FREE DECK)
						score_count+=10
				else:
					print('INVALID MOVE')
					return choose_card(),move_card()
			else:
				print('INVALID MOVE') 
				return choose_card(),move_card()
		elif deck_choice == "C":
			if card_choice[-1] == "b":
				if int(suit_deck["Clubs"][-1][0:2]) == int(card_choice[0:2])-1:
					suit_deck["Clubs"].append(card_choice)	#add card to clubs
					if card_choice in play_field[firs][-1]:	#check card origin
						play_field[firs][-1].pop(-1)		#deletes copy of card
						score_count+=10
					elif card_choice in cards:
						cards.pop(0)						#deletes copy of card(FREE DECK)
						score_count+=10
				else:
					print('INVALID MOVE') 
					return choose_card(),move_card()
			else:
				print('INVALID MOVE') 
				return choose_card(),move_card()
		elif deck_choice == "S":
			if card_choice[-1] == "e":
				if int(suit_deck["Spades"][-1][0:2]) == int(card_choice[0:2])-1:
					suit_deck["Spades"].append(card_choice) #add card to spades
					if card_choice in play_field[firs][-1]: #check card origin
						play_field[firs][-1].pop(-1)		#deletes copy of card
						score_count+=10
					elif card_choice in cards:
						cards.pop(0)						#deletes copy of card(FREE DECK)					
						score_count+=10
				else:
					print('INVALID MOVE')
					return choose_card(),move_card()
			else:
				print('INVALID MOVE')
				return choose_card(),move_card()
		elif deck_choice == "H":
			if card_choice[-1] == "t":
				if int(suit_deck["Hearts"][-1][0:2]) == int(card_choice[0:2])-1:
					suit_deck["Hearts"].append(card_choice) #add card to hearts
					if card_choice in play_field[firs][-1]: #check card origin
						play_field[firs][-1].pop(-1)		#deletes copy of card
						score_count+=10							
					elif card_choice in cards:
						cards.pop(0)						#deletes copy of card(FREE DECK)
						score_count+=10
				else:
					print('INVALID MOVE') 
					return choose_card(),move_card()
			else:
				print('INVALID MOVE')
				return choose_card(),move_card()
		else:
			print('INVALID MOVE')
			return choose_card(),move_card()
	elif col0_choice == "1": #OTHER MOVE OPTIONS`
		col_choice = int(input("To which column would you take it?	"))
		if len(play_field[col_choice][-1]) == 0: #ADD KING to FREE ROW
			if int(card_choice[0:2]) == 13:
				if card_choice in shown_cards or card_choice == cards[0]: #MOVE KING FROM SHOWN CARDS
					if card_choice == cards[0]:
						play_field[col_choice][-1].append(card_choice)		#Appends card to stack
						shown_cards.append(card_choice)						#Appends to shown card on field
						cards.pop(0)
						score_count+=5
					elif card_choice == play_field[firs][-1][-1]:
						play_field[col_choice][-1].append(card_choice)		#Appends card to stack
						shown_cards.append(card_choice)						#Appends to shown card on field
						play_field[firs][-1].pop(-1)
						score_count+=5
					else:
						for x in range (index_count,len(play_field[firs][-1])):
							if play_field[firs][-1][index_count-1] != play_field[firs][-1][-1]:
								play_field[col_choice][-1].append(play_field[firs][-1][index_count-1])
								shown_cards.append(play_field[firs][-1][index_count-1])
								play_field[firs][-1].pop(index_count-1)
						play_field[col_choice][-1].append(play_field[firs][-1][-1])	#Appends last card of row to stack
						shown_cards.append(play_field[firs][-1][-1])				#Appends last card to shown card on field
						play_field[firs][-1].pop(-1)			
						score_count+=5
				else:
					print("INVALID")
					return choose_card(),move_card()
			else:
				print("INVALID")
				return choose_card(),choose_card(),move_card()
		elif len(cards) != 0 and card_choice == cards[0]: #CARD CHOICE FROM FREE DECK 
			if int(card_choice[0:2]) == int(play_field[col_choice][-1][-1][0:2])-1: #ADD SINGLE CARD TO COL CHECKER
				if card_choice[-1] in red:								#RED to BLACK ATTRIB CHECK
					if play_field[col_choice][-1][-1][-1] in black:		
						play_field[col_choice][-1].append(card_choice)	#Appends card to stack
						shown_cards.append(card_choice)					#Appends to shown card on field
						cards.pop(0)
						score_count+=5
					else:
						print('INVALID MOVE') 
						return choose_card(),move_card()
				elif card_choice[-1] in black:							#BLACK to RED ATTRIB CHECK
					if play_field[col_choice][-1][-1][-1] in red:
						play_field[col_choice][-1].append(card_choice)	#Appends card to stack
						shown_cards.append(card_choice)					#Appends to shown card on field
						cards.pop(0)
						score_count+=5
					else:
						print('INVALID MOVE') 
						return choose_card(),move_card()
				else:
					print('INVALID MOVE') 
					return choose_card(),move_card()
			else:
				print('INVALID MOVE')  
		elif int(card_choice[0:2]) == int(play_field[col_choice][-1][-1][0:2])-1 and card_choice == play_field[firs][-1][-1] : #ADD CARD TO COL CHECKER 
			if card_choice in shown_cards:
				if card_choice[-1] in red: 								#RED to BLACK ATTRIB CHECK
					if play_field[col_choice][-1][-1][-1] in black: 	
						play_field[col_choice][-1].append(card_choice)	#Appends card to stack
						shown_cards.append(card_choice)					#Appends to shown card on field
						play_field[firs][-1].pop(-1)
						score_count+=5
					else:
						print('INVALID MOVE')
						return choose_card(),move_card() 
				elif card_choice[-1] in black:							#BLACK to RED ATTRIB CHECK
					if play_field[col_choice][-1][-1][-1] in red:		
						play_field[col_choice][-1].append(card_choice)	#Appends card to stack
						shown_cards.append(card_choice)					#Appends to shown card on field
						play_field[firs][-1].pop(-1)
						score_count+=5
					else:
						print("INVALID MOVE")
						return choose_card(),move_card()
				else:
					print("INVALID MOVE")
					return choose_card(),move_card()
		elif play_field[firs][-1][-1] != card_choice: #MOVE SET OF CARDS TO COL_CHOICE
			if int(card_choice[0:2]) == int(play_field[col_choice][-1][-1][0:2])-1:
				if card_choice[-1] in red:								#RED to BLACK ATTRIB CHECK
					if play_field[col_choice][-1][-1][-1] in black:
						for x in range (index_count,len(play_field[firs][-1])):
							if play_field[firs][-1][index_count-1] != play_field[firs][-1][-1]:
								play_field[col_choice][-1].append(play_field[firs][-1][index_count-1])
								shown_cards.append(play_field[firs][-1][index_count-1])
								play_field[firs][-1].pop(index_count-1)
						play_field[col_choice][-1].append(play_field[firs][-1][-1])	#Appends last card of row to stack
						shown_cards.append(play_field[firs][-1][-1])				#Appends last card to shown card on field
						play_field[firs][-1].pop(-1)
						score_count+=5					
					else:
						print('INVALID MOVE')
						return choose_card(),move_card() 
				elif card_choice[-1] in black:							#BLACK to RED ATTRIB CHECK
					if play_field[col_choice][-1][-1][-1] in red:
						for x in range (index_count,len(play_field[firs][-1])):
							if play_field[firs][-1][index_count-1] != play_field[firs][-1][-1]:
								play_field[col_choice][-1].append(play_field[firs][-1][index_count-1])
								shown_cards.append(play_field[firs][-1][index_count-1])
								play_field[firs][-1].pop(index_count-1)
						play_field[col_choice][-1].append(play_field[firs][-1][-1])
						shown_cards.append(play_field[firs][-1][-1])
						play_field[firs][-1].pop(-1)
						score_count+=5
					else:
						print('INVALID MOVE') 
						return choose_card(),move_card()
				else:
					print('INVALID MOVE')
					return choose_card(),move_card()
			else:
				print('INVALID MOVE')	
				return choose_card(),move_card()
		else:
			print('INVALID MOVE')
			return choose_card(),move_card()
	else:
		print("INVALID MOVE")
		return choose_card(),move_card()

def check_game():
	global game_check
	for suitss in suit_deck:
		if len(suit_deck[suitss]) != 14:
			game_check = False
			return game_check
	game_check = True
	return game_check

def load_game():		#LAST SAVED GAME
	global cards, shown_cards, suit_deck, play_field, score_count
	try:
		lastgamehandler = open("save/cards.txt","r")			#last saved game cards (free deck)
		for entry in lastgamehandler:
			cline = entry
			cline_items = cline.split("*")
			for items in cline_items:
				if items != "":
					cards.append(items)
		lastgamehandler.close()
		lastgamehandler = open("save/shown_cards.txt","r")		#last saved game shown cards (appears on playing field)
		for entry in lastgamehandler:
			sline = entry
			sline_items = sline.split("*")
			for items in sline_items:
				if items != "":
					shown_cards.append(items)
		lastgamehandler.close()
		lastgamehandler = open("save/suit_deck.txt","r")		#last saved game suit deck (Ace - King)
		for entry in lastgamehandler:
			cline = entry
			cline_items = cline.split("\n")
			cline_items = cline_items[-2]
			cline_items = cline_items.split("*")
			del cline_items[-1]
			suit_deck[cline_items[0]].pop(0)
			for x in cline_items:
				if x != cline_items[0]:
					suit_deck[cline_items[0]].append(x)
		lastgamehandler.close()
		lastgamehandler = open("save/play_field.txt","r")		#last saved game playing field
		for entry in lastgamehandler:
			pline = entry
			pline_items = pline.split("*")
			del pline_items[-1]
			for x in pline_items:
				if x != pline_items[0]:
					play_field[int(pline_items[0])][-1].append(x)
		lastgamehandler.close()
		lastgamehandler = open("save/score_count.txt","r")		#last saved score count
		for entry in lastgamehandler:
			eline = entry
			eline_items = eline.split("*")
			del eline_items[-1]
			for items in eline_items:
				score_count = int(items)
		lastgamehandler.close()
		return True
	except:
		return False

def autosave_game():
	global cards, shown_cards, suit_deck, play_field, score_count
	lastgamehandler = open("save/cards.txt","w")  #cards (free deck)
	for c in cards:
		lastgamehandler.write(c+"*")
	lastgamehandler.close()
	lastgamehandler = open("save/shown_cards.txt","w")	#shown cards (appears on playing field)
	for s in shown_cards:
		lastgamehandler.write(s+"*")
	lastgamehandler.close()
	lastgamehandler = open("save/suit_deck.txt","w") 	#present suit deck (Ace - King)
	for sd in suit_deck:
		lastgamehandler.write(sd+"*")
		for sdk in suit_deck[sd]:
			lastgamehandler.write(sdk+"*")
		lastgamehandler.write("\n")
	lastgamehandler.close()
	lastgamehandler = open("save/play_field.txt","w")	#present playing field
	for p in play_field:
		lastgamehandler.write(str(p)+"*")
		for pl in play_field[p][-1]:
			lastgamehandler.write(pl+"*")
		lastgamehandler.write("\n")
	lastgamehandler = open("save/score_count.txt","w")	#present score
	lastgamehandler.write(str(score_count)+"*")
	lastgamehandler.close()

def open_savescores():
	global high_scores
	high_scores = []
	try:
		scorehandle = open("save/scores.txt","r")
		for entry in scorehandle:
			scline = entry
			scline_items = scline.split("*")
			del scline_items[-1]
			for items in scline_items:
				high_scores.append(int(items))
		scorehandle.close()
		high_scores.sort(reverse = True)
		print("\nTOP SCORES")
		for index,score in enumerate(high_scores):
			print("{",index+1,"}	-",score)
		print()
	except FileNotFoundError:
		print("\nNo High Scores Record Found!\n")
	save_scores()

def save_scores():
	global high_scores
	scorehandle = open("save/scores.txt","w")
	for i in high_scores:
		scorehandle.write(str(i)+"*")
	scorehandle.close()

def say_congrats_if_win():
	if game_check == True:
		print("\n\n							Congratulations!					\n\n") 
		high_scores.append(score_count)
		save_scores()

def reset():
	global play_field, shown_cards, suit_deck, cards, exit_game
	play_field = {1:[[]],2:[[]],3:[[]],4:[[]],5:[[]],6:[[]],7:[[]]}
	shown_cards=[]
	suit_deck = {'Diamonds':["00"], 'Hearts':["00"], 'Clubs':["00"], 'Spades':["00"]}
	cards = []
	shown_cards = []
	exit_game = 0

#Main 
start()
choice = input("ENTER:	")
while choice != "4":
	reset()
	if choice == "1":				#NEW GAME
		cards = cardNames()
		play_field = init_cards()
		while game_check == False:
			if len(cards) == 0:
				cards.append("X")
			show()
			choose_card()
			if exit_game == 1:
				break
			move_card()
			check_game()
			autosave_game()
		say_congrats_if_win()
	elif choice == "2":				#LOAD LAST GAME
		if(load_game()):
			while game_check == False:
				show()
				choose_card()
				if exit_game == 1:
					break
				move_card()
				check_game()
				autosave_game()
			say_congrats_if_win()
		else:
			print("\nNo Saved Game Found!\n")
	elif choice == "3":				#HIGH SCORE
		open_savescores()
	else:
		print("\nInvalid Input\n")
	start()
	choice = input("ENTER:	")
print("\nProgram will now close\n")
time.sleep(1)