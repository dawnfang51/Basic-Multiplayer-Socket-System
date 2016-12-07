import socket
import random
import pickle

class Player:
	def __init__(self, name):
		self.name = name
		self.max_health = 100
		self.health = self.max_health
		self.attack = 10

def Battle(x, y):
	print "debugger here"
	if x == "1":
		print "debug2"
		global dmg1
		dmg1 = random.randint(int(Player1.attack/3), Player1.attack)
		Player2.health -= dmg1
	if y == "1":
		global dmg2
		dmg2 = random.randint(int(Player2.attack/3), Player2.attack)
		Player1.health -= dmg2
		if Player1.health <= 0:
			global win2
			win2 = 1
			global win1
			win1 = 2
			global win
		elif Player2.health <= 0:
			global win2
			win2 = 2
			global win1
			win1 = 1 



def Main():
	host = '192.168.1.22'
	port = 7890
	global win1
	win1 = 0
	global win2
	win2 = 0

	s = socket.socket()
	s.bind((host, port))

	print "debug"
	s.listen(1)
	c1, addr1 = s.accept()
	print "Connection from: " + str(addr1)
	s.listen(1)
	c2, addr2 = s.accept()
	print "Connection from: " + str(addr2)

	data1 = c1.recv(1024)
	global Player1
	Player1 = pickle.loads(data1)
	data2 = c2.recv(1024)
	global Player2
	Player2 = pickle.loads(data2)
	c1.send(data2)
	c2.send(data1)
	
	while True:
		print "Before Recieve"
		data1 = c1.recv(1024)
		data2 = c2.recv(1024)
		print "After Recieve"
		Battle(data1, data2)
		Health1 = Player1.health
		Health2 = Player2.health
		THealth1 = pickle.dumps([Health1, Health2, win1])
		THealth2 = pickle.dumps([Health2, Health1, win2])
		c1.send(THealth1)
		c2.send(THealth2)



	

	c1.close()
	c2.close()
if __name__ == "__main__":
	Main()

		
