## some basic collision rules ##
## nothing important to see here, move along please ##


def collision(sprite1, sprite2):
	# check for collision between sprites 1 and 2
	# made it into a nested if to make it more readable
	if sprite1.x < sprite2.x + sprite2.w:
		if sprite1.x + sprite1.w > sprite2.x:
			if sprite1.y < sprite2.y + sprite2.h:
				if sprite1.y + sprite1.h > sprite2.y:
					return True
	return False