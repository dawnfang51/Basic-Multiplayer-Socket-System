import socket
import os
import random
import sys
import pickle

class Player:
	def __init__(self, name):
		self.name = name
		self.max_health = 100
		self.health = self.max_health
		self.attack = 20


def Main():
	os.system("cls")
	print "What do you want to do?\n"
	print "1.) Start"
	print "2.) Quit"
	option = raw_input("-> ")
	if option == "1":
		startp()
	elif option == "2":
		sys.quit()
	else:
		Main()

def startp():
	os.system('cls')
	print "What is your name?"
	option = raw_input("-> ")

	if len(option) < 1:
		startp()

	else:
		global PlayerIG
		PlayerIG = Player(option)
		Start()

def Start():
	os.system('cls')
	print "What do you want to do?"
	print "1.) Fight"
	print "2.) Exit"
	option = raw_input("-> ")
	if option == "1":
		Mp_Main()
	elif option == "2":
		sys.exit()
	else:
		Start()

def Mp_Format(name, health):
	os.system('cls')
	print "================================"
	print "|%s vs %s"  % (PlayerIG.name, name)
	print "|==============================="
	print "|%s Health: %i" % (name, health)
	print "|%s Health: %i" % (PlayerIG.name, PlayerIG.health)
	print "================================"
	print "| 1.) Attack"
	global mpinput
	mpinput = raw_input("->")
	if mpinput != "1":
		Mp_Format(name, health)

def Damage_Dealt(x, y):
	os.system('cls')
	print "You take %i damage" % x
	print "You deal %i damage to %s" % (y, Enemy.name)
	option = raw_input(' ')

def win():
	print "Congratulations you have defeated %s" % Enemy.name
	option = raw_input(' ')
	Start()

def lose():
	print "You have lost against %s" % Enemy.name
	option = raw_input(' ')
	Start()


def Mp_Main():
	host = '192.168.1.22'
	port = 7890

	s = socket.socket()
	s.connect((host, port))
	os.system('cls')
	print "Waiting for other player to connect."
	PlayerObj = pickle.dumps(PlayerIG)
	s.send(PlayerObj)
	global Enemy
	Enemy = s.recv(1024)
	Enemy = pickle.loads(Enemy)

	while True:
		Mp_Format(Enemy.name, Enemy.health)
		s.send(mpinput)
		os.system('cls')
		print "Waiting for other player to respond..."
		Damage = s.recv(1024)
		Damage = pickle.loads(Damage)
		Damage_Dealt(PlayerIG.health-Damage[0], Enemy.health-Damage[1])
		PlayerIG.health = Damage[0]
		Enemy.health = Damage[1]
		if Damage[2] != 0:
			if Damage[2] == 1:
				win()
			elif Damage[2] == 2:
				lose()

		
	s.close()

if __name__ == '__main__':
	Main()


