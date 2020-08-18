def collision(sprite1, sprite2):
	if sprite1.x < sprite2.x + sprite2.w:
		if sprite1.x + sprite1.w > sprite2.x:
			if sprite1.y < sprite2.y + sprite2.h:
				if sprite1.y + sprite1.h > sprite2.y:
					return True
	return False


def sprite_sprite_collision(sprite1, sprite2, resp):
	if collision(sprite1, sprite2):
		resp(sprite1, sprite2)
	return

def sprite_group_collision(sprite, group, resp):
	for obj in group:
		if collision(sprite, obj):
			resp(sprite, obj)
	return

def group_group_collision(group1, group2, resp):
	for obj in group1:
		for pbj in group2:
			if collision(obj, pbj):
				resp(obj, pbj)
	return