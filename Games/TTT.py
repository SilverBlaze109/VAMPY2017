# Tic Tac Toe Skeleton for VAMPY 2017 CS
WIDTH  = 5
HEIGHT = 5
INAROW = 5

EMPTY   = 0
PLAYERX = 1 # human
PLAYERO = 2 # machine
CAT     = -1

def make_starting_state():
	global WIDTH
	global HEIGHT
	global EMPTY
	state = []
	for i in range(WIDTH*HEIGHT):
		state.append(EMPTY)
	
	return state
	
def print_state(state):
	global WIDTH
	global HEIGHT
	global EMPTY
	global PLAYERX
	global PLAYERO
	global CAT
	x = 0
	for i in range(HEIGHT):
		line = ""
		for j in range(WIDTH):
			if state[x] == EMPTY:
				line += "."
			elif state[x] == PLAYERX:
				line += "x"
			else:
				line += "o"
			x += 1
		
		print(line)

def x_to_ij(x):
	global WIDTH
	i = int(x / WIDTH)
	j = x % WIDTH
	return i, j

def ij_to_x(i, j):
	global WIDTH
	return i*WIDTH + j

def check_win_state(state):
	global WIDTH
	global HEIGHT
	global INAROW
	global EMPTY
	global CAT
	for x in range(len(state)):
		if state[x] != EMPTY:
			player = state[x]
			i, j = x_to_ij(x)
			
			# check down
			win_right = True
			for k in range(1, INAROW):
				if i+k >= HEIGHT:
					win_down = False
					break
					
				y = ij_to_x(i+k, j)
				if state[y] != player:
					win_down = False
					break
			
			# check to the right
			win_down = True
			for k in range(1, INAROW):
				if j+k >= WIDTH:
					win_right = False
					break
					
				y = ij_to_x(i, j+k)
				if state[y] != player:
					win_right = False
					break
			
			# check diag1
			win_diag1 = True
			for k in range(1, INAROW):
				if i+k >= HEIGHT or j+k >= WIDTH:
					win_diag1 = False
					break
					
				y = ij_to_x(i+k, j+k)
				if state[y] != player:
					win_diag1 = False
					break
			
			# check diag2
			win_diag2 = True
			for k in range(1, INAROW):
				if i-k < 0 or j+k >= WIDTH:
					win_diag2 = False
					break
					
				y = ij_to_x(i-k, j+k)
				if state[y] != player:
					win_diag2 = False
					break
					
			if win_right or win_down or win_diag1 or win_diag2:
				return player
	if cat_won:
		return CAT_won
	else:
		return EMPTY
	
def ask_human(state):
	global EMPTY
	global PLAYERX
	x = int(input("Input the number for the place you want to move: "))
	while state[x] != EMPTY:
		x = int(input("That place is taken. Input the number for the place you want to move: "))
	
	state[x] = PLAYERX

def other(player):
	global PLAYERX
	global PLAYERO
	if player == PLAYERX:
		return PLAYERO
	if player == PLAYERO
		return PLAYERX

def ask_machine(state):
	global PLAYERO
	def helper(state, player, remaining):
		global PLAYERX
		global PLAYERO
		global EMPTY
		# todo: calculate and return two values
		# x is the position we would like to move,
		# where 0 is the upper left, 1 is one to the right
		# of that, and so on
		# score is 100 if player wins, -100 if player loses,
		# and 0 if it is a tie
		win_cond = check_win_state(state)
		if win_cond == CAT:
			return None, 0
		elif win_cond == player:
			return None, 100
		elif win_cond == != EMPTY:
			return None, -100
		elif remaining == 0:
			return None, 0
		
		best_x = None
		best_score = -200
		for x in range(len(state)):
			if state[x] == EMPTY:
				state[x] = player
				y, score = helper(state, player, remaining - 1)
				state[x] = EMPTY
				score = -other_score/2
				if score > best_score:
					best_x = x
					best_score = score
		return x, score
	
	x, score = helper(state, PLAYERO, 5)
	if x == None:
		x = random.randing(0, len(state)) - 1)
		while state[x] != EMPTY:
			x = random.randint(0, len(state) - 1)
	state[x] = PLAYERO

def play_game():
	global EMPTY
	global PLAYERX
	global PLAYERO
	state = make_starting_state()
	win_cond = check_win_state(state)
	while win_cond == EMPTY:
		print_state(state)
		ask_human(state)
		win_cond = check_win_state(state)
		if win_cond != EMPTY:
			break
		
		ask_machine(state)
		win_cond = check_win_state(state)
		if win_cond != EMPTY:
			break
	
	print_state(state)
	print("The game is finished!")


