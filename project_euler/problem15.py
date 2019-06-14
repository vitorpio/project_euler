def check_move(pos):
	return pos[0] <= width and pos[1] <= height

def move(pos):
	global routes
	global routes_found

	if pos != end_pos:
		pos_str = '_'.join([str(pos[0]), str(pos[1])])
		if pos_str in routes_found:
			routes += routes_found[pos_str]
		else:
			# right
			right_move_pos = (pos[0]+1, pos[1])
			if check_move(right_move_pos):
				move(right_move_pos) 
			#down
			down_move_pos = (pos[0], pos[1]+1)
			if check_move(down_move_pos):
				move(down_move_pos)
	else:	
		routes += 1

height = 21
width = 21

end_pos = (width, height)

routes_found = {}

for x in range(width, 0, -1):
	for y in range(height, 0, -1):
		routes = 0
		move((x,y))
		pos_str = '_'.join([str(x),str(y)])
		routes_found[pos_str] = routes

print(routes_found['1_1'])
		
