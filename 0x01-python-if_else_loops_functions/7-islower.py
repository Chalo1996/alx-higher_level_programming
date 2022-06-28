#!/usr/bin/python3
def islower(c):
	ch = ord(c)
	if ch in range(ord('A'), ord('Z') + 1):
		return False
	else:
	 return True
